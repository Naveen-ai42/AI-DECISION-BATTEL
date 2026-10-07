"""
Backward compatibility bridge for agent factory.
Re-exports functions and classes from backend/app/agents/agent_factory.py.
"""

from typing import List, Optional
from .agent_factory import (
    get_agents_for_category,
    get_specialized_agents,
    FACTOR_AGENT_REGISTRY,
)
from ..core.decision_config import get_decision_config

def get_category_factors(category: str, subcategory: Optional[str] = None) -> List[str]:
    """
    Returns the list of factor keys for the given category and subcategory.
    """
    cfg = get_decision_config(category, subcategory)
    return [f.key for f in cfg.factors]

__all__ = [
    "get_category_factors",
    "get_agents_for_category",
    "get_specialized_agents",
    "FACTOR_AGENT_REGISTRY",
]
