"""
Specialized Vehicle Candidate Evaluation Agents for Decision Arena.
Evaluates passenger vehicles, cars, and motorcycles strictly along automotive dimensions.
"""

from typing import Dict, Any, Optional
from ..base_agent import BaseCandidateAgent, CandidateEvaluation
from ...schemas.decision import DecisionInputSchema

def _extract_vehicle_reason(
    candidate: Dict[str, Any],
    factor_key: str,
    factor_label: str,
    keywords: list[str],
    score: float,
) -> str:
    strengths = candidate.get("strengths", [])
    concerns = candidate.get("concerns", [])
    cand_name = candidate.get("name", "Vehicle")

    if score < 80.0:
        for c in concerns:
            c_low = str(c).lower()
            if any(k in c_low for k in keywords):
                return f"{cand_name}: {c}"

    for s in strengths:
        s_low = str(s).lower()
        if any(k in s_low for k in keywords):
            return f"{cand_name}: {s}"

    if score >= 92.0:
        return f"{cand_name}: Leading {factor_label.lower()} profile ({score:.0f}/100) exceeding automotive class benchmarks."
    elif score >= 85.0:
        return f"{cand_name}: Solid {factor_label.lower()} capability ({score:.0f}/100) well-calibrated for daily commuting."
    elif score >= 75.0:
        return f"{cand_name}: Moderate {factor_label.lower()} score ({score:.0f}/100) reflecting category trade-offs."
    else:
        return f"{cand_name}: Lower {factor_label.lower()} rating ({score:.0f}/100) requiring user compromise."


class VehicleFactorAgent(BaseCandidateAgent):
    def __init__(self, agent_name: str, factor_key: str, keywords: list[str]):
        super().__init__(agent_name=agent_name, factor_key=factor_key)
        self.keywords = keywords

    def evaluate(
        self,
        candidate: Dict[str, Any],
        decision: Optional[DecisionInputSchema] = None,
    ) -> CandidateEvaluation:
        attrs = candidate.get("attributes", {})
        score = float(attrs.get(self.factor_key, 78.0))
        reason = _extract_vehicle_reason(
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


class VehicleSafetyAgent(VehicleFactorAgent):
    def __init__(self):
        super().__init__("Safety", "safety", ["safety", "airbag", "adas", "braking", "crash", "pacifica", "durango"])

class VehicleMileageAgent(VehicleFactorAgent):
    def __init__(self):
        super().__init__("Mileage", "mileage", ["mileage", "fuel", "mpg", "hybrid", "economy", "efficiency"])

class VehicleComfortAgent(VehicleFactorAgent):
    def __init__(self):
        super().__init__("Comfort", "comfort", ["comfort", "cabin", "seating", "suspension", "quiet", "pacifica", "touring"])

class VehicleSpaceAgent(VehicleFactorAgent):
    def __init__(self):
        super().__init__("Space", "space", ["space", "cargo", "trunk", "legroom", "folding", "minivan", "suv"])

class VehiclePerformanceAgent(VehicleFactorAgent):
    def __init__(self):
        super().__init__("Performance", "performance", ["performance", "horsepower", "torque", "rwd", "charger", "hornet", "engine"])

class VehicleMaintenanceAgent(VehicleFactorAgent):
    def __init__(self):
        super().__init__("Maintenance", "maintenance", ["maintenance", "reliability", "service", "warranty", "parts"])

class VehicleValueAgent(VehicleFactorAgent):
    def __init__(self):
        super().__init__("Value", "value", ["value", "price", "cost", "resale", "discount"])
