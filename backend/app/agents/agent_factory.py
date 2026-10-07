"""
Agent Factory for Decision Arena.
Dynamically maps category and subcategory dimensions to specialized candidate evaluation agents.
Agents evaluate candidates; agents are NOT candidates.
"""

from typing import List, Optional, Dict
from .base_agent import BaseCandidateAgent, BaseAgent
from .specialized import (
    # Electronics
    PerformanceAgent,
    BatteryAgent,
    DisplayAgent,
    BuildAgent,
    UpgradeabilityAgent,
    ValueAgent,
    CameraAgent,
    SoftwareAgent,
    HealthFitnessAgent,
    SmartFeaturesAgent,
    ComfortAgent,
    DurabilityAgent,
    CompatibilityAgent,
    PortabilityAgent,
    ProductivityAgent,
    SoundQualityAgent,
    NoiseCancellationAgent,
    ConnectivityAgent,
    # Finance
    ReturnPotentialAgent,
    RiskAgent,
    LiquidityAgent,
    StabilityAgent,
    GrowthAgent,
    InterestRateAgent,
    EMIAgent,
    TotalCostAgent,
    TenureAgent,
    FlexibilityAgent,
    EligibilityAgent,
    RewardsAgent,
    AnnualFeeAgent,
    BenefitsAgent,
    InterestChargesAgent,
    AcceptanceAgent,
    CoverageAgent,
    PremiumAgent,
    ClaimSupportAgent,
    ExclusionsAgent,
    ReliabilityAgent,
    LongTermValueAgent,
    # Career
    SalaryAgent,
    SkillFitAgent,
    CareerGrowthAgent,
    WorkLifeBalanceAgent,
    CareerStabilityAgent,
    LocationAgent,
    LearningAgent,
    # Vehicle
    VehicleSafetyAgent,
    VehicleMileageAgent,
    VehicleComfortAgent,
    VehicleSpaceAgent,
    VehiclePerformanceAgent,
    VehicleMaintenanceAgent,
    VehicleValueAgent,
    # Generic
    GenericFactorAgent,
)
from ..decision.factor_selector import get_decision_config
from .category_agents import (
    PerformanceAgent as LegacyPerformanceAgent,
    ValueAgent as LegacyValueAgent,
    BatteryAgent as LegacyBatteryAgent,
    ExperienceAgent as LegacyExperienceAgent,
    FutureAgent as LegacyFutureAgent,
    CameraAgent as LegacyCameraAgent,
    DisplayUXAgent as LegacyDisplayUXAgent,
    FitnessAgent as LegacyFitnessAgent,
    ReturnAgent as LegacyReturnAgent,
    RiskAgent as LegacyRiskAgent,
    LiquidityAgent as LegacyLiquidityAgent,
    StabilityAgent as LegacyStabilityAgent,
    GrowthAgent as LegacyGrowthAgent,
    CompensationAgent as LegacyCompensationAgent,
    SkillFitAgent as LegacySkillFitAgent,
    CareerGrowthAgent as LegacyCareerGrowthAgent,
    WorkLifeAgent as LegacyWorkLifeAgent,
    CareerStabilityAgent as LegacyCareerStabilityAgent,
    AcademicAgent as LegacyAcademicAgent,
    CostAgent as LegacyCostAgent,
    PlacementAgent as LegacyPlacementAgent,
    CampusExperienceAgent as LegacyCampusExperienceAgent,
    FutureOpportunityAgent as LegacyFutureOpportunityAgent,
    BudgetAgent as LegacyBudgetAgent,
    SafetyAgent as LegacySafetyAgent,
    TravelExperienceAgent as LegacyTravelExperienceAgent,
    ConvenienceAgent as LegacyConvenienceAgent,
    AttractionsAgent as LegacyAttractionsAgent,
    PriceAgent as LegacyPriceAgent,
    QualityAgent as LegacyQualityAgent,
    FeaturesAgent as LegacyFeaturesAgent,
    ReviewAgent as LegacyReviewAgent,
    DurabilityAgent as LegacyDurabilityAgent,
    FitAgent as LegacyFitAgent,
    GenericValueAgent as LegacyGenericValueAgent,
    GenericRiskAgent as LegacyGenericRiskAgent,
    GenericExperienceAgent as LegacyGenericExperienceAgent,
    FutureImpactAgent as LegacyFutureImpactAgent,
)
from ..services.ai_provider import AIProvider

