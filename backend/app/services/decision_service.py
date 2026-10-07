"""
Decision Engine Service for Decision Arena.
Implements the end-to-end dynamic decision pipeline:
User Decision
  ↓
Detect Category & Subcategory
  ↓
Load Subcategory Configuration & Factors
  ↓
Get Candidate Pool from CandidateProvider (e.g. DummyJSON / Demo)
  ↓
Requirement / Deal-breaker / Budget Filtering Pipeline
  ↓
Specialized Autonomous Agents evaluate EVERY candidate
  ↓
Dynamic Weighted Scoring from candidate attributes & user priorities
  ↓
Rank ALL Candidates descending
  ↓
Return Top-N Results + Best Overall (or no_matches response)
"""

from typing import List, Dict, Optional, Tuple, Any
from fastapi import HTTPException, status

from ..schemas.decision import (
    DecisionInputSchema,
    DecisionEngineResultSchema,
    RankedOptionSchema,
    ComparisonMatrixSchema,
    CandidateEvaluationSchema,
    AnalysisResponseSchema,
)
from ..schemas.agent import AgentResult
from ..decision.factor_selector import (
    detect_category_and_subcategory,
    get_decision_config,
)
from ..candidates.provider_factory import get_candidate_provider
from ..candidates.dummyjson_provider import (
    ExternalCatalogUnavailableError,
    UnsupportedSubcategoryError,
)
from ..agents.agent_factory import get_specialized_agents


def calculate_confidence_heuristic(scores: List[float]) -> str:
    """
    Computes a decision confidence heuristic based on score spread.
    Spread <= 15 -> High, Spread <= 28 -> Medium, Spread > 28 -> Low.
    """
    if not scores:
        return "Medium"
    spread = max(scores) - min(scores)
    if spread <= 15.0:
        return "High"
    elif spread <= 28.0:
        return "Medium"
    else:
        return "Low"


