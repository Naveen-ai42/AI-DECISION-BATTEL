"""
DummyJSON Candidate Provider for Decision Arena.
Queries the external DummyJSON product catalog dynamically, caches responses in-memory,
and normalizes records into internal candidate models.

Cleanly separated: the decision engine does not know candidates came from DummyJSON.
"""

import json
import time
import urllib.request
import urllib.error
from typing import List, Dict, Any, Optional

from .base_provider import BaseCandidateProvider
from .normalizer import normalize_dummyjson_catalog
from ..catalog.category_mapping import map_to_external_category

# Simple in-memory cache for external API responses
# Cache key -> (timestamp, List[Dict[str, Any]])
_CATALOG_CACHE: Dict[str, tuple[float, List[Dict[str, Any]]]] = {}
CACHE_TTL_SECONDS = 300  # 5 minutes


class ExternalCatalogUnavailableError(Exception):
    """Raised when external catalog API cannot be reached or times out."""
    pass


class UnsupportedSubcategoryError(Exception):
    """Raised when external catalog does not support the requested subcategory."""
    pass


class DummyJSONCandidateProvider(BaseCandidateProvider):
    """
    Dynamic candidate provider pulling real product catalog data from DummyJSON.
    """

    def __init__(self, base_url: str = "https://dummyjson.com/products"):
        self.base_url = base_url.rstrip("/")

    def get_candidates(
        self,
        category: str,
        subcategory: Optional[str] = None,
        decision: Optional[Any] = None,
    ) -> List[Dict[str, Any]]:
        """
        Retrieves normalized candidates from DummyJSON for the requested category/subcategory.
        Does NOT restrict candidate pool to 5 items; retrieves all available candidates in catalog.
        """
        cat = (category or "electronics").strip().lower()
        sub = (subcategory or "").strip().lower()

        # 1. Map to external DummyJSON category slug
        external_slug = map_to_external_category(cat, sub)
        if not external_slug:
            raise UnsupportedSubcategoryError(
                f"Data source unavailable for category '{category}' and subcategory '{subcategory}'. "
                f"Supported DummyJSON subcategories include: laptop, smartphone, tablet, vehicle, motorcycle, watch, accessories."
            )

        # 2. Check in-memory cache
        cache_key = f"{cat}:{sub}:{external_slug}"
        now = time.time()
        if cache_key in _CATALOG_CACHE:
            cached_time, cached_products = _CATALOG_CACHE[cache_key]
            if now - cached_time < CACHE_TTL_SECONDS:
                return normalize_dummyjson_catalog(cached_products, category=cat, subcategory=sub)

        # 3. Query external API dynamically
        # Retrieve all items in the category using limit=100
        url = f"{self.base_url}/category/{external_slug}?limit=100"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) DecisionArena/1.0",
            "Accept": "application/json",
        }

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=8.0) as response:
                status_code = response.getcode()
                if status_code != 200:
                    raise ExternalCatalogUnavailableError(
                        f"External product catalog returned HTTP {status_code}"
                    )
                raw_bytes = response.read()
                data = json.loads(raw_bytes.decode("utf-8"))

        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise UnsupportedSubcategoryError(
                    f"Category '{external_slug}' not found in external catalog."
                )
            raise ExternalCatalogUnavailableError(
                f"External product catalog error (HTTP {e.code}): {e.reason}"
            )
        except urllib.error.URLError as e:
            raise ExternalCatalogUnavailableError(
                f"Could not connect to external catalog provider: {e.reason}"
            )
        except Exception as e:
            raise ExternalCatalogUnavailableError(
                f"Failed fetching candidates from external catalog: {str(e)}"
            )

        raw_products = data.get("products", [])
        if not isinstance(raw_products, list):
            raw_products = []

        # Store in cache
        _CATALOG_CACHE[cache_key] = (now, raw_products)

        # 4. Normalize candidates into internal schema
        normalized = normalize_dummyjson_catalog(raw_products, category=cat, subcategory=sub)
        return normalized
