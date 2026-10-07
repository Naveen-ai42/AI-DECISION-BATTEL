from typing import Optional
from .base_agent import BaseAgent
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from ..services.ai_provider import AIProvider

class FutureAgent(BaseAgent):
    """
    Future Agent:
    Specializes in obsolescence mitigation, future workload headroom,
    component upgradeability (RAM, SSD, I/O), driver roadmaps, and multi-year longevity.
    """

    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="future",
            name="Future Agent",
            specialization="Longevity, upgrades, future workload and long-term viability",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        """
        Executes future-readiness evaluation using swappable AIProvider backend.
        Returns concise structured metrics without internal reasoning traces.
        """
        return self.provider.evaluate_dimension(
            agent_id=self.id,
            agent_name=self.name,
            specialization=self.specialization,
            decision=decision,
        )
