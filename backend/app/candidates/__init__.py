"""
Candidate Provider Package for Decision Arena.
"""

from .base_provider import BaseCandidateProvider
from .dummyjson_provider import (
    DummyJSONCandidateProvider,
    ExternalCatalogUnavailableError,
    UnsupportedSubcategoryError,
)
from .demo_provider import DemoCandidateProvider
from .normalizer import (
    normalize_dummyjson_product,
    normalize_dummyjson_catalog,
)
from .provider_factory import get_candidate_provider

__all__ = [
    "BaseCandidateProvider",
    "DummyJSONCandidateProvider",
    "ExternalCatalogUnavailableError",
    "UnsupportedSubcategoryError",
    "DemoCandidateProvider",
    "normalize_dummyjson_product",
    "normalize_dummyjson_catalog",
    "get_candidate_provider",
]
