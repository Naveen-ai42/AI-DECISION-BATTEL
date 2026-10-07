"""
Base Candidate Provider Abstraction for Decision Arena.
Defines the abstract interface for retrieving candidate options.
Enables pluggable data providers (Demo, Local Database, External API, Scraping, etc.).
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class BaseCandidateProvider(ABC):
    """
    Abstract Base Class for Candidate Providers.
    Any connected candidate source (Demo, Database, REST API) must implement this interface.
    """

    @abstractmethod
    def get_candidates(
        self,
        category: str,
        subcategory: Optional[str] = None,
        decision: Optional[Any] = None,
    ) -> List[Dict[str, Any]]:
        """
        Retrieves candidate options matching the given category and subcategory.

        Args:
            category: Decision domain category (e.g. 'electronics', 'finance', 'career')
            subcategory: Subcategory or candidate type (e.g. 'laptop', 'smartphone', 'investment')
            decision: Optional DecisionInputSchema containing budget, requirements, etc.

        Returns:
            A dynamic list of candidate dictionaries:
            [
                {
                    "id": str,
                    "name": str,
                    "category": str,
                    "subcategory": str,
                    "price": str,
                    "attributes": Dict[str, float],
                    "description": str,
                    "strengths": List[str],
                    "concerns": List[str],
                    "tags": List[str],
                    "source": str,
                },
                ...
            ]
        """
        pass
