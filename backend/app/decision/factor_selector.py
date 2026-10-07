"""
Factor Selector for Decision Arena.
Selects and returns the precise domain evaluation factors for any given category and subcategory.
Ensures factors are strictly domain-specific (e.g. vehicle factors never mix with electronics).
"""

from typing import List, Optional, Tuple, Dict, Any
from .category_config import DECISION_CONFIG, SubcategoryConfig, FactorDefinition

def detect_category_and_subcategory(
    category: Optional[str],
    subcategory: Optional[str],
    description: Optional[str] = "",
) -> Tuple[str, str]:
    """
    Infers and resolves canonical (category, subcategory) pair:
    1. If explicit category and subcategory are provided and valid, returns them.
    2. If subcategory is missing or blank, infers semantically from user decision description.
    3. Falls back safely without crashing.
    """
    cat = (category or "").strip().lower()
    sub = (subcategory or "").strip().lower()
    desc = (description or "").lower()

    # Detect category from description if missing or generic
    if not cat or cat not in DECISION_CONFIG:
        if any(term in desc for term in ["car", "vehicle", "suv", "sedan", "automobile", "motorcycle", "bike", "drive"]):
            cat = "vehicle"
        elif any(term in desc for term in ["invest", "mutual fund", "sip", "stock", "loan", "emi", "portfolio"]):
            cat = "finance"
        elif any(term in desc for term in ["job", "offer", "salary", "career", "role", "tech lead"]):
            cat = "career"
        else:
            cat = "electronics"

    cat_config = DECISION_CONFIG.get(cat, DECISION_CONFIG["electronics"])

    # If explicit subcategory is provided: check direct match or canonical aliases
    if sub:
        if sub in cat_config.subcategories:
            return cat, sub
        # Check canonical aliases
        alias_map = {
            "laptops": "laptop",
            "notebook": "laptop",
            "smartphones": "smartphone",
            "phones": "smartphone",
            "phone": "smartphone",
            "mobile": "smartphone",
            "tablets": "tablet",
            "ipads": "tablet",
            "cars": "vehicle",
            "car": "vehicle",
            "automobiles": "vehicle",
            "automobile": "vehicle",
            "motorcycles": "motorcycle",
            "bikes": "motorcycle",
            "bike": "motorcycle",
            "watches": "smartwatch",
            "headphones": "headphones",
            "earphones": "headphones",
            "earbuds": "headphones",
        }
        if sub in alias_map and alias_map[sub] in cat_config.subcategories:
            return cat, alias_map[sub]
        # Return the requested subcategory directly so provider reports data source unavailable
        return cat, sub

    # When subcategory is omitted/empty, infer semantically based on description keywords
    if cat == "electronics":
        if any(term in desc for term in ["tablet", "ipad", "tab", "stylus", "drawing"]):
            return cat, "tablet"
        elif any(term in desc for term in ["phone", "smartphone", "mobile", "android", "iphone", "pixel", "oneplus", "camera"]):
            return cat, "smartphone"
        elif any(term in desc for term in ["watch", "smartwatch", "fitness band", "garmin", "fitbit"]):
            return cat, "smartwatch"
        elif any(term in desc for term in ["headphone", "earbud", "earphone", "anc", "tws", "audio"]):
            return cat, "headphones"
        elif any(term in desc for term in ["laptop", "notebook", "macbook", "pc", "gaming laptop", "computer", "coding"]):
            return cat, "laptop"
        return cat, cat_config.defaultSubcategory

    elif cat == "vehicle":
        if any(term in desc for term in ["motorcycle", "bike", "two-wheeler", "scooter"]):
            return cat, "motorcycle"
        return cat, "vehicle"

    elif cat == "finance":
        if any(term in desc for term in ["loan", "emi", "borrow", "home loan", "personal loan"]):
            return cat, "loan"
        return cat, "investment"

    elif cat == "career":
        return cat, "job"

    return cat, cat_config.defaultSubcategory


def get_decision_config(category: str, subcategory: Optional[str] = None) -> SubcategoryConfig:
    """
    Retrieves the exact SubcategoryConfig defining the factors, agents, and criteria.
    """
    cat = (category or "electronics").strip().lower()
    sub = (subcategory or "").strip().lower()

    if cat not in DECISION_CONFIG:
        cat = "electronics"

    cat_config = DECISION_CONFIG[cat]
    if sub in cat_config.subcategories:
        return cat_config.subcategories[sub]

    return cat_config.subcategories[cat_config.defaultSubcategory]


def get_factors_for_decision(category: str, subcategory: Optional[str] = None) -> List[str]:
    """
    Returns the list of factor keys applicable for the resolved category and subcategory.
    """
    cfg = get_decision_config(category, subcategory)
    return [f.key for f in cfg.factors]
