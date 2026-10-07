from typing import Optional
from .base_agent import BaseAgent
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult
from ..services.ai_provider import AIProvider

# =====================================================================
# 1. ELECTRONICS AGENTS
# =====================================================================

class PerformanceAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="performance",
            name="Performance Agent",
            specialization="CPU, GPU, RAM, coding & AI/ML compute capability",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class ValueAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="value",
            name="Value Agent",
            specialization="Price, features, performance per price & budget fit",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class BatteryAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="battery",
            name="Battery Agent",
            specialization="Battery life, power efficiency & portability",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class ExperienceAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="experience",
            name="Experience Agent",
            specialization="Display, build quality, keyboard & usability",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class FutureAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="futureProof",
            name="Future Agent",
            specialization="Longevity, upgradeability & future workload headroom",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class CameraAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="camera",
            name="Camera Agent",
            specialization="Optics, sensor size, low-light image processing & video stabilization",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class DisplayUXAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="display",
            name="Display & UX Agent",
            specialization="Screen resolution, refresh rate, outdoor peak nits & touch response",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class FitnessAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="fitness",
            name="Fitness & Health Agent",
            specialization="Biometric HR sensors, dual-band GPS accuracy & workout analytics",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


# =====================================================================
# 2. FINANCE AGENTS
# =====================================================================

class ReturnAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="returnPotential",
            name="Return Agent",
            specialization="Yield potential, CAGR, compounding rate & alpha generation",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class RiskAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="risk",
            name="Risk Agent",
            specialization="Drawdown risk, capital preservation & volatility hedge",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class LiquidityAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="liquidity",
            name="Liquidity Agent",
            specialization="Cash access speed, redemption ease & lock-in terms",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class StabilityAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="stability",
            name="Stability Agent",
            specialization="Valuation predictability, low variance & stress resilience",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class GrowthAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="growth",
            name="Growth Agent",
            specialization="Multi-year capital appreciation & inflation protection",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


# =====================================================================
# 3. CAREER AGENTS
# =====================================================================

class CompensationAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="salary",
            name="Compensation Agent",
            specialization="Base pay, equity upside, total benefits & market benchmark",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class SkillFitAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="skillFit",
            name="Skill-Fit Agent",
            specialization="Technical capability match, role responsibilities & daily ownership",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class CareerGrowthAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="growth",
            name="Growth Agent",
            specialization="Career trajectory, mentorship, promotion speed & resume impact",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class WorkLifeAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="workLifeBalance",
            name="Work-Life Agent",
            specialization="Hours sustainability, schedule flexibility & burnout prevention",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class CareerStabilityAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="stability",
            name="Stability Agent",
            specialization="Company runway, organizational tenure & employment safety",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


# =====================================================================
# 4. EDUCATION AGENTS
# =====================================================================

class AcademicAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="academicQuality",
            name="Academic Agent",
            specialization="Curriculum depth, faculty credentials & research facilities",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class CostAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="cost",
            name="Cost Agent",
            specialization="Total tuition, debt burden, scholarships & educational ROI",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class PlacementAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="placements",
            name="Placement Agent",
            specialization="Graduate placement rate, median salary & employer recruitment",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class CampusExperienceAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="experience",
            name="Experience Agent",
            specialization="Peer collaboration, campus life & student community",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class FutureOpportunityAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="futureOpportunity",
            name="Future Opportunity Agent",
            specialization="Global brand prestige, alumni leverage & career mobility",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


# =====================================================================
# 5. TRAVEL AGENTS
# =====================================================================

class BudgetAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="cost",
            name="Budget Agent",
            specialization="Travel expenses, lodging rates, transit & daily budget optimization",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class SafetyAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="safety",
            name="Safety Agent",
            specialization="Regional safety index, emergency healthcare & traveler security",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class TravelExperienceAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="experience",
            name="Experience Agent",
            specialization="Cultural immersion, cuisine, scenic vistas & comfort",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class ConvenienceAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="convenience",
            name="Convenience Agent",
            specialization="Transit duration, airport connectivity & routing friction",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class AttractionsAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="attractions",
            name="Attractions Agent",
            specialization="Historic landmarks, hiking trails & sightseeing density",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


# =====================================================================
# 6. SHOPPING AGENTS
# =====================================================================

class PriceAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="price",
            name="Price Agent",
            specialization="Competitive retail pricing, market discounts & budget fit",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class QualityAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="quality",
            name="Quality Agent",
            specialization="Materials, build craftsmanship & manufacturing standards",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class FeaturesAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="features",
            name="Features Agent",
            specialization="Ergonomic adjustability, versatility & everyday utility",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class ReviewAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="reviews",
            name="Review Agent",
            specialization="Verified buyer sentiment, long-term owner reviews & defects",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class DurabilityAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="durability",
            name="Durability Agent",
            specialization="Component lifespan, warranty coverage & wear resistance",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


# =====================================================================
# 7. OTHER / GENERIC AGENTS
# =====================================================================

class FitAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="optionFit",
            name="Fit Agent",
            specialization="Goal alignment, core values & strategic fit",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class GenericValueAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="value",
            name="Value Agent",
            specialization="Resource efficiency, economic return & cost balance",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class GenericRiskAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="risk",
            name="Risk Agent",
            specialization="Downside exposure, worst-case mitigation & reversibility",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class GenericExperienceAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="experience",
            name="Experience Agent",
            specialization="Qualitative lifestyle, daily comfort & satisfaction",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)


class FutureImpactAgent(BaseAgent):
    def __init__(self, provider: Optional[AIProvider] = None):
        super().__init__(
            id="longTermImpact",
            name="Future Impact Agent",
            specialization="Multi-year trajectory, durability & long-term compounding",
            provider=provider,
        )

    def analyze(self, decision: DecisionInputSchema) -> AgentResult:
        return self.provider.evaluate_dimension(self.id, self.name, self.specialization, decision)
