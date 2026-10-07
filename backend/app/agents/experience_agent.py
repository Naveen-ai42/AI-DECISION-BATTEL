from typing import Optional
from .base_agent import BaseAgent
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from ..services.ai_provider import AIProvider

class ExperienceAgent(BaseAgent):
    """
    Experience Agent:
    Specializes in ergonomic comfort, sensory factors (display, keyboard, acoustics),
    chassis build rigidity, daily usability, and qualitative satisfaction.
    """

    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="experience",
            name="Experience Agent",
            specialization="Display, build quality, usability, comfort and satisfaction",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        """
        Executes user experience evaluation using swappable AIProvider backend.
        Returns concise structured metrics without internal reasoning traces.
        """
        return self.provider.evaluate_dimension(
            agent_id=self.id,
            agent_name=self.name,
            specialization=self.specialization,
            decision=decision,
        )
