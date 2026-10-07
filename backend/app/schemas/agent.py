from typing import List
from pydantic import BaseModel, Field

class AgentResult(BaseModel):
    """
    Structured evaluation result produced by a specialized agent.
    Never exposes internal chain-of-thought.
    """
    agent: str = Field(..., description="Agent display name")
    score: float = Field(..., ge=0.0, le=100.0, description="Evaluation score between 0 and 100")
    strengths: List[str] = Field(default_factory=list, description="Key strengths identified by this agent")
    concerns: List[str] = Field(default_factory=list, description="Key concerns or trade-offs identified")
    conclusion: str = Field(..., description="Executive conclusion summary")
    factors: List[str] = Field(default_factory=list, description="Core dimensions evaluated")

    model_config = {
        "json_schema_extra": {
            "example": {
                "agent": "Performance Agent",
                "score": 92.0,
                "strengths": [
                    "Strong CPU performance",
                    "Good RAM capacity"
                ],
                "concerns": [
                    "Dedicated GPU may increase power usage"
                ],
                "conclusion": "Strong choice for coding and AI/ML workloads.",
                "factors": [
                    "CPU performance",
                    "RAM",
                    "GPU capability"
                ]
            }
        }
    }

# Backward compatibility alias
AgentResultSchema = AgentResult
