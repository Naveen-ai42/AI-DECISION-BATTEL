"""
Candidate Providers for Education, Travel, Shopping, and Generic Fallbacks.
Data source is currently marked as 'demo'.
"""

from typing import List, Dict, Any, Optional
from .base import BaseCandidateProvider, create_candidate_option
from ..schemas.decision import DecisionInputSchema

class EducationCandidateProvider(BaseCandidateProvider):
    """Provides dynamic candidate options for Education decisions."""

    DEMO_EDUCATION = [
        create_candidate_option(
            id="tier1-ms-ai",
            name="Tier-1 Master's in Applied AI & Distributed Computing",
            category="education",
            subcategory="college",
            price="₹18–24 Lakhs",
            description="Full-time residential MS program with world-renowned AI research labs and top-quartile tech placements",
            tags=["Tier 1", "MS Degree", "AI Labs", "Top Placements"],
            attributes={"academicQuality": 94.0, "cost": 78.0, "placements": 95.0, "experience": 92.0, "futureOpportunity": 96.0},
            strengths=["Highest graduate career trajectory and alumni network density", "Direct mentorship from distinguished faculty"],
            concerns=["Substantial upfront tuition capital requirement"],
            source="demo",
        ),
        create_candidate_option(
            id="germany-public-ms",
            name="German Public University Master's in Computer Science",
            category="education",
            subcategory="college",
            price="₹4–6 Lakhs (Living only)",
            description="Tuition-free English-taught graduate degree in Europe with 18-month post-study work visa",
            tags=["Zero Tuition", "Europe Visa", "Rigor", "Research"],
            attributes={"academicQuality": 91.0, "cost": 94.0, "placements": 88.0, "experience": 89.0, "futureOpportunity": 92.0},
            strengths=["Near-zero tuition fees with outstanding institutional academic rigor", "Full European Schengen mobility and post-study work rights"],
            concerns=["Requires managing self-directed German bureaucratic paperwork and accommodation"],
            source="demo",
        ),
        create_candidate_option(
            id="applied-bootcamp-certification",
            name="Intensive Full-Stack & GenAI Engineer Apprenticeship",
            category="education",
            subcategory="certification",
            price="₹1.5 Lakhs",
            description="6-month practical bootcamp with guaranteed hiring pipeline and dedicated portfolio engineering",
            tags=["6 Months", "Job Guarantee", "Hands-on", "Modern Stack"],
            attributes={"academicQuality": 84.0, "cost": 89.0, "placements": 87.0, "experience": 85.0, "futureOpportunity": 83.0},
            strengths=["Fast 6-month turnaround into active employment without taking multi-year career breaks"],
            concerns=["Lacks the long-term institutional prestige of an accredited master's degree"],
            source="demo",
        ),
    ]

    def get_candidates(self, category: str, subcategory: str = "", decision: Optional[DecisionInputSchema] = None) -> List[Dict[str, Any]]:
        candidates = list(self.DEMO_EDUCATION)
        if decision and decision.maxCandidates and decision.maxCandidates > 0:
            return candidates[:decision.maxCandidates]
        return candidates


class TravelCandidateProvider(BaseCandidateProvider):
    """Provides dynamic candidate options for Travel decisions."""

    DEMO_TRAVEL = [
        create_candidate_option(
            id="himachal-scenic-retreat",
            name="Himachal Valley Eco-Resort & Scenic Homestay",
            category="travel",
            subcategory="destination",
            price="₹35,000 / week",
            description="High-altitude panoramic mountain retreat with guided treks, high-speed fiber internet, and organic farm dining",
            tags=["Mountain View", "Fiber Wi-Fi", "Quiet Nature", "Trekking"],
            attributes={"cost": 88.0, "safety": 92.0, "experience": 95.0, "convenience": 85.0, "attractions": 93.0},
            strengths=["Pristine mountain vistas with serene natural tranquility", "Comfortable dedicated remote work amenities"],
            concerns=["Mountain road transfer requires a 4-hour scenic drive from nearest airport"],
            source="demo",
        ),
        create_candidate_option(
            id="andaman-coastal-gateway",
            name="Andaman Coral Bay Luxury Beachfront Villa",
            category="travel",
            subcategory="destination",
            price="₹65,000 / week",
            description="White sand beach resort with PADI certified scuba diving, bioluminescent night kayaking, and seafood dining",
            tags=["Scuba Diving", "White Sands", "Island Life", "PADI"],
            attributes={"cost": 79.0, "safety": 94.0, "experience": 96.0, "convenience": 82.0, "attractions": 94.0},
            strengths=["World-class turquoise water visibility and untouched marine coral reefs", "Safe resort perimeter with attentive hospitality"],
            concerns=["Flight logistics and ferry timings require disciplined pre-booking"],
            source="demo",
        ),
    ]

    def get_candidates(self, category: str, subcategory: str = "", decision: Optional[DecisionInputSchema] = None) -> List[Dict[str, Any]]:
        candidates = list(self.DEMO_TRAVEL)
        if decision and decision.maxCandidates and decision.maxCandidates > 0:
            return candidates[:decision.maxCandidates]
        return candidates


class GenericCandidateProvider(BaseCandidateProvider):
    """Generic fallback candidate provider producing dynamic candidates."""

    def get_candidates(self, category: str, subcategory: str = "", decision: Optional[DecisionInputSchema] = None) -> List[Dict[str, Any]]:
        cat = (category or "other").capitalize()
        pool = [
            create_candidate_option(
                id=f"{category}-choice-1",
                name=f"Top-Tier Strategic Choice ({cat} Solution A)",
                category=category,
                subcategory=subcategory,
                price="Premium Tier",
                description="Engineered for high capability headroom, rigorous safety compliance, and multi-year durability.",
                tags=["Top Alignment", "High Durability", "Recommended"],
                attributes={"optionFit": 93.0, "value": 85.0, "risk": 89.0, "experience": 92.0, "longTermImpact": 91.0},
                strengths=["Maximum alignment with primary stated criteria", "Proven operational reliability across benchmark evaluations"],
                concerns=["Requires higher upfront commitment"],
                source="demo",
            ),
            create_candidate_option(
                id=f"{category}-choice-2",
                name=f"High-Value Balanced Choice ({cat} Solution B)",
                category=category,
                subcategory=subcategory,
                price="Balanced Tier",
                description="Optimized price-to-feature performance delivering rapid time-to-value with minimal overhead.",
                tags=["High Value", "Fast ROI", "Accessible"],
                attributes={"optionFit": 89.0, "value": 93.0, "risk": 87.0, "experience": 87.0, "longTermImpact": 85.0},
                strengths=["Best efficiency per unit cost in the candidate group", "Smooth adoption curve with low friction"],
                concerns=["Secondary luxury features are omitted to preserve value"],
                source="demo",
            ),
            create_candidate_option(
                id=f"{category}-choice-3",
                name=f"Conservative Low-Risk Choice ({cat} Solution C)",
                category=category,
                subcategory=subcategory,
                price="Standard Tier",
                description="Emphasizes stability, low historical variance, and predictable guaranteed outcomes.",
                tags=["Low Risk", "Stable", "Proven"],
                attributes={"optionFit": 86.0, "value": 88.0, "risk": 95.0, "experience": 85.0, "longTermImpact": 87.0},
                strengths=["Near-zero downside surprise or disruption", "Standardized and battle-tested execution profile"],
                concerns=["Does not capture aggressive exponential upside"],
                source="demo",
            ),
        ]
        if decision and decision.maxCandidates and decision.maxCandidates > 0:
            return pool[:decision.maxCandidates]
        return pool
