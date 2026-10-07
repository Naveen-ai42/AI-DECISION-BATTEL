"""
Centralized Dynamic Decision Configuration Bridge for Decision Arena.
Re-exports the modular decision configuration from backend/app/decision.
"""

from ..decision.category_config import (
    DECISION_CONFIG,
    CategoryConfig,
    SubcategoryConfig,
    FactorDefinition,
)
from ..decision.factor_selector import (
    detect_category_and_subcategory,
    get_decision_config,
    get_factors_for_decision,
)

__all__ = [
    "DECISION_CONFIG",
    "CategoryConfig",
    "SubcategoryConfig",
    "FactorDefinition",
    "detect_category_and_subcategory",
    "get_decision_config",
    "get_factors_for_decision",
]
