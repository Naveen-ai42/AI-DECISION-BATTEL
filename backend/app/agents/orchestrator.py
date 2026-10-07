from typing import List, Optional
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from ..services.ai_provider import AIProvider, get_ai_provider
from .factory import get_agents_for_category

class DecisionOrchestrator:
    """
    Category-Aware Decision Orchestrator:
    Instantiates and executes the 5 specialized autonomous agents dynamically
    selected based on the decision category.
    Guarantees all 5 category-calibrated agents execute and produce structured evaluations.
    """

    def __init__(self, provider: Optional[AIProvider] = None):
        self.provider = provider or get_ai_provider()

    def run_all(self, decision: DecisionInputSchema) -> List[AgentResult]:
        """
        Dynamically retrieves the 5 agents for decision.category,
        executes their evaluations deterministically, and returns the AgentResults.
        """
        sub = decision.subcategory
        desc_lower = (decision.description or "").lower()
        if not sub and decision.category == "electronics":
            if "watch" in desc_lower:
                sub = "smartwatch"
            elif "phone" in desc_lower or "mobile" in desc_lower:
                sub = "smartphone"
            elif "laptop" in desc_lower or "notebook" in desc_lower or "macbook" in desc_lower:
                sub = "laptop"
        if sub and decision.subcategory != sub:
            decision.subcategory = sub

        agents = get_agents_for_category(decision.category, subcategory=sub, provider=self.provider)
        results: List[AgentResult] = []

        for agent in agents:
            res = agent.analyze(decision)
            results.append(res)

        return results