# Mapping of factor keys to candidate-level specialized agents
FACTOR_AGENT_REGISTRY: Dict[str, type[BaseCandidateAgent]] = {
    # Electronics - Common & Laptop
    "performance": PerformanceAgent,
    "battery": BatteryAgent,
    "display": DisplayAgent,
    "build": BuildAgent,
    "upgradeability": UpgradeabilityAgent,
    "value": ValueAgent,
    # Smartphone
    "camera": CameraAgent,
    "software": SoftwareAgent,
    # Smartwatch
    "healthFitness": HealthFitnessAgent,
    "smartFeatures": SmartFeaturesAgent,
    "comfort": ComfortAgent,
    "durability": DurabilityAgent,
    "compatibility": CompatibilityAgent,
    # Tablet
    "portability": PortabilityAgent,
    "productivity": ProductivityAgent,
    # Headphones
    "soundQuality": SoundQualityAgent,
    "noiseCancellation": NoiseCancellationAgent,
    "connectivity": ConnectivityAgent,
    # Finance - Investment
    "returnPotential": ReturnPotentialAgent,
    "risk": RiskAgent,
    "liquidity": LiquidityAgent,
    "stability": StabilityAgent,
    "growth": GrowthAgent,
    # Finance - Loan
    "interestRate": InterestRateAgent,
    "emi": EMIAgent,
    "totalCost": TotalCostAgent,
    "tenure": TenureAgent,
    "flexibility": FlexibilityAgent,
    "eligibility": EligibilityAgent,
    # Finance - Credit Card
    "rewards": RewardsAgent,
    "annualFee": AnnualFeeAgent,
    "benefits": BenefitsAgent,
    "interestCharges": InterestChargesAgent,
    "acceptance": AcceptanceAgent,
    # Finance - Insurance
    "coverage": CoverageAgent,
    "premium": PremiumAgent,
    "claimSupport": ClaimSupportAgent,
    "exclusions": ExclusionsAgent,
    "reliability": ReliabilityAgent,
    "longTermValue": LongTermValueAgent,
    # Career
    "salary": SalaryAgent,
    "skillFit": SkillFitAgent,
    "workLifeBalance": WorkLifeBalanceAgent,
    "location": LocationAgent,
    "learning": LearningAgent,
    "demand": CareerGrowthAgent,
    "salaryPotential": SalaryAgent,
    "learningCurve": LearningAgent,
}

VEHICLE_AGENT_REGISTRY: Dict[str, type[BaseCandidateAgent]] = {
    "safety": VehicleSafetyAgent,
    "mileage": VehicleMileageAgent,
    "comfort": VehicleComfortAgent,
    "space": VehicleSpaceAgent,
    "performance": VehiclePerformanceAgent,
    "maintenance": VehicleMaintenanceAgent,
    "value": VehicleValueAgent,
}


def get_specialized_agents(
    category: str,
    subcategory: Optional[str] = None,
) -> List[BaseCandidateAgent]:
    """
    Candidate Evaluation Agent Factory:
    Dynamically returns the specialized agents for the given subcategory.
    Each agent evaluates candidates along one factor dimension.
    """
    cat = (category or "").strip().lower()
    sub_config = get_decision_config(category, subcategory)
    agents: List[BaseCandidateAgent] = []

    for factor_def in sub_config.factors:
        agent_cls = None
        if cat in {"vehicle", "automotive", "transportation"}:
            agent_cls = VEHICLE_AGENT_REGISTRY.get(factor_def.key)
        if not agent_cls:
            agent_cls = FACTOR_AGENT_REGISTRY.get(factor_def.key)

        if agent_cls:
            agents.append(agent_cls())
        else:
            agents.append(GenericFactorAgent(agent_name=factor_def.name, factor_key=factor_def.key))

    return agents


