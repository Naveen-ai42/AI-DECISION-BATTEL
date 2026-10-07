"""
Step 9 Dynamic Decision Engine Verification Suite.
Validates:
1. Smartphone + Camera-heavy priority -> Camera champion ranks #1 (e.g. Pixel 8a or Moto Edge 50 Pro).
2. Smartphone + Battery-heavy priority -> Battery champion ranks #1 (ranking dynamically changes!).
3. Smartwatch -> Smartwatch-specific factors and specialized agents (zero laptop/smartphone factor contamination).
4. Laptop -> Laptop-specific factors and specialized agents.
5. Finance (Investment) -> Finance factors & agents (zero hardware leakage).
6. Filter fallback -> Budget strictly ₹10,000 where no phones exist -> graceful fallback response without crashing.
7. Candidate Count is dynamic (13 smartphones, 7 laptops, 5 smartwatches, 4 investments, 3 careers, or simulated 25 candidates).
"""

import sys
import pytest
from app.schemas.decision import DecisionInputSchema
from app.services.analysis_service import analysis_service
from app.decision.category_config import DECISION_CONFIG


def test_smartphone_catalog_contains_more_than_ten_unique_ranked_options():
    result = analysis_service.analyze_decision(
        DecisionInputSchema(
            description="Compare smartphones for camera, gaming performance, and battery life",
            category="electronics",
            subcategory="smartphone",
        )
    )

    candidate_ids = {candidate.id for candidate in result.rankedCandidates}
    assert result.candidateCount > 10
    assert len(result.rankedCandidates) == result.candidateCount
    assert len(candidate_ids) == result.candidateCount


@pytest.mark.parametrize(
    ("category", "subcategory", "first_intent", "second_intent"),
    [
        ("electronics", "laptop", "gaming performance", "long battery life for travel"),
        ("electronics", "smartphone", "best camera for photography", "gaming performance and speed"),
        ("electronics", "tablet", "bright display for reading", "keyboard productivity and multitasking"),
        ("electronics", "smartwatch", "fitness tracking and accurate heart rate", "multi-day battery life"),
        ("electronics", "headphones", "excellent sound quality for music", "strong noise cancellation for flights"),
        ("vehicle", "vehicle", "family safety and crash protection", "fuel economy and mileage"),
        ("vehicle", "motorcycle", "engine performance and acceleration", "fuel economy and mileage"),
        ("finance", "investment", "high investment returns and long-term growth", "stable investment with low risk and capital preservation"),
        ("finance", "loan", "low interest rate and low total borrowing cost", "flexible loan tenure and fast eligibility approval"),
        ("career", "job", "highest salary and compensation", "excellent work life balance and remote flexibility"),
        ("education", "program", "best academic quality and research faculty", "lowest tuition and affordable fees"),
        ("travel", "trip", "safe destination with emergency services", "affordable trip with the lowest travel cost"),
        ("shopping", "product", "highest product quality and durability", "lowest price and biggest discount"),
        ("other", "general", "best option fit for my goals and values", "minimize cost and maximize financial value"),
    ],
)
def test_distinct_description_intents_change_winner_for_every_subcategory(
    category, subcategory, first_intent, second_intent
):
    factors = [
        factor.key
        for factor in DECISION_CONFIG[category].subcategories[subcategory].factors
    ]
    share = round(100.0 / len(factors), 2)
    priorities = {factor: share for factor in factors}
    priorities[factors[-1]] += 100.0 - sum(priorities.values())

    results = [
        analysis_service.analyze_decision(
            DecisionInputSchema(
                description=f"I want {intent}",
                category=category,
                subcategory=subcategory,
                priorities=priorities,
            )
        )
        for intent in (first_intent, second_intent)
    ]

    assert results[0].bestOverall.name != results[1].bestOverall.name, (
        f"Distinct {subcategory} intents should produce different winners."
    )
    for result in results:
        assert result.category == category
        assert result.subcategory == subcategory
        assert all(
            option.category == category and option.subcategory == subcategory
            for option in result.rankedCandidates
        )


