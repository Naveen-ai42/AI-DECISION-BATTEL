from fastapi import APIRouter, HTTPException, status
from ..schemas.decision import DecisionInputSchema, AnalysisResponseSchema
from ..services.analysis_service import analysis_service

router = APIRouter(tags=["Analysis"])

@router.post(
    "/analysis",
    response_model=AnalysisResponseSchema,
    summary="Multi-Agent Decision Analysis",
    status_code=status.HTTP_200_OK,
)
async def analyze_decision(decision: DecisionInputSchema):
    """
    Accepts a user decision payload, dynamically executes 5 specialized autonomous agents
    tailored to the selected category (electronics, finance, career, education, travel, shopping, other),
    and calculates weighted composite recommendations through the category-aware Decision Engine.
    """
    # 1. Validate description content
    if not decision.description or not decision.description.strip():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Description is required and must not be empty.",
        )

    # 2. Execute full analysis pipeline via AnalysisService
    return analysis_service.analyze_decision(decision)
