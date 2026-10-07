"""
Specialized Career Candidate Evaluation Agents for Decision Arena.
Evaluates job offers and career trajectories with zero electronics leakage.
"""

from typing import Dict, Any, Optional
from ..base_agent import BaseCandidateAgent, CandidateEvaluation
from ...schemas.decision import DecisionInputSchema

def _extract_career_reason(
    candidate: Dict[str, Any],
    factor_key: str,
    factor_label: str,
    keywords: list[str],
    score: float,
) -> str:
    strengths = candidate.get("strengths", [])
    concerns = candidate.get("concerns", [])
    cand_name = candidate.get("name", "Role")

    if score < 82.0:
        for c in concerns:
            c_low = str(c).lower()
            if any(k in c_low for k in keywords):
                return f"{cand_name}: {c}"

    for s in strengths:
        s_low = str(s).lower()
        if any(k in s_low for k in keywords):
            return f"{cand_name}: {s}"

    if score >= 94.0:
        return f"{cand_name}: Superior {factor_label.lower()} ({score:.0f}/100) providing significant career advantage."
    elif score >= 88.0:
        return f"{cand_name}: Competitive {factor_label.lower()} ({score:.0f}/100) meeting target benchmarks."
    elif score >= 80.0:
        return f"{cand_name}: Moderate {factor_label.lower()} ({score:.0f}/100) with typical industry trade-offs."
    else:
        return f"{cand_name}: Lower {factor_label.lower()} ({score:.0f}/100) requiring personal mitigation."


class CareerFactorAgent(BaseCandidateAgent):
    def __init__(self, agent_name: str, factor_key: str, keywords: list[str]):
        super().__init__(agent_name=agent_name, factor_key=factor_key)
        self.keywords = keywords

    def evaluate(
        self,
        candidate: Dict[str, Any],
        decision: Optional[DecisionInputSchema] = None,
    ) -> CandidateEvaluation:
        attrs = candidate.get("attributes", {})
        score = float(attrs.get(self.factor_key, 80.0))
        reason = _extract_career_reason(
            candidate=candidate,
            factor_key=self.factor_key,
            factor_label=self.agent_name,
            keywords=self.keywords,
            score=score,
        )
        return CandidateEvaluation(
            agent=self.agent_name,
            candidateId=str(candidate.get("id", "")),
            score=score,
            reason=reason,
        )


class SalaryAgent(CareerFactorAgent):
    def __init__(self):
        super().__init__("Compensation", "salary", ["salary", "compensation", "lpa", "equity", "stock", "bonus", "base pay"])

class SkillFitAgent(CareerFactorAgent):
    def __init__(self):
        super().__init__("Skill Fit", "skillFit", ["skill", "tech stack", "relevance", "expertise", "autonomy", "stack"])

class CareerGrowthAgent(CareerFactorAgent):
    def __init__(self):
        super().__init__("Career Growth", "growth", ["growth", "promotion", "leadership", "runway", "mentorship", "headroom"])

class WorkLifeBalanceAgent(CareerFactorAgent):
    def __init__(self):
        super().__init__("Work-Life Balance", "workLifeBalance", ["work-life", "hours", "sprint", "crunch", "pto", "hybrid", "remote"])

class CareerStabilityAgent(CareerFactorAgent):
    def __init__(self):
        super().__init__("Company Stability", "stability", ["stability", "security", "runway", "revenue", "fortune 500", "backing"])

class LocationAgent(CareerFactorAgent):
    def __init__(self):
        super().__init__("Location", "location", ["location", "commute", "city", "remote", "onsite", "relocation"])

class LearningAgent(CareerFactorAgent):
    def __init__(self):
        super().__init__("Learning Curve", "learning", ["learning", "exposure", "frontier", "cutting-edge", "curve", "mentorship"])
