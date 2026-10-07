"""
Centralized Category Configuration System for Decision Arena.
Defines modular domain rules, evaluation factors, default weights, and criteria.
"""

from typing import Dict, List, Any, Optional, Tuple
from pydantic import BaseModel, Field

class FactorDefinition(BaseModel):
    key: str
    name: str
    description: str
    defaultWeight: float = 20.0

class SubcategoryConfig(BaseModel):
    id: str
    label: str
    description: str
    candidateType: str
    factors: List[FactorDefinition]
    commonRequirements: List[str] = Field(default_factory=list)
    commonDealBreakers: List[str] = Field(default_factory=list)

class CategoryConfig(BaseModel):
    id: str
    label: str
    description: str
    defaultSubcategory: str
    subcategories: Dict[str, SubcategoryConfig]

DECISION_CONFIG: Dict[str, CategoryConfig] = {
    # =========================================================================
    # ELECTRONICS
    # =========================================================================
    "electronics": CategoryConfig(
        id="electronics",
        label="Electronics",
        description="Compute gadgets, mobile devices, hardware, and accessories",
        defaultSubcategory="laptop",
        subcategories={
            "laptop": SubcategoryConfig(
                id="laptop",
                label="Laptop",
                description="Laptops, ultrabooks, mobile workstations, and MacBooks",
                candidateType="laptop",
                factors=[
                    FactorDefinition(key="performance", name="Performance", description="Compute throughput, CPU, GPU, speed & multitasking", defaultWeight=25.0),
                    FactorDefinition(key="battery", name="Battery", description="Battery endurance, power efficiency & mobility runtime", defaultWeight=15.0),
                    FactorDefinition(key="display", name="Display", description="Resolution, color accuracy, refresh rate & brightness", defaultWeight=15.0),
                    FactorDefinition(key="build", name="Build Quality", description="Chassis materials, thermals, ergonomics & durability", defaultWeight=15.0),
                    FactorDefinition(key="upgradeability", name="Upgradeability", description="RAM/SSD expansion slots, ports & future headroom", defaultWeight=15.0),
                    FactorDefinition(key="value", name="Price / Value", description="Component value per price & budget alignment", defaultWeight=15.0),
                ],
                commonRequirements=["16GB RAM minimum", "Dedicated GPU", "FHD IPS display", "Good battery life"],
                commonDealBreakers=["Thermal overheating", "Less than 16GB RAM", "Poor display under 250 nits"],
            ),
            "smartphone": SubcategoryConfig(
                id="smartphone",
                label="Smartphone",
                description="Smartphones, camera phones, Android flagships & iPhones",
                candidateType="smartphone",
                factors=[
                    FactorDefinition(key="performance", name="Performance", description="SoC processor speed, gaming FPS & multitasking RAM", defaultWeight=20.0),
                    FactorDefinition(key="camera", name="Camera", description="Primary sensor size, OIS, low-light imaging & video stabilization", defaultWeight=25.0),
                    FactorDefinition(key="battery", name="Battery", description="Screen-on time endurance & fast-charging speed", defaultWeight=20.0),
                    FactorDefinition(key="display", name="Display", description="AMOLED clarity, 120Hz refresh rate & outdoor sunlight nits", defaultWeight=15.0),
                    FactorDefinition(key="software", name="Software & Updates", description="OS smoothness, update tenure & clean UI without bloatware", defaultWeight=10.0),
                    FactorDefinition(key="build", name="Build & Design", description="Ergonomics, water resistance rating & finish", defaultWeight=5.0),
                    FactorDefinition(key="value", name="Price / Value", description="Feature density per rupee & warranty coverage", defaultWeight=5.0),
                ],
                commonRequirements=["50MP OIS camera", "120Hz AMOLED display", "5000mAh battery", "Fast charging"],
                commonDealBreakers=["Slow charging under 25W", "Bloatware ads", "Short OS support"],
            ),
            "tablet": SubcategoryConfig(
                id="tablet",
                label="Tablet",
                description="iPads, Android tablets, and drawing workstations",
                candidateType="tablet",
                factors=[
                    FactorDefinition(key="performance", name="Performance", description="Chipset speed, multitasking & creative rendering", defaultWeight=25.0),
                    FactorDefinition(key="display", name="Display", description="Screen resolution, aspect ratio & stylus input latency", defaultWeight=20.0),
                    FactorDefinition(key="battery", name="Battery Life", description="Video streaming & note-taking endurance", defaultWeight=15.0),
                    FactorDefinition(key="portability", name="Portability", description="Slim thickness, lightweight chassis & easy mobility", defaultWeight=15.0),
                    FactorDefinition(key="software", name="Software Ecosystem", description="Tablet-optimized apps, stylus features & OS updates", defaultWeight=10.0),
                    FactorDefinition(key="productivity", name="Productivity", description="External keyboard support & desktop multi-window mode", defaultWeight=10.0),
                    FactorDefinition(key="value", name="Price / Value", description="In-box accessories, price-to-spec ratio", defaultWeight=5.0),
                ],
                commonRequirements=["Stylus pen support", "High resolution display", "All-day battery"],
                commonDealBreakers=["Poor app optimization", "Severe thermal throttling"],
            ),
            "smartwatch": SubcategoryConfig(
                id="smartwatch",
                label="Smartwatch",
                description="Fitness trackers, GPS sports wearables & smartwatches",
                candidateType="smartwatch",
                factors=[
                    FactorDefinition(key="healthFitness", name="Health & Fitness", description="GPS accuracy, optical HR precision, HRV & workout tracking", defaultWeight=30.0),
                    FactorDefinition(key="battery", name="Battery Life", description="Multi-day runtime, GPS duration & standby efficiency", defaultWeight=25.0),
                    FactorDefinition(key="smartFeatures", name="Smart Features", description="Bluetooth calls, app ecosystem, contactless payments & music", defaultWeight=15.0),
                    FactorDefinition(key="comfort", name="Comfort & Weight", description="Wrist fit, strap comfort & 24/7 sleep tracking wearability", defaultWeight=10.0),
                    FactorDefinition(key="durability", name="Durability", description="Water resistance (5 ATM), glass scratch resistance & ruggedness", defaultWeight=10.0),
                    FactorDefinition(key="compatibility", name="Compatibility", description="Cross-platform Android/iOS pairing & ecosystem sync", defaultWeight=5.0),
                    FactorDefinition(key="value", name="Price / Value", description="Zero mandatory subscriptions & feature value", defaultWeight=5.0),
                ],
                commonRequirements=["Accurate HR sensor", "5 ATM water resistance", "Multi-day battery"],
                commonDealBreakers=["Mandatory paid subscription", "Battery under 24 hours"],
            ),
            "headphones": SubcategoryConfig(
                id="headphones",
                label="Headphones",
                description="Over-ear headphones, ANC wireless earbuds & audiophile cans",
                candidateType="headphones",
                factors=[
                    FactorDefinition(key="soundQuality", name="Sound Quality", description="Acoustic clarity, bass response, soundstage & codec support", defaultWeight=30.0),
                    FactorDefinition(key="noiseCancellation", name="Active Noise Cancellation", description="ANC attenuation, transparency mode & wind resistance", defaultWeight=25.0),
                    FactorDefinition(key="battery", name="Battery Life", description="Playback hours per charge & fast recharge speed", defaultWeight=15.0),
                    FactorDefinition(key="comfort", name="Comfort & Fit", description="Ear cushion pressure, weight & long-session ergonomics", defaultWeight=15.0),
                    FactorDefinition(key="connectivity", name="Connectivity", description="Bluetooth multipoint, low latency & codec stability", defaultWeight=5.0),
                    FactorDefinition(key="durability", name="Durability & Build", description="Sweat resistance, headband hinge strength & case build", defaultWeight=5.0),
                    FactorDefinition(key="value", name="Price / Value", description="Sound-per-rupee ratio & bundled accessories", defaultWeight=5.0),
                ],
                commonRequirements=["Active noise cancellation", "Long battery life", "Bluetooth multipoint"],
                commonDealBreakers=["Muddy muffled sound", "Uncomfortable ear pressure"],
            ),
        },
    ),

    # =========================================================================
    # VEHICLE / TRANSPORTATION
    # =========================================================================
    "vehicle": CategoryConfig(
        id="vehicle",
        label="Vehicle",
        description="Cars, sedans, SUVs, minivans, and motorcycles",
        defaultSubcategory="vehicle",
        subcategories={
            "vehicle": SubcategoryConfig(
                id="vehicle",
                label="Vehicle",
                description="Passenger cars, sedans, crossovers, SUVs, and minivans",
                candidateType="vehicle",
                factors=[
                    FactorDefinition(key="safety", name="Safety", description="Crash ratings, active ADAS, airbags & brake assist", defaultWeight=25.0),
                    FactorDefinition(key="mileage", name="Mileage & Fuel Efficiency", description="Highway/city MPG, hybrid range, and running cost", defaultWeight=20.0),
                    FactorDefinition(key="comfort", name="Ride Comfort", description="Cabin insulation, suspension dampening & ergonomic seating", defaultWeight=15.0),
                    FactorDefinition(key="space", name="Cabin & Cargo Space", description="Passenger legroom, trunk capacity, and seat folding utility", defaultWeight=15.0),
                    FactorDefinition(key="performance", name="Performance & Drivetrain", description="Horsepower, torque, transmission response & road handling", defaultWeight=10.0),
                    FactorDefinition(key="maintenance", name="Maintenance & Reliability", description="Expected service interval, parts availability & warranty", defaultWeight=10.0),
                    FactorDefinition(key="value", name="Price / Value", description="Resale projection, standard equipment vs base price", defaultWeight=5.0),
                ],
                commonRequirements=["High safety rating", "Reliable transmission", "Spacious seating"],
                commonDealBreakers=["Poor crash rating", "Frequent mechanical recalls"],
            ),
            "motorcycle": SubcategoryConfig(
                id="motorcycle",
                label="Motorcycle",
                description="Street bikes, sportbikes, cruisers, and commuter two-wheelers",
                candidateType="motorcycle",
                factors=[
                    FactorDefinition(key="mileage", name="Fuel Economy", description="Kilometers per liter and highway fuel efficiency", defaultWeight=25.0),
                    FactorDefinition(key="performance", name="Engine Performance", description="Displacement, acceleration, torque band & speed", defaultWeight=25.0),
                    FactorDefinition(key="comfort", name="Ergonomics & Seating", description="Riding posture, seat cushioning & vibration control", defaultWeight=15.0),
                    FactorDefinition(key="safety", name="Braking & Safety", description="Dual-channel ABS, traction control & headlight throw", defaultWeight=15.0),
                    FactorDefinition(key="maintenance", name="Maintenance", description="Service costs, spares availability & reliability", defaultWeight=10.0),
                    FactorDefinition(key="value", name="Price / Value", description="Price-to-displacement ratio & resale value", defaultWeight=10.0),
                ],
                commonRequirements=["Dual-channel ABS", "Good fuel efficiency"],
                commonDealBreakers=["Severe vibration at cruising speed"],
            ),
        },
    ),

    # =========================================================================
    # FINANCE
    # =========================================================================
    "finance": CategoryConfig(
        id="finance",
        label="Finance",
        description="Investments, credit products, loans, and portfolio planning",
        defaultSubcategory="investment",
        subcategories={
            "investment": SubcategoryConfig(
                id="investment",
                label="Investment",
                description="Mutual funds, index baskets, sovereign bonds, and equity",
                candidateType="investment",
                factors=[
                    FactorDefinition(key="returnPotential", name="Return Potential", description="Expected annualized returns & compounding upside", defaultWeight=25.0),
                    FactorDefinition(key="risk", name="Risk Assessment", description="Downside exposure, capital preservation & volatility tolerance", defaultWeight=25.0),
                    FactorDefinition(key="liquidity", name="Liquidity", description="Ease of redemption, settlement turnaround & lock-in terms", defaultWeight=20.0),
                    FactorDefinition(key="stability", name="Stability", description="Predictability, low variance & stress resilience", defaultWeight=15.0),
                    FactorDefinition(key="growth", name="Long-Term Growth", description="Multi-year capital compounding & inflation defense", defaultWeight=15.0),
                ],
                commonRequirements=["CAGR above 12%", "Downside risk protection", "Zero punitive lock-in"],
                commonDealBreakers=["Permanent capital loss", "High management fee drag"],
            ),
            "loan": SubcategoryConfig(
                id="loan",
                label="Loan",
                description="Home loans, personal loans, and debt financing",
                candidateType="loan",
                factors=[
                    FactorDefinition(key="interestRate", name="Interest Rate", description="Effective annual percentage rate & benchmark spread", defaultWeight=30.0),
                    FactorDefinition(key="emi", name="EMI Affordability", description="Monthly repayment burden relative to net cash flow", defaultWeight=25.0),
                    FactorDefinition(key="totalCost", name="Total Cost of Borrowing", description="Processing fees, documentation & cumulative interest", defaultWeight=20.0),
                    FactorDefinition(key="tenure", name="Tenure Flexibility", description="Repayment schedule adaptability & prepayment clauses", defaultWeight=15.0),
                    FactorDefinition(key="eligibility", name="Eligibility & Speed", description="Approval turnaround, documentation ease & criteria", defaultWeight=10.0),
                ],
                commonRequirements=["Low interest rate", "Zero prepayment penalty"],
                commonDealBreakers=["Hidden processing fees"],
            ),
        },
    ),

    # =========================================================================
    # CAREER
    # =========================================================================
    "career": CategoryConfig(
        id="career",
        label="Career",
        description="Job offers, career transitions, and professional growth tracks",
        defaultSubcategory="job",
        subcategories={
            "job": SubcategoryConfig(
                id="job",
                label="Job Offer",
                description="Comparing concrete job offers, compensation, and team culture",
                candidateType="job",
                factors=[
                    FactorDefinition(key="salary", name="Salary & Compensation", description="Base pay, equity/stock upside, bonuses & benefits package", defaultWeight=25.0),
                    FactorDefinition(key="skillFit", name="Skill Fit & Relevance", description="Alignment with core technical skills, passion & autonomy", defaultWeight=20.0),
                    FactorDefinition(key="growth", name="Career Growth", description="Promotion runway, leadership opportunities & mentorship density", defaultWeight=20.0),
                    FactorDefinition(key="workLifeBalance", name="Work-Life Balance", description="Predictable hours, remote flexibility & burnout prevention", defaultWeight=15.0),
                    FactorDefinition(key="stability", name="Company Stability", description="Financial runway, market defensibility & job security", defaultWeight=10.0),
                    FactorDefinition(key="learning", name="Learning Curve", description="Exposure to cutting-edge technologies & domain depth", defaultWeight=10.0),
                ],
                commonRequirements=["Competitive equity & base", "Modern tech stack"],
                commonDealBreakers=["Toxic work culture", "Severe crunch overtime"],
            ),
        },
    ),
    "education": CategoryConfig(
        id="education",
        label="Education",
        description="Compare universities, degrees, certifications, and research programs",
        defaultSubcategory="program",
        subcategories={
            "program": SubcategoryConfig(
                id="program",
                label="Education Program",
                description="Universities, degrees, online certifications, and research programs",
                candidateType="education",
                factors=[
                    FactorDefinition(key="academicQuality", name="Academic Quality", description="Curriculum depth, research labs, syllabus rigor, and faculty", defaultWeight=20.0),
                    FactorDefinition(key="cost", name="Cost", description="Tuition fees, living expenses, scholarships, and educational ROI", defaultWeight=20.0),
                    FactorDefinition(key="placements", name="Placements", description="Campus recruitment, graduate salaries, and employer network", defaultWeight=20.0),
                    FactorDefinition(key="experience", name="Campus Experience", description="Peer community, campus environment, and collaborative culture", defaultWeight=20.0),
                    FactorDefinition(key="futureOpportunity", name="Future Opportunity", description="Degree prestige, alumni network, and career mobility", defaultWeight=20.0),
                ],
                commonRequirements=["Recognized accreditation", "Strong graduate outcomes"],
                commonDealBreakers=["Unaccredited program", "Unmanageable total cost"],
            ),
        },
    ),
    "travel": CategoryConfig(
        id="travel",
        label="Travel",
        description="Compare destinations, vacation packages, transit routes, and itineraries",
        defaultSubcategory="trip",
        subcategories={
            "trip": SubcategoryConfig(
                id="trip",
                label="Trip",
                description="Destinations, vacation packages, transit routes, and itineraries",
                candidateType="travel",
                factors=[
                    FactorDefinition(key="cost", name="Budget / Cost", description="Transport, lodging, daily expenses, and total spend", defaultWeight=20.0),
                    FactorDefinition(key="safety", name="Safety", description="Regional security, emergency services, and traveler reassurance", defaultWeight=20.0),
                    FactorDefinition(key="experience", name="Experience", description="Local cuisine, scenery, hospitality, and lasting memories", defaultWeight=20.0),
                    FactorDefinition(key="convenience", name="Convenience", description="Visa ease, transit logistics, travel times, and accessibility", defaultWeight=20.0),
                    FactorDefinition(key="attractions", name="Attractions", description="Sightseeing, landmarks, culture, and excursions", defaultWeight=20.0),
                ],
                commonRequirements=["Stay within trip budget", "Safe accommodation and transport"],
                commonDealBreakers=["Active travel warning", "Unsafe accommodation"],
            ),
        },
    ),
    "shopping": CategoryConfig(
        id="shopping",
        label="Shopping",
        description="Compare consumer products, appliances, tools, and lifestyle purchases",
        defaultSubcategory="product",
        subcategories={
            "product": SubcategoryConfig(
                id="product",
                label="Product",
                description="Consumer products, appliances, tools, and lifestyle purchases",
                candidateType="shopping",
                factors=[
                    FactorDefinition(key="price", name="Price", description="Upfront retail cost, discounts, and price competitiveness", defaultWeight=20.0),
                    FactorDefinition(key="quality", name="Quality", description="Material grade, build precision, and finish standard", defaultWeight=20.0),
                    FactorDefinition(key="features", name="Features", description="Functional capabilities, specifications, and versatility", defaultWeight=20.0),
                    FactorDefinition(key="reviews", name="Reviews", description="User ratings, community consensus, and reputation", defaultWeight=20.0),
                    FactorDefinition(key="durability", name="Durability", description="Product lifespan, warranty coverage, and wear resistance", defaultWeight=20.0),
                ],
                commonRequirements=["Fits intended use", "Available warranty coverage"],
                commonDealBreakers=["Known safety defect", "No warranty coverage"],
            ),
        },
    ),
    "other": CategoryConfig(
        id="other",
        label="Other",
        description="Custom and general strategic decisions",
        defaultSubcategory="general",
        subcategories={
            "general": SubcategoryConfig(
                id="general",
                label="General Decision",
                description="Custom and general strategic decisions",
                candidateType="general",
                factors=[
                    FactorDefinition(key="optionFit", name="Strategic Fit", description="Alignment with core goals and personal values", defaultWeight=20.0),
                    FactorDefinition(key="value", name="Cost / Value", description="Financial implications, budget, and return on investment", defaultWeight=20.0),
                    FactorDefinition(key="risk", name="Risk", description="Downside consequences, uncertainty, and reversibility", defaultWeight=20.0),
                    FactorDefinition(key="experience", name="Experience", description="Day-to-day satisfaction, lifestyle impact, and well-being", defaultWeight=20.0),
                    FactorDefinition(key="longTermImpact", name="Long-term Impact", description="Strategic trajectory and multi-year outlook", defaultWeight=20.0),
                ],
                commonRequirements=["Supports stated goals", "Manageable downside risk"],
                commonDealBreakers=["Irreversible severe downside", "Unacceptable ongoing cost"],
            ),
        },
    ),
}
