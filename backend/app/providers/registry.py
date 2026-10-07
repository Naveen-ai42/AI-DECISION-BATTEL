"""
Candidate Provider Registry for Decision Arena.
Dynamically resolves the appropriate CandidateProvider for any category and subcategory.
"""

from typing import List, Dict, Any, Optional
from .base import BaseCandidateProvider
from .electronics_provider import ElectronicsCandidateProvider
from .finance_provider import FinanceCandidateProvider
from .career_provider import CareerCandidateProvider
from .other_providers import (
    EducationCandidateProvider,
    TravelCandidateProvider,
    GenericCandidateProvider,
)
from ..schemas.decision import DecisionInputSchema

# Provider instances
_ELECTRONICS_PROVIDER = ElectronicsCandidateProvider()
_FINANCE_PROVIDER = FinanceCandidateProvider()
_CAREER_PROVIDER = CareerCandidateProvider()
_EDUCATION_PROVIDER = EducationCandidateProvider()
_TRAVEL_PROVIDER = TravelCandidateProvider()
_GENERIC_PROVIDER = GenericCandidateProvider()

def get_candidate_provider(category: str, subcategory: str = "") -> BaseCandidateProvider:
    """
    Resolves the domain-specific candidate provider.
    """
    cat = (category or "electronics").strip().lower()
    if cat == "electronics":
        return _ELECTRONICS_PROVIDER
    elif cat == "finance":
        return _FINANCE_PROVIDER
    elif cat == "career":
        return _CAREER_PROVIDER
    elif cat == "education":
        return _EDUCATION_PROVIDER
    elif cat == "travel":
        return _TRAVEL_PROVIDER
    else:
        return _GENERIC_PROVIDER

def get_candidates_for_decision(
    category: str,
    subcategory: str = "",
    decision: Optional[DecisionInputSchema] = None,
) -> List[Dict[str, Any]]:
    """
    High-level entrypoint for fetching candidate options.
    Returns a dynamically sized list of candidate options from the resolved provider.
    """
    provider = get_candidate_provider(category, subcategory)
    return provider.get_candidates(category, subcategory, decision)
