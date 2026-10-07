"""
Career Candidate Providers for Decision Arena.
Provides dynamic candidate pools for Job Offers, Career Paths, and Skill Development.
Data source is currently marked as 'demo'.
"""

from typing import List, Dict, Any, Optional
from .base import BaseCandidateProvider, create_candidate_option
from ..schemas.decision import DecisionInputSchema

class JobProvider(BaseCandidateProvider):
    """Provides dynamic candidate options for job offers and roles."""

    DEMO_JOBS = [
        create_candidate_option(
            id="senior-data-scientist-product",
            name="Senior Applied Data Scientist (Product AI Track)",
            category="career",
            subcategory="job",
            price="₹28–34 LPA",
            description="Leading machine learning & LLM evaluation for user-facing recommendation engines at a Series-C tech scaleup",
            tags=["LLM & RecSys", "Product Impact", "Modern Stack", "Hybrid 2-day", "Tier-1 Equity"],
            attributes={"salary": 93.0, "skillFit": 94.0, "growth": 93.0, "workLifeBalance": 86.0, "stability": 88.0},
            strengths=[
                "Direct architectural ownership of core revenue-generating AI algorithms",
                "Generous equity component with clear secondary liquidation history",
                "High peer density working alongside former tier-1 tech leads",
            ],
            concerns=[
                "Quarterly product releases occasionally involve sprint deadline crunches",
                "High expectation of rapid autonomous delivery with minimal initial hand-holding",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="staff-platform-engineer",
            name="Staff Platform & Distributed Systems Engineer",
            category="career",
            subcategory="job",
            price="₹32–38 LPA",
            description="Architecting global high-throughput streaming pipelines, Kubernetes clusters, and multi-region infrastructure",
            tags=["Kubernetes", "High Scale", "Staff Track", "Competitive Base", "Remote-First"],
            attributes={"salary": 94.0, "skillFit": 86.0, "growth": 88.0, "workLifeBalance": 82.0, "stability": 91.0},
            strengths=[
                "Highest cash base compensation offer among current candidate options",
                "Full remote flexibility with comprehensive home office allowance",
                "Strategic technical leadership role mentoring 12+ backend developers",
            ],
            concerns=[
                "Requires periodic rotational on-call escalations for core tier-0 services",
                "Legacy technical debt in older microservices requires diplomatic refactoring",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="applied-ai-engineering-specialist",
            name="Applied AI Engineering Specialist",
            category="career",
            subcategory="job",
            price="₹27–31 LPA",
            description="Fine-tuning open weights, managing vector databases, and deploying low-latency agentic workflows",
            tags=["Generative AI", "Vector DBs", "RAG Pipelines", "High Market Demand"],
            attributes={"salary": 91.0, "skillFit": 92.0, "growth": 91.0, "workLifeBalance": 83.0, "stability": 86.0},
            strengths=[
                "Working on cutting-edge generative AI and multi-agent systems in production",
                "Skills gained possess immense hiring market premium for the next decade",
                "Balanced hybrid schedule with budget for attending global research conferences",
            ],
            concerns=[
                "Fast-moving tooling landscape means frameworks require continuous learning",
                "Occasional scope creep as business stakeholders experiment with novel AI use cases",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="enterprise-cloud-architect",
            name="Enterprise Cloud Infrastructure Architect",
            category="career",
            subcategory="job",
            price="₹29–33 LPA",
            description="Designing secure multi-cloud governance and compliance frameworks for global Fortune 500 financial clients",
            tags=["Enterprise Security", "Predictable Hours", "Fortune 500", "High Job Stability"],
            attributes={"salary": 90.0, "skillFit": 85.0, "growth": 84.0, "workLifeBalance": 88.0, "stability": 94.0},
            strengths=[
                "Extremely predictable 40-hour work weeks with strict boundary enforcement",
                "Exceptional job security and institutional stability across recession cycles",
                "Comprehensive executive healthcare, pension, and tuition benefits",
            ],
            concerns=[
                "Slower promotion cadence due to formal enterprise annual review cycles",
                "Rigid compliance and security approvals required before deploying code",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="startup-founding-engineer",
            name="High-Growth Tech Scaleup Lead",
            category="career",
            subcategory="job",
            price="₹24–28 LPA + 0.5% Equity",
            description="Early-stage technical lead building end-to-end cloud products from ground zero with venture backing",
            tags=["Founding Engineer", "High Equity", "Zero to One", "Rapid Velocity", "Full Ownership"],
            attributes={"salary": 85.0, "skillFit": 87.0, "growth": 95.0, "workLifeBalance": 72.0, "stability": 78.0},
            strengths=[
                "Maximum exponential career trajectory if company scales to Series-A/B",
                "Complete freedom across tech stack selection, hiring, and system architecture",
                "Zero corporate red tape or bureaucratic review committees",
            ],
            concerns=[
                "Work-life balance is demanding with frequent evening and weekend sprints",
                "Company runway is tied to venture milestones across an 18-month horizon",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="fintech-quantitative-developer",
            name="Quantitative Algorithmic Trading Engineer",
            category="career",
            subcategory="job",
            price="₹35–45 LPA",
            description="Building ultra-low-latency C++ order routing engines and statistical arbitrage execution models",
            tags=["Low Latency", "C++ Systems", "High Compensation", "Algorithmic Trading"],
            attributes={"salary": 98.0, "skillFit": 84.0, "growth": 86.0, "workLifeBalance": 75.0, "stability": 89.0},
            strengths=[
                "Top-tier compensation package with performance-linked trading bonuses",
                "Direct exposure to world-class high-frequency networking infrastructure",
            ],
            concerns=["High-pressure trading floor environment", "Strict non-compete agreements upon departure"],
            source="demo",
        ),
        create_candidate_option(
            id="developer-advocate-lead",
            name="Principal Developer Advocate & Community Architect",
            category="career",
            subcategory="job",
            price="₹25–30 LPA",
            description="Creating open-source tutorials, technical keynotes, and driving global developer adoption for cloud APIs",
            tags=["Public Speaking", "Open Source", "Global Travel", "High Flexibility"],
            attributes={"salary": 87.0, "skillFit": 86.0, "growth": 89.0, "workLifeBalance": 87.0, "stability": 84.0},
            strengths=[
                "Exceptional public personal brand building across global tech conferences",
                "High degree of autonomous schedule management and remote travel allowance",
            ],
            concerns=["Frequent international flight travel can disrupt weekly routines", "Less direct coding time"],
            source="demo",
        ),
    ]

    def get_candidates(
        self,
        category: str,
        subcategory: str = "",
        decision: Optional[DecisionInputSchema] = None,
    ) -> List[Dict[str, Any]]:
        candidates = list(self.DEMO_JOBS)
        if decision and decision.maxCandidates and decision.maxCandidates > 0:
            return candidates[:decision.maxCandidates]
        return candidates


class CareerCandidateProvider(BaseCandidateProvider):
    """Main Career Candidate Provider."""

    def __init__(self):
        self.job_provider = JobProvider()

    def get_candidates(
        self,
        category: str,
        subcategory: str = "",
        decision: Optional[DecisionInputSchema] = None,
    ) -> List[Dict[str, Any]]:
        return self.job_provider.get_candidates(category, subcategory, decision)
