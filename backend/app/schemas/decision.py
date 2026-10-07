from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, field_validator
from .agent import AgentResult, AgentResultSchema

VALID_CATEGORIES = {
    "electronics",
    "vehicle",
    "transportation",
    "career",
    "education",
    "finance",
    "travel",
    "shopping",
    "other",
}

VALID_RISK_TOLERANCES = {
    "low",
    "balanced",
    "high",
}

VALID_DECISION_STYLES = {
    "best-overall",
    "best-value",
    "best-performance",
    "best-long-term",
}

# Dynamic priorities dictionary alias for compatibility
PrioritiesSchema = Dict[str, float]

class DecisionInputSchema(BaseModel):
    description: str = Field(..., description="Core decision prompt or dilemma")
    category: str = Field(default="electronics", description="Category of decision")
    subcategory: Optional[str] = Field(default="", description="Optional subcategory (e.g. laptop, smartphone, smartwatch, investment, offer)")
    budget: Optional[str] = Field(default="", description="Optional budget constraint")
    location: Optional[str] = Field(default="", description="Optional location constraint")
    deadline: Optional[str] = Field(default="", description="Optional deadline constraint")
    additionalRequirements: Optional[str] = Field(default="", description="Optional extra notes or context")
    requirements: List[str] = Field(default_factory=list, description="List of must-have requirements")
    dealBreakers: List[str] = Field(default_factory=list, description="List of negative deal-breakers")
    priorities: Dict[str, float] = Field(
        default_factory=dict,
        description="Dynamic normalized priority weights for the selected category totaling 100%"
    )
    riskTolerance: str = Field(default="balanced", description="Risk tolerance: low | balanced | high")
    decisionStyle: str = Field(default="best-overall", description="Decision style: best-overall | best-value | best-performance | best-long-term")

    @field_validator("description")
    @classmethod
    def validate_description(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("Description is required and must not be empty.")
        return v.strip()

    @field_validator("category")
    @classmethod
    def validate_category(cls, v: str) -> str:
        cleaned = v.strip().lower() if v else "electronics"
        if cleaned not in VALID_CATEGORIES:
            valid_list = ", ".join(sorted(VALID_CATEGORIES))
            raise ValueError(f"Invalid category '{v}'. Must be one of: {valid_list}")
        return cleaned

    @field_validator("priorities")
    @classmethod
    def validate_priorities(cls, v: Any) -> Dict[str, float]:
        if not v:
            return {}
        if isinstance(v, dict):
            cleaned: Dict[str, float] = {}
            for k, val in v.items():
                try:
                    num = float(val)
                except (ValueError, TypeError):
                    raise ValueError(f"Priority weight for '{k}' must be a numeric value.")
                if num < 0 or num > 100:
                    raise ValueError(f"Priority weight for '{k}' must be between 0 and 100.")
                cleaned[str(k)] = num

            total = sum(cleaned.values())
            if abs(total - 100.0) > 0.1:
                raise ValueError(
                    f"Priority weights must total exactly 100%. Current total: {total:.1f}%"
                )
            return cleaned
        raise ValueError("Priorities must be a dictionary of factor weights.")

    @field_validator("riskTolerance")
    @classmethod
    def validate_risk_tolerance(cls, v: str) -> str:
        cleaned = v.strip().lower() if v else "balanced"
        if cleaned not in VALID_RISK_TOLERANCES:
            valid_list = ", ".join(sorted(VALID_RISK_TOLERANCES))
            raise ValueError(f"Invalid riskTolerance '{v}'. Must be one of: {valid_list}")
        return cleaned

    @field_validator("decisionStyle")
    @classmethod
    def validate_decision_style(cls, v: str) -> str:
        cleaned = v.strip().lower() if v else "best-overall"
        if cleaned not in VALID_DECISION_STYLES:
            valid_list = ", ".join(sorted(VALID_DECISION_STYLES))
            raise ValueError(f"Invalid decisionStyle '{v}'. Must be one of: {valid_list}")
        return cleaned

    model_config = {
        "json_schema_extra": {
            "example": {
                "description": "Choose the best investment option for ₹2 lakh",
                "category": "finance",
                "budget": "200000",
                "location": "",
                "deadline": "",
                "additionalRequirements": "Moderate risk with long-term growth",
                "requirements": [
                    "Moderate risk",
                    "Long-term growth"
                ],
                "dealBreakers": [
                    "Very high risk"
                ],
                "priorities": {
                    "returnPotential": 30,
                    "risk": 25,
                    "liquidity": 15,
                    "stability": 20,
                    "growth": 10
                },
                "riskTolerance": "balanced",
                "decisionStyle": "best-overall"
            }
        }
    }

    topN: int = Field(default=5, description="Number of top options to highlight (default 5)")
    maxCandidates: Optional[int] = Field(default=None, description="Optional maximum candidate pool size limit for simulation or pagination")

class CandidateEvaluationSchema(BaseModel):
    agent: str = Field(..., description="Agent or factor evaluation title")
    candidateId: str = Field(..., description="Unique ID of the evaluated candidate")
    score: float = Field(..., ge=0.0, le=100.0, description="Evaluation score between 0 and 100")
    reason: str = Field(..., description="Concise, user-facing rationale for this score")

class RankedOptionSchema(BaseModel):
    rank: int = Field(..., description="Rank position (1 is best overall)")
    id: str = Field(..., description="Option identifier")
    name: str = Field(..., description="Option display name")
    option: Optional[str] = Field(default=None, description="Alias for name matching user specification")
    brand: Optional[str] = Field(default="", description="Product brand name")
    image: Optional[str] = Field(default="", description="Primary product image URL")
    thumbnail: Optional[str] = Field(default="", description="Thumbnail image URL")
    rating: Optional[float] = Field(default=None, description="External consumer rating out of 5.0")
    candidate: Optional[Dict[str, Any]] = Field(default=None, description="Raw candidate object with domain attributes")
    score: float = Field(..., description="Final overall weighted score (0-100)")
    overallScore: Optional[float] = Field(default=None, description="Alias for score matching user specification")
    rawScore: float = Field(default=0.0, description="Raw unpenalized weighted score")
    confidence: str = Field(default="High", description="Candidate confidence rating")
    why: Optional[str] = Field(default="", description="Executive explanation of why this option ranked at this position")
    price: Optional[str] = Field(default="", description="Price or cost indicator")
    description: Optional[str] = Field(default="", description="Short option description or spec highlights")
    category: Optional[str] = Field(default="", description="Option category")
    subcategory: Optional[str] = Field(default="", description="Option subcategory")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Generic domain attribute map")
    factorScores: Dict[str, float] = Field(default_factory=dict, description="Agent evaluation score for each factor")
    agentEvaluations: List[CandidateEvaluationSchema] = Field(default_factory=list, description="Evaluations from each specialized agent for this candidate")
    strengths: List[str] = Field(default_factory=list, description="Top positive strengths")
    concerns: List[str] = Field(default_factory=list, description="Potential trade-offs or concerns")
    requirementsPassed: List[str] = Field(default_factory=list, description="Must-have requirements satisfied")
    requirementsMissed: List[str] = Field(default_factory=list, description="Must-have requirements not met")
    dealBreakersTriggered: List[str] = Field(default_factory=list, description="Deal-breaker criteria triggered")
    badge: Optional[str] = Field(default="", description="Optional award badge e.g. Best Overall, Runner-up, Value Pick")
    source: str = Field(default="dummyjson", description="Data source: dummyjson | database | external-api")

class ComparisonMatrixSchema(BaseModel):
    factors: List[Dict[str, str]] = Field(default_factory=list, description="List of factor definitions {key, name}")
    options: List[Dict[str, Any]] = Field(default_factory=list, description="Row entries with factor scores for each option")

class DecisionEngineResultSchema(BaseModel):
    overallScore: float = Field(..., description="Calculated weighted composite score of rank #1")
    recommendation: str = Field(..., description="Winning option or choice name")
    confidence: str = Field(default="High", description="Decision confidence heuristic (High, Medium, Low)")
    totalOptionsEvaluated: int = Field(default=0, description="Count of candidate options evaluated")

class AnalysisResponseSchema(BaseModel):
    status: str = Field(default="success", description="Status code: 'success' | 'no_matches' | 'error'")
    message: Optional[str] = Field(default=None, description="Optional informational or no-match message")
    suggestions: List[str] = Field(default_factory=list, description="Helpful next-step suggestions when no matches or warnings occur")
    category: str = Field(default="electronics", description="Selected decision category")
    subcategory: str = Field(default="", description="Selected decision subcategory / type")
    factors: List[Dict[str, Any]] = Field(default_factory=list, description="Active decision factors and weights for this subcategory")
    candidateCount: int = Field(default=0, description="Total candidates in candidate pool retrieved from provider")
    filteredCandidateCount: Optional[int] = Field(default=None, description="Count of candidates that passed filter pipeline")
    topN: int = Field(default=5, description="Configured top-N candidates displayed prominently")
    rankedCandidates: List[RankedOptionSchema] = Field(default_factory=list, description="All evaluated candidates ranked from best to worst")
    bestOverall: Optional[RankedOptionSchema] = Field(default=None, description="Top ranked #1 recommendation")
    explanation: Optional[str] = Field(default="", description="High-level decision synthesis explanation")
    agents: List[AgentResult] = Field(default_factory=list, description="List of evaluations from specialized autonomous agents")
    rankings: List[RankedOptionSchema] = Field(default_factory=list, description="Backward compatibility alias for rankedCandidates")
    comparison: Optional[ComparisonMatrixSchema] = Field(default=None, description="Side-by-side factor comparison matrix")
    decision: Optional[DecisionEngineResultSchema] = Field(default=None, description="Decision Engine weighted result and recommendation")
    decisionEngine: Optional[DecisionEngineResultSchema] = Field(default=None, description="Compatibility alias for frontend")
    dataSource: str = Field(default="dummyjson", description="Candidate pool data source (e.g. dummyjson, database, external-api)")
    isDemoData: bool = Field(default=False, description="Indicates whether synthetic test data is in use")
    fallbackNotice: Optional[str] = Field(default=None, description="Fallback notice if filter required relaxing")