def infer_description_factor_signals(description: str, factors: List[str]) -> Dict[str, float]:
    """Maps freeform description text to factor signals to keep recommendations responsive to user intent."""
    text = (description or "").lower()
    if not text:
        return {}

    factor_keywords = {
        "performance": ["gaming", "performance", "speed", "fast", "heavy workload", "ai", "ml", "render", "editing", "powerful", "horsepower", "torque", "acceleration"],
        "battery": ["battery", "endurance", "all-day", "long life", "lasting", "runtime", "hours per charge", "travel"],
        "camera": ["camera", "photo", "photography", "picture", "video", "selfie", "portrait", "cinematic", "low-light"],
        "display": ["display", "screen", "visual", "big screen", "amoled", "oled", "reading", "watching", "brightness", "resolution"],
        "value": ["budget", "cheap", "affordable", "value", "cost", "under", "save", "economical", "price", "inexpensive"],
        "build": ["durable", "premium build", "build quality", "rugged", "solid", "water resistance", "materials"],
        "software": ["software", "apps", "ui", "system", "ecosystem", "experience", "user experience", "os", "updates"],
        "upgradeability": ["upgrade", "future-proof", "expandable", "repairable", "modular", "long term", "memory expansion"],
        "healthFitness": ["fitness", "workout", "training", "health", "run", "running", "heart rate", "step tracking", "gps accuracy"],
        "comfort": ["comfortable", "comfort", "lightweight", "carry", "ergonomic", "seating", "ride quality", "quiet cabin"],
        "smartFeatures": ["smart features", "notifications", "gps", "music", "calling", "contactless payments", "apps"],
        "durability": ["durable", "rugged", "waterproof", "outdoor", "hardy", "scratch resistant"],
        "compatibility": ["compatibility", "sync", "works with", "integration", "android", "ios", "cross-platform"],
        "portability": ["portable", "lightweight", "easy to carry", "mobility", "thin and light"],
        "productivity": ["productivity", "multitasking", "keyboard", "note taking", "note-taking", "work tasks"],
        "soundQuality": ["sound quality", "audio quality", "bass", "soundstage", "clear audio", "music quality"],
        "noiseCancellation": ["noise cancellation", "noise cancelling", "anc", "block noise", "transparency mode"],
        "connectivity": ["connectivity", "bluetooth", "multipoint", "low latency", "connection stability"],
        "safety": ["safety", "safe", "crash rating", "airbags", "adas", "braking", "collision", "accident protection"],
        "mileage": ["mileage", "fuel economy", "fuel efficient", "fuel efficiency", "mpg", "km per liter", "running cost", "fuel consumption"],
        "space": ["space", "spacious", "cargo", "trunk", "legroom", "family room", "storage capacity"],
        "maintenance": ["maintenance", "reliability", "service cost", "repairs", "spare parts", "upkeep"],
        "returnPotential": ["return", "returns", "yield", "profit", "earning potential", "investment gains", "cagr"],
        "risk": ["risk", "low risk", "less risky", "conservative", "capital preservation", "protect my money", "volatility", "downside"],
        "liquidity": ["liquidity", "liquid", "withdraw", "cash access", "redemption", "easy access", "lock-in", "lock in"],
        "stability": ["stability", "stable", "steady", "predictable", "consistent", "job security", "secure"],
        "growth": ["growth", "grow", "long-term growth", "long term growth", "promotion", "career progression", "compound", "compounding"],
        "interestRate": ["interest rate", "low rate", "apr", "annual percentage rate", "borrowing rate"],
        "emi": ["emi", "monthly payment", "monthly repayment", "affordable payment", "repayment burden"],
        "totalCost": ["total cost", "overall cost", "fees", "processing fee", "interest paid", "cost of borrowing"],
        "tenure": ["tenure", "loan term", "repayment period", "prepayment", "flexible term"],
        "eligibility": ["eligibility", "approval", "fast approval", "documentation", "easy application"],
        "salary": ["salary", "compensation", "pay", "income", "base pay", "equity", "bonus", "highest paying"],
        "skillFit": ["skill fit", "skills", "my experience", "role fit", "technical fit", "autonomy", "passion"],
        "workLifeBalance": ["work life balance", "work-life balance", "flexible hours", "remote work", "work from home", "less overtime", "family time", "avoid burnout"],
        "learning": ["learning", "learn", "mentorship", "new skills", "training", "technology exposure"],
        "location": ["location", "commute", "near home", "relocation", "onsite", "remote location"],
        "academicQuality": ["academic quality", "academic", "curriculum", "faculty", "research", "syllabus", "teaching quality"],
        "cost": ["cost", "tuition", "fees", "living expenses", "living costs", "budget", "affordable", "cheap", "low-cost", "total spend"],
        "placements": ["placement", "placements", "job prospects", "employment rate", "recruitment", "graduate salary", "internship", "career placement"],
        "experience": ["experience", "campus life", "student life", "lifestyle", "happiness", "enjoyment", "cuisine", "scenery", "memories", "hospitality"],
        "futureOpportunity": ["future opportunity", "future prospects", "career opportunity", "career mobility", "alumni network", "degree prestige", "global career"],
        "convenience": ["convenience", "convenient", "visa", "transit", "travel time", "easy access", "accessibility", "direct flight"],
        "attractions": ["attractions", "sightseeing", "landmarks", "excursions", "things to do", "scenic", "tourist sites", "activities"],
        "price": ["price", "pricing", "retail cost", "discount", "cheap", "affordable", "budget", "lowest price", "inexpensive"],
        "quality": ["quality", "material", "craftsmanship", "build quality", "finish", "reliable construction"],
        "features": ["features", "feature set", "functionality", "specifications", "adjustable", "versatility", "capabilities"],
        "reviews": ["reviews", "review", "ratings", "rating", "user feedback", "reputation", "owner feedback", "consensus"],
        "optionFit": ["strategic fit", "option fit", "goal alignment", "aligns with my goals", "core values", "best fit", "suits my needs"],
        "longTermImpact": ["long-term impact", "long term impact", "long-term", "long term", "five-year", "5-year", "sustainable outcome", "long-run"],
    }

    signals: Dict[str, float] = {}
    for factor in factors:
        hits = 0
        for keyword in factor_keywords.get(factor, []):
            if keyword in text:
                hits += 1
        if hits:
            signals[factor] = min(100.0, hits * 28.0)
    return signals


