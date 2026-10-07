"""
Compatibility module redirecting to orchestrator.DecisionOrchestrator.
"""
from typing import List
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from .orchestrator import DecisionOrchestrator

def evaluate_decision_with_agents(decision: DecisionInputSchema) -> List[AgentResult]:
    """Delegates to DecisionOrchestrator."""
    return DecisionOrchestrator().run_all(decision)