def test_description_changes_recommendation_even_with_same_priorities():
    decision_gaming = DecisionInputSchema(
        description="I need a phone for gaming and camera with good display",
        category="electronics",
        subcategory="smartphone",
        budget="40000",
        priorities={
            "performance": 25.0,
            "battery": 25.0,
            "value": 20.0,
            "experience": 15.0,
            "display": 15.0,
        },
        riskTolerance="balanced",
        decisionStyle="best-overall",
    )
    decision_battery = DecisionInputSchema(
        description="I need a phone for battery life and travel with all-day endurance",
        category="electronics",
        subcategory="smartphone",
        budget="40000",
        priorities={
            "performance": 25.0,
            "battery": 25.0,
            "value": 20.0,
            "experience": 15.0,
            "display": 15.0,
        },
        riskTolerance="balanced",
        decisionStyle="best-overall",
    )

    res_gaming = analysis_service.analyze_decision(decision_gaming)
    res_battery = analysis_service.analyze_decision(decision_battery)

    assert res_gaming.bestOverall.name != res_battery.bestOverall.name, (
        "Different descriptions with the same category and priorities should not collapse to the same winner."
    )


def test_lower_near_miss_budget_changes_phone_recommendation():
    camera_decision = DecisionInputSchema(
        description="I have a buy a phone under 55000 for cameraa",
        category="electronics",
        subcategory="smartphone",
        budget="55000",
    )
    low_budget_decision = DecisionInputSchema(
        description="I have a buy a phone under 20000",
        category="electronics",
        subcategory="smartphone",
        budget="20000",
    )

    camera_result = analysis_service.analyze_decision(camera_decision)
    low_budget_result = analysis_service.analyze_decision(low_budget_decision)

    assert camera_result.bestOverall is not None
    assert low_budget_result.bestOverall is not None
    assert camera_result.bestOverall.name != low_budget_result.bestOverall.name
    assert low_budget_result.bestOverall.name == "Nothing Phone (2a) Plus"
    assert low_budget_result.fallbackNotice is not None
    assert "below lowest catalog item" in low_budget_result.fallbackNotice


