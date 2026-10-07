from typing import Optional
from .base_agent import BaseAgent
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from ..services.ai_provider import AIProvider

class PerformanceAgent(BaseAgent):
    """
    Performance Agent:
    Specializes in compute horsepower, throughput, processing bottlenecks,
    hardware resources (CPU, GPU, RAM), multitasking, and technical workload execution.
    """

    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="performance",
            name="Performance Agent",
            specialization="CPU, GPU, RAM, workload and raw compute capability",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        """
        Executes performance evaluation using swappable AIProvider backend.
        Returns concise structured metrics without internal reasoning traces.
        """
        return self.provider.evaluate_dimension(
            agent_id=self.id,
            agent_name=self.name,
            specialization=self.specialization,
            decision=decision,
        )
