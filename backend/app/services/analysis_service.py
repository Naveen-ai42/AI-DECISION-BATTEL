"""
Analysis Service for Decision Arena.
Coordinates the end-to-end multi-agent and dynamic decision engine lifecycle.
"""

from typing import Optional
from fastapi import HTTPException, status
from ..schemas.decision import DecisionInputSchema, AnalysisResponseSchema
from ..agents.orchestrator import DecisionOrchestrator
from .decision_service import calculate_decision_outcome
from .ai_provider import AIProvider, get_ai_provider
from ..decision.factor_selector import detect_category_and_subcategory

class AnalysisService:
    """
    Analysis Service:
    Coordinates the full decision evaluation lifecycle:
    1. Detects category and subcategory semantics.
    2. Runs overview agents for decision card insights.
    3. Executes dynamic decision engine:
       - Loads subcategory factors
       - Fetches candidates from CandidateProvider (DummyJSON / Demo)
       - Applies Requirement, Budget, and Deal-breaker filtering
       - Runs specialized factor agents on every candidate
       - Calculates weighted scores from candidate attributes + user priorities
       - Ranks candidates in descending order
    4. Assembles and returns comprehensive AnalysisResponseSchema.
    """

    def __init__(self, provider: Optional[AIProvider] = None):
        self.provider = provider or get_ai_provider()
        self.orchestrator = DecisionOrchestrator(provider=self.provider)

    def analyze_decision(self, decision: DecisionInputSchema) -> AnalysisResponseSchema:
        """
        Executes end-to-end multi-agent analysis and dynamic candidate ranking.
        """
        try:
            # Step 1: Detect canonical category and subcategory
            detected_category, detected_subcategory = detect_category_and_subcategory(
                category=decision.category,
                subcategory=decision.subcategory,
                description=decision.description,
            )

            decision.category = detected_category
            if not decision.subcategory:
                decision.subcategory = detected_subcategory

            # Step 2: Run high-level overview agents
            agent_results = self.orchestrator.run_all(decision)

            # Step 3: Run dynamic candidate evaluation engine
            response = calculate_decision_outcome(decision, agent_results)
            return response

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred during multi-agent analysis: {str(e)}",
            )

analysis_service = AnalysisService()
