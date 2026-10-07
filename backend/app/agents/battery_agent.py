from typing import Optional
from .base_agent import BaseAgent
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from ..services.ai_provider import AIProvider

class BatteryAgent(BaseAgent):
    """
    Battery Agent:
    Specializes in energy endurance, power efficiency curves, portability,
    thermal throttle impact, and operational sustainability.
    """

    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="battery",
            name="Battery Agent",
            specialization="Battery life, endurance, efficiency and sustainability",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        """
        Executes endurance evaluation using swappable AIProvider backend.
        Returns concise structured metrics without internal reasoning traces.
        """
        return self.provider.evaluate_dimension(
            agent_id=self.id,
            agent_name=self.name,
            specialization=self.specialization,
            decision=decision,
        )