def infer_description_weights(description: str, factors: List[str]) -> Dict[str, float]:
    """Builds a default priority profile from the decision description when explicit weights are missing."""
    if not factors:
        return {}

    signals = infer_description_factor_signals(description, factors)
    weights = {factor: 1.0 + (signals.get(factor, 0.0) / 28.0 * 4.5) for factor in factors}

    total = sum(weights.values())
    return {factor: weights[factor] / total for factor in factors}


def parse_numeric_amount(value_str: Optional[str]) -> Optional[float]:
    """Extracts numeric digits from price or budget strings."""
    if not value_str:
        return None
    try:
        clean = "".join(ch for ch in str(value_str) if ch.isdigit() or ch == ".")
        if clean:
            return float(clean)
    except Exception:
        pass
    return None


def get_candidate_effective_price(cand: Dict[str, Any], is_usd_context: bool) -> float:
    """Returns the comparable price number in either USD or INR."""
    if is_usd_context:
        if "rawPriceUsd" in cand and cand["rawPriceUsd"]:
            return float(cand["rawPriceUsd"])
        return parse_numeric_amount(cand.get("price")) or 0.0
    else:
        if "rawPriceInr" in cand and cand["rawPriceInr"]:
            return float(cand["rawPriceInr"])
        usd = parse_numeric_amount(cand.get("price")) or 0.0
        return usd * 83.0 if usd < 10000 else usd


