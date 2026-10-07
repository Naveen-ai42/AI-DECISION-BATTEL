"""
Candidate Provider Factory for Decision Arena.

Selects the appropriate candidate source based on category/subcategory.

For the current expo/demo build, DemoCandidateProvider is the primary
source because it contains category-specific candidate attributes that
are compatible with the specialized decision agents.
"""

from typing import Optional

from .base_provider import BaseCandidateProvider
from .dummyjson_provider import DummyJSONCandidateProvider
from .demo_provider import DemoCandidateProvider


_DUMMYJSON_PROVIDER_INSTANCE: Optional[DummyJSONCandidateProvider] = None
_DEMO_PROVIDER_INSTANCE: Optional[DemoCandidateProvider] = None


# DemoProvider currently has purpose-built candidate data for these domains.
DEMO_SUPPORTED = {
    "electronics": {
        "laptop",
        "smartphone",
        "smartwatch",
        "tablet",
        "headphones",
    },
    "finance": {
        "investment",
        "loan",
    },
    "career": {
        "job",
    },
    "vehicle": {
        "vehicle",
        "motorcycle",
    },
}


# DummyJSON can remain available as an optional external catalog.
DUMMYJSON_SUPPORTED = {
    "electronics": {
        "laptop",
        "smartphone",
        "tablet",
    }
}


def get_candidate_provider(
    category: Optional[str] = None,
    subcategory: Optional[str] = None,
    provider_type: str = "auto",
) -> BaseCandidateProvider:
    """
    Return the candidate provider for the requested decision.

    provider_type:
        - "demo"      -> DemoCandidateProvider
        - "dummyjson" -> DummyJSONCandidateProvider
        - "auto"      -> select the best supported provider automatically
    """

    global _DUMMYJSON_PROVIDER_INSTANCE
    global _DEMO_PROVIDER_INSTANCE

    if _DUMMYJSON_PROVIDER_INSTANCE is None:
        _DUMMYJSON_PROVIDER_INSTANCE = DummyJSONCandidateProvider()

    if _DEMO_PROVIDER_INSTANCE is None:
        _DEMO_PROVIDER_INSTANCE = DemoCandidateProvider()

    p_type = (provider_type or "auto").lower().strip()

    # Explicit provider selection
    if p_type == "dummyjson":
        return _DUMMYJSON_PROVIDER_INSTANCE

    if p_type == "demo":
        return _DEMO_PROVIDER_INSTANCE

    # Automatic provider selection
    cat = (category or "").lower().strip()
    sub = (subcategory or "").lower().strip()

    # Purpose-built demo data takes priority.
    if sub in DEMO_SUPPORTED.get(cat, set()):
        return _DEMO_PROVIDER_INSTANCE

    # Use DummyJSON only where we intentionally support it.
    if sub in DUMMYJSON_SUPPORTED.get(cat, set()):
        return _DUMMYJSON_PROVIDER_INSTANCE

    # For the current expo build, DemoProvider is the safest fallback.
    return _DEMO_PROVIDER_INSTANCE