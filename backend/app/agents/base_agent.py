"""
Base Agent Module for Decision Arena.
Defines foundational abstractions for:
1. Candidate-level specialized evaluation agents (evaluate individual candidates).
2. Category-level prompt evaluation agents (evaluate overall decision context).
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from ..services.ai_provider import AIProvider, get_ai_provider

class CandidateEvaluation(BaseModel):
    """
    Structured candidate evaluation returned by a specialized agent.
    Never exposes internal chain-of-thought; returns only concise user-facing reasoning.
    """
    agent: str = Field(..., description="Agent or factor evaluation title")
    candidateId: str = Field(..., description="Unique ID of the evaluated candidate")
    score: float = Field(..., ge=0.0, le=100.0, description="Evaluation score between 0 and 100")
    reason: str = Field(..., description="Concise, user-facing rationale for this score")

    model_config = {
        "json_schema_extra": {
            "example": {
                "agent": "Camera",
                "candidateId": "phone-pixel8a",
                "score": 96.0,
                "reason": "Outstanding computational photography and HDR image pipeline."
            }
        }
    }


class BaseCandidateAgent(ABC):
    """
    Specialized agent that evaluates candidates along a specific factor dimension.
    Agents evaluate candidates; agents are NOT candidates.
    """

    def __init__(self, agent_name: str, factor_key: str):
        self.agent_name = agent_name
        self.factor_key = factor_key

    @abstractmethod
    def evaluate(
        self,
        candidate: Dict[str, Any],
        decision: Optional[DecisionInputSchema] = None,
    ) -> CandidateEvaluation:
        """
        Evaluates a single candidate and returns a structured CandidateEvaluation.
        """
        pass


class BaseAgent(ABC):
    """
    Foundation class for overall category-level decision analysis agents.
    Maintained for backward compatibility with existing orchestrators and UI cards.
    """

    def __init__(
        self,
        id: str,
        name: str,
        specialization: str,
        provider: Optional[AIProvider] = None,
    ):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.provider = provider or get_ai_provider()

    @abstractmethod
    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        """
        Evaluate the user decision along this agent's specialization dimension.
        Returns a validated AgentResult model without exposing chain-of-thought.
        """
        pass