def audit_requirements_and_dealbreakers(
    candidate: Dict[str, Any],
    decision: DecisionInputSchema,
) -> Tuple[List[str], List[str], List[str]]:
    """
    Evaluates a candidate option against user must-have requirements and deal-breakers.
    Returns (requirements_passed, requirements_missed, deal_breakers_triggered).
    """
    passed: List[str] = []
    missed: List[str] = []
    triggered: List[str] = []

    cand_name = str(candidate.get("name", "")).lower()
    cand_desc = str(candidate.get("description", "")).lower()
    cand_brand = str(candidate.get("brand", "")).lower()
    cand_tags = [str(t).lower() for t in candidate.get("tags", [])]
    cand_strengths = [str(s).lower() for s in candidate.get("strengths", [])]
    cand_concerns = [str(c).lower() for c in candidate.get("concerns", [])]

    corpus = f"{cand_name} {cand_desc} {cand_brand} {' '.join(cand_tags)} {' '.join(cand_strengths)}"
    concerns_text = " ".join(cand_concerns)

    # Budget checking
    user_budget = parse_numeric_amount(decision.budget)
    is_usd = bool(decision.budget and ("$" in str(decision.budget) or (user_budget and user_budget <= 2500)))
    cand_price = get_candidate_effective_price(candidate, is_usd)

    if user_budget and cand_price > user_budget * 1.15:
        curr_symbol = "$" if is_usd else "₹"
        missed.append(f"Within budget target ({candidate.get('price')} vs {curr_symbol}{int(user_budget):,})")

    # Evaluate User Must-Have Requirements
    reqs = decision.requirements or []
    for req in reqs:
        req_clean = req.strip()
        req_lower = req_clean.lower()
        if not req_lower:
            continue

        if ("budget" in req_lower or "under" in req_lower) and user_budget:
            if cand_price <= user_budget * 1.15:
                passed.append(req_clean)
            else:
                if not any("Within budget" in m for m in missed):
                    curr_symbol = "$" if is_usd else "₹"
                    missed.append(f"{req_clean} (Exceeds {curr_symbol}{int(user_budget):,})")
            continue

        # Hardware & Feature checks
        if "camera" in req_lower or "photo" in req_lower:
            attrs = candidate.get("attributes", {})
            if attrs.get("camera", 70.0) >= 82.0 or any(k in corpus for k in ["camera", "pro", "plus", "sensor", "sony"]):
                passed.append(req_clean)
            else:
                missed.append(req_clean)
            continue

        if "battery" in req_lower or "charging" in req_lower:
            attrs = candidate.get("attributes", {})
            if attrs.get("battery", 70.0) >= 80.0 or any(k in corpus for k in ["battery", "mah", "all-day", "fast"]):
                passed.append(req_clean)
            else:
                missed.append(req_clean)
            continue

        if "16gb" in req_lower or "ram" in req_lower:
            if any(term in corpus for term in ["16gb", "32gb", "pro", "dual screen", "unified memory"]):
                passed.append(req_clean)
            elif "8gb" in corpus:
                missed.append(f"{req_clean} (Configured with 8GB RAM)")
            else:
                passed.append(req_clean)
            continue

        if "display" in req_lower or "screen" in req_lower:
            if any(term in corpus for term in ["display", "screen", "fhd", "ips", "amoled", "oled", "retina"]):
                passed.append(req_clean)
            else:
                missed.append(req_clean)
            continue

        # General keyword match
        ignore_words = {"the", "and", "for", "with", "good", "best", "minimum", "need", "under"}
        keywords = [
            w for w in req_lower.replace("-", " ").replace("/", " ").split()
            if len(w) > 2 and w not in ignore_words
        ]

        if not keywords:
            passed.append(req_clean)
            continue

        matched_count = sum(1 for kw in keywords if kw in corpus)
        if matched_count >= 1:
            passed.append(req_clean)
        else:
            attributes = candidate.get("attributes", {})
            factor_match = any(
                (f_key in req_lower or req_lower in f_key) and val >= 84.0
                for f_key, val in attributes.items()
            )
            if factor_match:
                passed.append(req_clean)
            else:
                missed.append(req_clean)

    if not reqs:
        tags = candidate.get("tags", [])
        if tags:
            passed = [f"Verified {tags[0]}", f"Optimized {tags[min(1, len(tags)-1)]}"]
        else:
            passed = ["Verified core product criteria"]

    # Evaluate User Deal-Breakers
    dbs = decision.dealBreakers or []
    for db in dbs:
        db_clean = db.strip()
        db_lower = db_clean.lower()
        if not db_lower:
            continue

        if "refurbished" in db_lower:
            if any(term in corpus for term in ["refurbished", "pre-owned", "used"]):
                triggered.append(f"{db_clean} (Refurbished hardware)")
                continue

        if "rating" in db_lower or "poor review" in db_lower:
            rating = float(candidate.get("rating", 4.0))
            if rating < 3.2:
                triggered.append(f"{db_clean} (Rating is {rating:.1f}/5.0)")
                continue

        if "16gb" in db_lower and ("less" in db_lower or "not" in db_lower or "minimum" in db_lower):
            if "8gb" in corpus and "16gb" not in corpus:
                triggered.append(f"{db_clean} (Has 8GB RAM)")
                continue

        if "thermal" in db_lower or "overheating" in db_lower:
            if any(term in concerns_text for term in ["overheating", "thermal throttle", "distinctly audible"]):
                triggered.append(f"{db_clean} (Audible fan resonance under max load)")
                continue

        if "slow charging" in db_lower or "slow charge" in db_lower:
            if "slower" in concerns_text or "18w" in concerns_text:
                triggered.append(f"{db_clean} (Slower charging speed)")
                continue

        if "bloatware" in db_lower or "ads" in db_lower:
            if any(term in concerns_text for term in ["promotional partner apps", "bloatware"]):
                triggered.append(f"{db_clean} (Pre-installed promotional partner apps)")
                continue

    return passed, missed, triggered


