from typing import List
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from .base_agent import BaseAgent
from .performance_agent import PerformanceAgent
from .value_agent import ValueAgent
from .battery_agent import BatteryAgent
from .experience_agent import ExperienceAgent
from .future_agent import FutureAgent
from .orchestrator import DecisionOrchestrator

def evaluate_decision_with_agents(decision: DecisionInputSchema) -> List[AgentResult]:
    """
    Compatibility wrapper delegating directly to DecisionOrchestrator.
    """
    orchestrator = DecisionOrchestrator()
    return orchestrator.run_all(decision)

__all__ = [
    "BaseAgent",
    "PerformanceAgent",
    "ValueAgent",
    "BatteryAgent",
    "ExperienceAgent",
    "FutureAgent",
    "DecisionOrchestrator",
    "evaluate_decision_with_agents",
]
