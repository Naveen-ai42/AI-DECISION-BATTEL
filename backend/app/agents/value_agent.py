from typing import Optional
from .base_agent import BaseAgent
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from ..services.ai_provider import AIProvider

class ValueAgent(BaseAgent):
    """
    Value Agent:
    Specializes in cost-benefit analysis, budget alignment, feature-to-price ratios,
    depreciation, and total economic return on investment.
    """

    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="value",
            name="Value Agent",
            specialization="Price, features, ROI and budget fit",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        """
        Executes value evaluation using swappable AIProvider backend.
        Returns concise structured metrics without internal reasoning traces.
        """
        return self.provider.evaluate_dimension(
            agent_id=self.id,
            agent_name=self.name,
            specialization=self.specialization,
            decision=decision,
        )
