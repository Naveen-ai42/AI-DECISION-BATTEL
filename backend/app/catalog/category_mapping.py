"""
Category Mapping Module for External Catalog Providers.
Maps internal domain categories & subcategories to external catalog categories (e.g. DummyJSON).
Ensures clear separation between domain modeling and external data sources.
"""

from typing import Optional, Dict, Tuple, List

# Mapping from (internal_category, internal_subcategory) -> DummyJSON category slug
DUMMYJSON_CATEGORY_MAP: Dict[Tuple[str, str], str] = {
    # Electronics
    ("electronics", "laptop"): "laptops",
    ("electronics", "laptops"): "laptops",
    ("electronics", "notebook"): "laptops",
    ("electronics", "smartphone"): "smartphones",
    ("electronics", "smartphones"): "smartphones",
    ("electronics", "phone"): "smartphones",
    ("electronics", "mobile"): "smartphones",
    ("electronics", "tablet"): "tablets",
    ("electronics", "tablets"): "tablets",
    ("electronics", "ipad"): "tablets",
    ("electronics", "smartwatch"): "mens-watches",
    ("electronics", "watch"): "mens-watches",
    ("electronics", "accessories"): "mobile-accessories",

    # Vehicle / Transportation
    ("vehicle", "vehicle"): "vehicle",
    ("vehicle", "car"): "vehicle",
    ("vehicle", "cars"): "vehicle",
    ("vehicle", "automobile"): "vehicle",
    ("vehicle", "sedan"): "vehicle",
    ("vehicle", "suv"): "vehicle",
    ("vehicle", "motorcycle"): "motorcycle",
    ("vehicle", "bike"): "motorcycle",
    ("transportation", "vehicle"): "vehicle",
    ("automotive", "vehicle"): "vehicle",

    # Shopping
    ("shopping", "furniture"): "furniture",
    ("shopping", "groceries"): "groceries",
    ("shopping", "beauty"): "beauty",
    ("shopping", "fragrances"): "fragrances",
    ("shopping", "sunglasses"): "sunglasses",
}

# Subcategory aliases for semantic query normalization
SUBCATEGORY_ALIASES: Dict[str, str] = {
    "laptops": "laptop",
    "notebook": "laptop",
    "smartphones": "smartphone",
    "phones": "smartphone",
    "phone": "smartphone",
    "mobile": "smartphone",
    "tablets": "tablet",
    "cars": "vehicle",
    "car": "vehicle",
    "automobile": "vehicle",
    "vehicles": "vehicle",
}

def map_to_external_category(category: str, subcategory: Optional[str] = None) -> Optional[str]:
    """
    Translates an internal (category, subcategory) pair into an external DummyJSON category slug.
    Returns None if the subcategory is not supported by the external catalog provider.
    """
    cat = (category or "").strip().lower()
    sub = (subcategory or "").strip().lower()

    if not sub:
        # Default subcategory mappings per category
        if cat == "electronics":
            sub = "laptop"
        elif cat in {"vehicle", "automotive", "transportation"}:
            cat = "vehicle"
            sub = "vehicle"
        elif cat == "shopping":
            sub = "furniture"

    # Normalize alias
    sub = SUBCATEGORY_ALIASES.get(sub, sub)

    # Direct tuple lookup
    if (cat, sub) in DUMMYJSON_CATEGORY_MAP:
        return DUMMYJSON_CATEGORY_MAP[(cat, sub)]

    # Secondary check with normalized category
    if cat in {"vehicle", "automotive", "transportation"}:
        return "vehicle"

    return None

def is_subcategory_supported(category: str, subcategory: Optional[str] = None) -> bool:
    """Returns True if the external data provider can serve candidates for this subcategory."""
    return map_to_external_category(category, subcategory) is not None

def get_supported_categories() -> List[str]:
    """Returns a list of supported category/subcategory descriptions."""
    return [
        "electronics (laptop, smartphone, tablet, smartwatch)",
        "vehicle (vehicle, car, motorcycle)",
        "shopping (furniture, beauty, fragrances, groceries)",
    ]