def get_agents_for_category(
    category: str,
    subcategory: Optional[str] = None,
    provider: Optional[AIProvider] = None,
) -> List[BaseAgent]:
    """
    Backward-compatible category-level agent factory.
    Returns 5 high-level agents for the decision overview cards in UI.
    """
    cat = (category or "electronics").strip().lower()
    sub = (subcategory or "").strip().lower()

    if cat == "vehicle":
        return [
            LegacySafetyAgent(provider=provider),
            LegacyBudgetAgent(provider=provider),
            LegacyTravelExperienceAgent(provider=provider),
            LegacyConvenienceAgent(provider=provider),
            LegacyGenericValueAgent(provider=provider),
        ]
    elif cat == "finance":
        return [
            LegacyReturnAgent(provider=provider),
            LegacyRiskAgent(provider=provider),
            LegacyLiquidityAgent(provider=provider),
            LegacyStabilityAgent(provider=provider),
            LegacyGrowthAgent(provider=provider),
        ]
    elif cat == "career":
        return [
            LegacyCompensationAgent(provider=provider),
            LegacySkillFitAgent(provider=provider),
            LegacyCareerGrowthAgent(provider=provider),
            LegacyWorkLifeAgent(provider=provider),
            LegacyCareerStabilityAgent(provider=provider),
        ]
    elif cat == "education":
        return [
            LegacyAcademicAgent(provider=provider),
            LegacyCostAgent(provider=provider),
            LegacyPlacementAgent(provider=provider),
            LegacyCampusExperienceAgent(provider=provider),
            LegacyFutureOpportunityAgent(provider=provider),
        ]
    elif cat == "travel":
        return [
            LegacyBudgetAgent(provider=provider),
            LegacySafetyAgent(provider=provider),
            LegacyTravelExperienceAgent(provider=provider),
            LegacyConvenienceAgent(provider=provider),
            LegacyAttractionsAgent(provider=provider),
        ]
    elif cat == "shopping":
        return [
            LegacyPriceAgent(provider=provider),
            LegacyQualityAgent(provider=provider),
            LegacyFeaturesAgent(provider=provider),
            LegacyReviewAgent(provider=provider),
            LegacyDurabilityAgent(provider=provider),
        ]
    elif cat == "electronics":
        if sub == "smartphone":
            return [
                LegacyCameraAgent(provider=provider),
                LegacyBatteryAgent(provider=provider),
                LegacyPerformanceAgent(provider=provider),
                LegacyDisplayUXAgent(provider=provider),
                LegacyValueAgent(provider=provider),
            ]
        elif sub == "smartwatch":
            return [
                LegacyFitnessAgent(provider=provider),
                LegacyBatteryAgent(provider=provider),
                LegacyDurabilityAgent(provider=provider),
                LegacyDisplayUXAgent(provider=provider),
                LegacyValueAgent(provider=provider),
            ]
        else:
            return [
                LegacyPerformanceAgent(provider=provider),
                LegacyValueAgent(provider=provider),
                LegacyBatteryAgent(provider=provider),
                LegacyExperienceAgent(provider=provider),
                LegacyFutureAgent(provider=provider),
            ]
    else:
        return [
            LegacyFitAgent(provider=provider),
            LegacyGenericValueAgent(provider=provider),
            LegacyGenericRiskAgent(provider=provider),
            LegacyGenericExperienceAgent(provider=provider),
            LegacyFutureImpactAgent(provider=provider),
        ]