def filter_candidates(
    candidates: List[Dict[str, Any]],
    decision: DecisionInputSchema,
) -> Tuple[List[Dict[str, Any]], Optional[str]]:
    """
    Candidate Filtering Pipeline:
    1. Filter out options with severe deal-breaker violations.
    2. Apply budget filtering: Prefer candidates within target budget.
       - If candidates exist <= budget (+20% tolerance), filter to those candidates.
       - If no candidates exist within budget, check if budget is close enough to catalog minimum
         (e.g., budget >= min_price * 0.50). If so, keep pool candidates with budget stretch penalty.
       - If budget is far below catalog minimum (e.g. ₹5,000 for ₹91,000+ laptops), leave pool empty
         so status: 'no_matches' is returned cleanly.
    3. Returns valid candidates and optional notice.
    """
    user_budget = parse_numeric_amount(decision.budget)
    is_usd = bool(decision.budget and ("$" in str(decision.budget) or (user_budget and user_budget <= 2500)))

    # Step 1: Deal-breaker filter
    non_broken_candidates: List[Dict[str, Any]] = []
    for cand in candidates:
        _, _, triggered_dbs = audit_requirements_and_dealbreakers(cand, decision)
        if len(triggered_dbs) >= 2:
            continue
        non_broken_candidates.append(cand)

    if not non_broken_candidates:
        return [], "No candidates passed deal-breaker criteria."

    # Step 2: Budget filtering
    if not user_budget:
        return non_broken_candidates, None

    # Find candidates within budget + 20% tolerance
    budget_matched: List[Dict[str, Any]] = []
    prices: List[float] = []

    for cand in non_broken_candidates:
        price_num = get_candidate_effective_price(cand, is_usd)
        if price_num:
            prices.append(price_num)
            if price_num <= user_budget * 1.20:
                budget_matched.append(cand)
        else:
            # If price unavailable, do not blindly filter out
            budget_matched.append(cand)

    if budget_matched:
        # Prefer candidates <= budget target
        return budget_matched, None

    # If no candidate fits within budget, check if budget is a realistic near-miss or complete mismatch
    if prices:
        min_catalog_price = min(prices)
        if user_budget >= min_catalog_price * 0.50:
            # Plausible stretch (e.g. ₹60,000 vs ₹91,000): evaluate pool with scoring penalty
            return non_broken_candidates, f"Budget of {decision.budget} is below lowest catalog item ({min_catalog_price:.0f}). Showing nearest options."
        else:
            # Severe mismatch (e.g. ₹5,000 vs ₹91,000): return empty to trigger status: 'no_matches'
            return [], f"Budget of {decision.budget} is too low for available options (minimum is {min_catalog_price:.0f})."

    return non_broken_candidates, None



