"""
Base Candidate Provider Abstraction for Decision Arena.
Defines the generic interface for retrieving dynamically sized pools of candidate options.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from ..schemas.decision import DecisionInputSchema

def create_candidate_option(
    id: str,
    name: str,
    category: str,
    subcategory: str,
    price: Any = "",
    attributes: Optional[Dict[str, float]] = None,
    description: str = "",
    tags: Optional[List[str]] = None,
    strengths: Optional[List[str]] = None,
    concerns: Optional[List[str]] = None,
    source: str = "demo",
) -> Dict[str, Any]:
    """
    Standard generic candidate model conforming to Decision Arena architecture:
    {
        "id": "unique-id",
        "name": "Option Name",
        "category": "electronics",
        "subcategory": "laptop",
        "price": 55000,
        "attributes": {},
        "source": "demo"
    }
    """
    return {
        "id": id,
        "name": name,
        "category": category,
        "subcategory": subcategory,
        "price": str(price),
        "attributes": attributes or {},
        "description": description,
        "tags": tags or [],
        "strengths": strengths or [],
        "concerns": concerns or [],
        "source": source,
    }


class BaseCandidateProvider(ABC):
    """
    Abstract Candidate Provider:
    Decouples candidate option retrieval from AI agents and Decision Engine.
    Subclasses can source candidates from demo datasets, internal databases,
    partner APIs, web scraping, or vector indices.
    """

    @abstractmethod
    def get_candidates(
        self,
        category: str,
        subcategory: str = "",
        decision: Optional[DecisionInputSchema] = None,
    ) -> List[Dict[str, Any]]:
        """
        Retrieves a dynamically sized list of candidate options.
        Must NOT assume a fixed number of items.
        """
        pass