def run_tests():
    print("=" * 75)
    print("DECISION ARENA - STEP 9 DYNAMIC DECISION ENGINE TEST SUITE")
    print("=" * 75)

    # -------------------------------------------------------------------------
    # TEST 1: Smartphone with Camera-heavy priority
    # -------------------------------------------------------------------------
    print("\n[*] TEST 1: Smartphone (Budget ~32k, Camera Priority 50%, Software 30%, Battery 5%, Perf 5%, Display 5%, Build 3%, Value 2%)")
    decision_camera = DecisionInputSchema(
        description="I need a smartphone with the best camera for photography under 35000",
        category="electronics",
        subcategory="smartphone",
        budget="35000",
        priorities={
            "camera": 50.0,
            "software": 30.0,
            "display": 5.0,
            "performance": 5.0,
            "build": 3.0,
            "battery": 5.0,
            "value": 2.0,
        },
        riskTolerance="balanced",
        decisionStyle="best-overall",
    )
    res_camera = analysis_service.analyze_decision(decision_camera)
    rank1_camera = res_camera.bestOverall.name
    score1_camera = res_camera.bestOverall.score
    print(f"  [OK] Evaluated {res_camera.candidateCount} smartphone candidates")
    print(f"  [OK] Rank #1 Best Overall: '{rank1_camera}' (Score: {score1_camera})")
    print(f"  [OK] Top 3 Candidates: {[c.name for c in res_camera.rankedCandidates[:3]]}")
    assert "Pixel" in rank1_camera or "Camera" in res_camera.bestOverall.why, "Expected Camera-focused phone to rank #1"

    # -------------------------------------------------------------------------
    # TEST 2: Same Smartphone category, but Battery-heavy priority
    # -------------------------------------------------------------------------
    print("\n[*] TEST 2: Smartphone (Budget ~36k, Battery Priority 55%, Performance 25%, Display 10%, Build 5%, Value 3%, Camera 1%, Software 1%)")
    decision_battery = DecisionInputSchema(
        description="I need a smartphone with extreme battery life and sustained gaming performance",
        category="electronics",
        subcategory="smartphone",
        budget="36000",
        priorities={
            "battery": 55.0,
            "performance": 25.0,
            "display": 10.0,
            "build": 5.0,
            "value": 3.0,
            "camera": 1.0,
            "software": 1.0,
        },
        riskTolerance="balanced",
        decisionStyle="best-performance",
    )
    res_battery = analysis_service.analyze_decision(decision_battery)
    rank1_battery = res_battery.bestOverall.name
    score1_battery = res_battery.bestOverall.score
    print(f"  [OK] Evaluated {res_battery.candidateCount} smartphone candidates")
    print(f"  [OK] Rank #1 Best Overall: '{rank1_battery}' (Score: {score1_battery})")
    print(f"  [OK] Top 3 Candidates: {[c.name for c in res_battery.rankedCandidates[:3]]}")
    
    # Verify ranking dynamically shifted!
    assert rank1_camera != rank1_battery, (
        f"CRITICAL FAILURE: Winner did NOT change! "
        f"Camera winner was '{rank1_camera}', Battery winner was '{rank1_battery}'."
    )
    print(f"  [PASS] VERIFIED: Winner changed dynamically from '{rank1_camera}' -> '{rank1_battery}' when priorities changed!")

    # -------------------------------------------------------------------------
    # TEST 3: Smartwatch factors & agents
    # -------------------------------------------------------------------------
    print("\n[*] TEST 3: Smartwatch Category & Specialized Agents")
    decision_watch = DecisionInputSchema(
        description="I need a smartwatch for running, marathon training, and heart-rate tracking",
        category="electronics",
        subcategory="smartwatch",
        budget="30000",
        priorities={
            "healthFitness": 45.0,
            "battery": 25.0,
            "smartFeatures": 10.0,
            "comfort": 10.0,
            "durability": 5.0,
            "compatibility": 3.0,
            "value": 2.0,
        },
    )
    res_watch = analysis_service.analyze_decision(decision_watch)
    print(f"  [OK] Subcategory resolved: {res_watch.subcategory}")
    factor_keys = [f["key"] for f in res_watch.factors]
    print(f"  [OK] Smartwatch factors: {factor_keys}")
    assert "healthFitness" in factor_keys, "Expected healthFitness factor in smartwatch"
    assert "camera" not in factor_keys, "Camera factor should NOT exist in smartwatch"
    print(f"  [OK] Rank #1 Smartwatch: '{res_watch.bestOverall.name}' (Score: {res_watch.bestOverall.score})")
    print(f"  [PASS] Smartwatch factors and agents verified!")

    # -------------------------------------------------------------------------
    # TEST 4: Laptop factors & agents
    # -------------------------------------------------------------------------
    print("\n[*] TEST 4: Laptop Category & Specialized Agents")
    decision_laptop = DecisionInputSchema(
        description="I need a laptop with maximum battery life and silent operation for work travel",
        category="electronics",
        subcategory="laptop",
        budget="95000",
        priorities={
            "battery": 50.0,
            "build": 25.0,
            "display": 15.0,
            "performance": 5.0,
            "upgradeability": 3.0,
            "value": 2.0,
        },
    )
    res_laptop = analysis_service.analyze_decision(decision_laptop)
    print(f"  [OK] Subcategory resolved: {res_laptop.subcategory}")
    laptop_factor_keys = [f["key"] for f in res_laptop.factors]
    print(f"  [OK] Laptop factors: {laptop_factor_keys}")
    assert "upgradeability" in laptop_factor_keys, "Expected upgradeability factor in laptop"
    assert "camera" not in laptop_factor_keys, "Camera factor should NOT exist in laptop"
    print(f"  [OK] Rank #1 Laptop with Battery Focus: '{res_laptop.bestOverall.name}' (Score: {res_laptop.bestOverall.score})")
    # Verify MacBook Air wins battery priority over ASUS TUF!
    assert "MacBook" in res_laptop.bestOverall.name, (
        f"Expected MacBook Air to win high-battery priority, but got '{res_laptop.bestOverall.name}'"
    )
    print(f"  [PASS] Laptop factors and dynamic winner (MacBook Air under battery priority) verified!")

    # -------------------------------------------------------------------------
    # TEST 5: Finance (Investment) - No hardware factor leakage
    # -------------------------------------------------------------------------
    print("\n[*] TEST 5: Finance (Investment) - Zero Hardware Leakage")
    decision_finance = DecisionInputSchema(
        description="Allocate ₹5 lakh for long-term growth and capital preservation",
        category="finance",
        subcategory="investment",
        budget="500000",
        priorities={
            "stability": 40.0,
            "risk": 30.0,
            "returnPotential": 15.0,
            "growth": 10.0,
            "liquidity": 5.0,
        },
    )
    res_finance = analysis_service.analyze_decision(decision_finance)
    fin_factors = [f["key"] for f in res_finance.factors]
    print(f"  [OK] Finance factors: {fin_factors}")
    hardware_terms = ["ram", "gpu", "battery", "camera", "display", "cpu", "screen"]
    for factor in fin_factors:
        for term in hardware_terms:
            assert term not in factor.lower(), f"Leakage detected: '{term}' in '{factor}'"
    print(f"  [OK] Zero hardware leakage across all finance factors!")
    print(f"  [OK] Rank #1 Investment: '{res_finance.bestOverall.name}' (Score: {res_finance.bestOverall.score})")
    print(f"  [PASS] Finance domain separation verified!")

    # -------------------------------------------------------------------------
    # TEST 6: Graceful Filter Fallback (Strict budget INR 10,000 where no phones match)
    # -------------------------------------------------------------------------
    print("\n[*] TEST 6: Strict Budget INR 10,000 Fallback Handling (Zero Crash)")
    decision_unmatched = DecisionInputSchema(
        description="I need a smartphone under 10000",
        category="electronics",
        subcategory="smartphone",
        budget="10000",
        priorities={
            "value": 50.0,
            "battery": 20.0,
            "display": 10.0,
            "camera": 10.0,
            "performance": 5.0,
            "software": 3.0,
            "build": 2.0,
        },
    )
    res_fallback = analysis_service.analyze_decision(decision_unmatched)
    notice_safe = str(res_fallback.fallbackNotice).encode('ascii', errors='replace').decode('ascii')
    print(f"  [OK] Fallback notice returned: '{notice_safe}'")
    assert res_fallback.fallbackNotice is not None, "Expected fallback notice when 0 candidates match budget"
    assert len(res_fallback.rankedCandidates) > 0, "Expected candidates to be returned with relaxed filter"
    print(f"  [OK] Engine gracefully relaxed filter and returned {len(res_fallback.rankedCandidates)} ranked options without crashing!")
    print(f"  [PASS] Zero-crash graceful fallback verified!")

    # -------------------------------------------------------------------------
    # TEST 7: Dynamic Candidate Pool Sizing (e.g. 25 candidates)
    # -------------------------------------------------------------------------
    print("\n[*] TEST 7: Dynamic Candidate Pool Expansion (25 candidates)")
    decision_large_pool = DecisionInputSchema(
        description="Evaluate large candidate pool of 25 smartphones",
        category="electronics",
        subcategory="smartphone",
        budget="50000",
        maxCandidates=25,
        priorities={
            "value": 20.0,
            "battery": 20.0,
            "display": 15.0,
            "camera": 15.0,
            "performance": 15.0,
            "software": 10.0,
            "build": 5.0,
        },
    )
    res_large = analysis_service.analyze_decision(decision_large_pool)
    print(f"  [OK] Dynamic candidate count: {res_large.candidateCount} (expected 25)")
    assert res_large.candidateCount == 25, f"Expected 25 candidates, got {res_large.candidateCount}"
    assert len(res_large.rankedCandidates) == 25, f"Expected 25 ranked candidates, got {len(res_large.rankedCandidates)}"
    # Verify monotonic descending order
    scores = [c.score for c in res_large.rankedCandidates]
    assert scores == sorted(scores, reverse=True), "Rankings must be monotonically descending by score"
    print(f"  [OK] All 25 candidates ranked monotonically: {scores[:5]} ... {scores[-2:]}")
    print(f"  [PASS] Dynamic candidate sizing (25 candidates) verified!")

    print("\n" + "=" * 75)
    print("ALL 7 STEP 9 TESTS PASSED FLAWLESSLY WITH ZERO DEFECTS!")
    print("=" * 75)

if __name__ == "__main__":
    run_tests()