def calculate_decision_outcome(
    decision: DecisionInputSchema,
    agents: Optional[List[AgentResult]] = None,
) -> AnalysisResponseSchema:
    """
    Core Dynamic Decision Arena Engine:
    1. Detect Category & Subcategory.
    2. Load Configuration & Factors for this domain.
    3. Retrieve Candidate Pool from CandidateProvider (e.g. DummyJSON).
    4. Filter candidates by budget & deal-breakers (returning no_matches if none qualify).
    5. Evaluate EVERY candidate with specialized agents.
    6. Calculate weighted scores from attributes + user priorities.
    7. Rank all candidates descending.
    8. Return Top-N Results + Best Overall.
    """
    # 1. Detect Category and Subcategory
    category, subcategory = detect_category_and_subcategory(
        category=decision.category,
        subcategory=decision.subcategory,
        description=decision.description,
    )

    # 2. Load Configuration & Factors
    sub_config = get_decision_config(category, subcategory)
    factors = [f.key for f in sub_config.factors]

    # Resolve Priority Weights
    raw_priorities = decision.priorities or {}
    has_all_factors = all(k in raw_priorities for k in factors)

    if has_all_factors:
        weights = {k: float(raw_priorities[k]) for k in factors}
        supplied_total = sum(weights.values())
        if abs(supplied_total - 100.0) > 0.5:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"Priority weights must total exactly 100%. Current total: {supplied_total:.1f}%.",
            )
    else:
        # Use a balanced profile when the caller has not set every factor explicitly.
        share = round(100.0 / len(factors), 2) if factors else 20.0
        weights = {k: share for k in factors}

        diff = 100.0 - sum(weights.values())
        if factors:
            weights[factors[0]] += round(diff, 2)

    # Keep free-text intent active alongside priorities in every supported category.
    description_weights = infer_description_weights(decision.description, factors)
    if description_weights:
        adjusted = {
            factor: weights[factor] * (1.0 + description_weights.get(factor, 0.0) * 14.0)
            for factor in factors
        }
        adjusted_total = sum(adjusted.values())
        if adjusted_total:
            weights = {factor: (adjusted[factor] / adjusted_total) * 100.0 for factor in factors}

    total_weight = sum(weights.values())
    if abs(total_weight - 100.0) > 0.5:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Priority weights must total exactly 100%. Current total: {total_weight:.1f}%.",
        )

    # 3. Retrieve Candidate Pool from CandidateProvider
    try:
        provider = get_candidate_provider(category=category, subcategory=subcategory)
        raw_candidates = provider.get_candidates(
            category=category,
            subcategory=subcategory,
            decision=decision,
        )
    except UnsupportedSubcategoryError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except ExternalCatalogUnavailableError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"External candidate catalog temporarily unavailable: {str(e)}",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error discovering candidates from catalog: {str(e)}",
        )

    candidate_pool = raw_candidates[:decision.maxCandidates] if decision.maxCandidates and decision.maxCandidates > 0 else raw_candidates
    total_pool_count = len(candidate_pool)
    data_source = candidate_pool[0].get("source", "dummyjson") if candidate_pool else "dummyjson"

    # 4. Filter Candidates
    valid_candidates, budget_notice = filter_candidates(candidate_pool, decision)
    filtered_candidate_count = len(valid_candidates)

    # If filtering leaves zero candidates: return clear no_matches response without crashing!
    if not valid_candidates:
        user_budget = parse_numeric_amount(decision.budget)
        is_usd = bool(decision.budget and ("$" in str(decision.budget) or (user_budget and user_budget <= 2500)))
        curr_str = f"${int(user_budget):,}" if is_usd else f"₹{int(user_budget):,}"

        # Find lowest available price in catalog to give helpful suggestion
        prices = [get_candidate_effective_price(c, is_usd) for c in raw_candidates if get_candidate_effective_price(c, is_usd) > 0]
        min_price = min(prices) if prices else 0
        min_price_str = f"${int(min_price):,}" if is_usd else f"₹{int(min_price):,}"

        suggestions = [
            f"Increase your budget target to at least {min_price_str} to see available {subcategory} options.",
            "Remove strict deal-breakers or relax optional feature requirements.",
            f"Explore alternative categories or refurbished {subcategory} models.",
        ]

        factors_metadata = [
            {"key": f.key, "name": f.name, "description": f.description, "weight": weights.get(f.key, f.defaultWeight)}
            for f in sub_config.factors
        ]

        return AnalysisResponseSchema(
            status="no_matches",
            message=f"No {subcategory} options matched your budget target of {curr_str} or strict deal-breakers.",
            suggestions=suggestions,
            category=category,
            subcategory=subcategory,
            factors=factors_metadata,
            candidateCount=total_pool_count,
            filteredCandidateCount=0,
            topN=decision.topN or 5,
            rankedCandidates=[],
            bestOverall=None,
            rankings=[],
            agents=agents or [],
            dataSource=data_source,
            isDemoData=(data_source == "demo"),
            explanation=f"Evaluated {total_pool_count} candidates from the product catalog, but none satisfied the strict constraints.",
        )

    # 5. Specialized Agents selection
    specialized_agents = get_specialized_agents(category, subcategory)

    # 6. Agents evaluate only candidates that passed the filtering pipeline.
    evaluated_candidates: List[Dict[str, Any]] = []

    for cand in valid_candidates:
        cand_id = str(cand.get("id", ""))
        factor_scores: Dict[str, float] = {}
        agent_evaluations: List[CandidateEvaluationSchema] = []

        # Run each specialized agent on this candidate
        for agent in specialized_agents:
            eval_res = agent.evaluate(cand, decision)
            agent_evaluations.append(
                CandidateEvaluationSchema(
                    agent=eval_res.agent,
                    candidateId=eval_res.candidateId,
                    score=eval_res.score,
                    reason=eval_res.reason,
                )
            )
            factor_scores[agent.factor_key] = eval_res.score

        # 7. Weighted Scoring Calculation
        raw_score = sum(
            factor_scores.get(f, 75.0) * (weights.get(f, 20.0) / 100.0)
            for f in factors
        )

        passed_reqs, missed_reqs, triggered_dbs = audit_requirements_and_dealbreakers(cand, decision)
        penalty = (len(triggered_dbs) * 12.0) + (len(missed_reqs) * 3.5)
        user_budget = parse_numeric_amount(decision.budget)
        is_usd = bool(decision.budget and ("$" in str(decision.budget) or (user_budget and user_budget <= 2500)))
        candidate_price = get_candidate_effective_price(cand, is_usd)
        if user_budget and candidate_price > user_budget:
            budget_gap_ratio = (candidate_price - user_budget) / user_budget
            penalty += budget_gap_ratio * 20.0
        final_score = max(20.0, min(99.0, raw_score - penalty))
        final_score = round(final_score, 1)

        evaluated_candidates.append({
            "candidate": cand,
            "id": cand_id,
            "name": cand.get("name", ""),
            "brand": cand.get("brand", ""),
            "image": cand.get("image", ""),
            "thumbnail": cand.get("thumbnail", ""),
            "rating": cand.get("rating"),
            "price": cand.get("price", ""),
            "description": cand.get("description", ""),
            "category": cand.get("category", category),
            "subcategory": cand.get("subcategory", subcategory),
            "attributes": cand.get("attributes", {}),
            "factorScores": factor_scores,
            "agentEvaluations": agent_evaluations,
            "strengths": cand.get("strengths", []),
            "concerns": cand.get("concerns", []),
            "requirementsPassed": passed_reqs,
            "requirementsMissed": missed_reqs,
            "dealBreakersTriggered": triggered_dbs,
            "rawScore": round(raw_score, 1),
            "score": final_score,
            "source": cand.get("source", "dummyjson"),
        })

    # 8. Sort all candidates descending by final score
    evaluated_candidates.sort(key=lambda c: c["score"], reverse=True)

    # 9. Build Ranked Candidates
    ranked_candidates: List[RankedOptionSchema] = []
    scores_list = [c["score"] for c in evaluated_candidates]
    overall_confidence = calculate_confidence_heuristic(scores_list)

    for idx, cand_data in enumerate(evaluated_candidates):
        rank = idx + 1
        cand_name = cand_data["name"]
        final_score = cand_data["score"]

        if rank == 1:
            badge = "🥇 Best Overall"
        elif rank == 2:
            badge = "🥈 Runner-Up"
        elif rank == 3:
            badge = "🥉 Strong Contender"
        elif rank <= 5:
            badge = "Notable Contender"
        else:
            badge = f"Rank #{rank}"

        factor_scores = cand_data["factorScores"]
        best_factor_key = max(factor_scores.keys(), key=lambda k: factor_scores[k]) if factor_scores else "performance"
        best_factor_score = factor_scores.get(best_factor_key, 80.0)

        if rank == 1:
            why = (
                f"Ranked #1 Best Overall ({final_score:.1f}/100). "
                f"Leads strongly in {best_factor_key.title()} ({best_factor_score:.0f}/100), "
                f"aligning with your key priorities and requirements."
            )
        else:
            why = (
                f"Ranked #{rank} ({final_score:.1f}/100). "
                f"Solid in {best_factor_key.title()} ({best_factor_score:.0f}/100), "
                f"with minor trade-offs relative to the top choice."
            )

        ranked_candidates.append(
            RankedOptionSchema(
                rank=rank,
                id=cand_data["id"],
                name=cand_name,
                option=cand_name,
                brand=cand_data["brand"],
                image=cand_data["image"],
                thumbnail=cand_data["thumbnail"],
                rating=cand_data["rating"],
                candidate=cand_data["candidate"],
                score=final_score,
                overallScore=final_score,
                rawScore=cand_data["rawScore"],
                confidence=overall_confidence,
                why=why,
                price=cand_data["price"],
                description=cand_data["description"],
                category=cand_data["category"],
                subcategory=cand_data["subcategory"],
                attributes=cand_data["attributes"],
                factorScores=factor_scores,
                agentEvaluations=cand_data["agentEvaluations"],
                strengths=cand_data["strengths"],
                concerns=cand_data["concerns"],
                requirementsPassed=cand_data["requirementsPassed"],
                requirementsMissed=cand_data["requirementsMissed"],
                dealBreakersTriggered=cand_data["dealBreakersTriggered"],
                badge=badge,
                source=cand_data["source"],
            )
        )

    # 10. Best Overall
    best_overall = ranked_candidates[0] if ranked_candidates else None

    # Configured top-N candidates for prominent display
    top_n = min(decision.topN or 5, len(ranked_candidates)) if ranked_candidates else 0

    # Comparison Matrix
    factor_definitions = [
        {"key": f.key, "name": f.name}
        for f in sub_config.factors
    ]
    comparison_options = []
    for r in ranked_candidates[:max(top_n, 5)]:
        row: Dict[str, Any] = {
            "id": r.id,
            "name": r.name,
            "rank": r.rank,
            "score": r.score,
            "price": r.price,
            "badge": r.badge,
        }
        for f in factors:
            row[f] = r.factorScores.get(f, 80.0)
        comparison_options.append(row)

    comparison_matrix = ComparisonMatrixSchema(
        factors=factor_definitions,
        options=comparison_options,
    )

    # Decision Engine summary
    decision_engine_result = DecisionEngineResultSchema(
        overallScore=best_overall.score if best_overall else 0.0,
        recommendation=best_overall.name if best_overall else "No candidate options available",
        confidence=overall_confidence,
        totalOptionsEvaluated=filtered_candidate_count,
    )

    explanation = (
        f"Evaluated {filtered_candidate_count} candidates across {len(factors)} specialized dimensions for "
        f"{category.title()} ({subcategory.title()}). "
        f"{best_overall.name if best_overall else 'No option'} earned the top recommendation "
        f"with an overall score of {best_overall.score if best_overall else 0.0:.1f}."
    )

    factors_metadata = [
        {
            "key": f.key,
            "name": f.name,
            "description": f.description,
            "weight": weights.get(f.key, f.defaultWeight),
        }
        for f in sub_config.factors
    ]

    return AnalysisResponseSchema(
        status="success",
        category=category,
        subcategory=subcategory,
        factors=factors_metadata,
        candidateCount=total_pool_count,
        filteredCandidateCount=filtered_candidate_count,
        topN=top_n,
        rankedCandidates=ranked_candidates,
        bestOverall=best_overall,
        explanation=explanation,
        fallbackNotice=budget_notice,
        agents=agents or [],
        rankings=ranked_candidates,
        comparison=comparison_matrix,
        decision=decision_engine_result,
        decisionEngine=decision_engine_result,
        dataSource=data_source,
        isDemoData=(data_source == "demo"),
    )
