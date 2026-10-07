from .base import BaseCandidateProvider, create_candidate_option
from .registry import get_candidate_provider, get_candidates_for_decision
from .electronics_provider import (
    ElectronicsCandidateProvider,
    LaptopProvider,
    SmartphoneProvider,
    SmartwatchProvider,
)
from .finance_provider import FinanceCandidateProvider, InvestmentProvider
from .career_provider import CareerCandidateProvider, JobProvider

__all__ = [
    "BaseCandidateProvider",
    "create_candidate_option",
    "get_candidate_provider",
    "get_candidates_for_decision",
    "ElectronicsCandidateProvider",
    "LaptopProvider",
    "SmartphoneProvider",
    "SmartwatchProvider",
    "FinanceCandidateProvider",
    "InvestmentProvider",
    "CareerCandidateProvider",
    "JobProvider",
]
