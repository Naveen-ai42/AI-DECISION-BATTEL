"""
Specialized Generic and Fallback Candidate Evaluation Agents for Decision Arena.
"""

from typing import Dict, Any, Optional
from ..base_agent import BaseCandidateAgent, CandidateEvaluation
from ...schemas.decision import DecisionInputSchema

class GenericFactorAgent(BaseCandidateAgent):
    """
    Fallback agent that can evaluate any arbitrary factor key gracefully.
    """
    def __init__(self, agent_name: str, factor_key: str):
        super().__init__(agent_name=agent_name, factor_key=factor_key)

    def evaluate(
        self,
        candidate: Dict[str, Any],
        decision: Optional[DecisionInputSchema] = None,
    ) -> CandidateEvaluation:
        attrs = candidate.get("attributes", {})
        cand_name = candidate.get("name", "Candidate")
        score = float(attrs.get(self.factor_key, 85.0))

        strengths = candidate.get("strengths", [])
        matched_strength = next(
            (s for s in strengths if self.factor_key.lower() in str(s).lower()),
            None
        )

        if matched_strength:
            reason = f"{cand_name}: {matched_strength}"
        elif score >= 90.0:
            reason = f"{cand_name}: Outstanding {self.agent_name.lower()} rating ({score:.0f}/100)."
        elif score >= 80.0:
            reason = f"{cand_name}: Solid {self.agent_name.lower()} performance ({score:.0f}/100)."
        else:
            reason = f"{cand_name}: Moderate {self.agent_name.lower()} score ({score:.0f}/100) with minor trade-offs."

        return CandidateEvaluation(
            agent=self.agent_name,
            candidateId=str(candidate.get("id", "")),
            score=score,
            reason=reason,
        )
