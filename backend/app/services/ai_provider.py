from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from ..core.config import settings
from ..schemas.decision import DecisionInputSchema
from ..schemas.agent import AgentResult

class AIProvider(ABC):
    """
    Abstract AI Provider Interface.
    Enables swappable intelligence backends (Mock, OpenAI, Gemini, Claude, Ollama)
    without modifying the multi-agent orchestration architecture or agent definitions.
    """

    @abstractmethod
    def evaluate_dimension(
        self,
        agent_id: str,
        agent_name: str,
        specialization: str,
        decision: DecisionInputSchema,
    ) -> AgentResult:
        """
        Produce a structured evaluation for an agent dimension.
        Returns AgentResult without exposing chain-of-thought.
        """
        pass


class MockAIProvider(AIProvider):
    """
    Deterministic category-aware mock AI provider.
    Delivers domain-tailored structured evaluations for every supported category and agent.
    Never exposes internal chain-of-thought or hardware terms across non-hardware domains.
    """

    # Comprehensive evaluation catalog keyed by (category, agent_id)
    EVALUATION_CATALOG: Dict[str, Dict[str, Dict[str, Any]]] = {
        # 1. ELECTRONICS
        "electronics": {
            "performance": {
                "score": 92.0,
                "strengths": [
                    "High compute throughput suitable for intensive development workflows",
                    "Easily handles local data modeling, Docker, and multi-core compilation",
                    "Exceeds minimum RAM and processor benchmarks for AI/ML prototyping",
                ],
                "concerns": [
                    "Dedicated GPU may increase power usage under peak sustained workloads",
                ],
                "conclusion": "Strong choice for coding and AI/ML workloads.",
                "factors": ["CPU performance", "RAM capacity", "GPU capability", "Multitasking", "Compute throughput"],
            },
            "value": {
                "score": 86.0,
                "strengths": [
                    "Exceptional performance per price ratio in this budget bracket",
                    "Comes comfortably within the defined budget ceiling with good feature density",
                    "High component value compared to competing market alternatives",
                ],
                "concerns": [
                    "Minor budget compromises on secondary chassis finish and port selections",
                ],
                "conclusion": "Outstanding price-to-performance ratio within the defined budget.",
                "factors": ["Price-to-spec ratio", "Component value", "Budget fit", "Feature density"],
            },
            "battery": {
                "score": 81.0,
                "strengths": [
                    "Solid 6–8 hour battery life during general coding and web browsing",
                    "Fast-charging profile recovers 60% capacity in under 45 minutes",
                    "Excellent energy efficiency in low-power idle states",
                ],
                "concerns": [
                    "Heavy AI/ML execution significantly accelerates battery drain away from the wall",
                ],
                "conclusion": "Adequate mobility, but heavy AI/ML compute will require AC power.",
                "factors": ["Battery endurance", "Power efficiency", "Portability", "Idle power draw"],
            },
            "experience": {
                "score": 90.0,
                "strengths": [
                    "High-resolution anti-glare display minimizes eye fatigue during long sessions",
                    "Ergonomic tactile keyboard with crisp key travel ideal for developers",
                    "Low acoustic fan resonance under everyday productivity tasks",
                ],
                "concerns": [
                    "Built-in speakers and webcam are standard quality rather than studio grade",
                ],
                "conclusion": "Top-tier ergonomics and daily tactile comfort for continuous work.",
                "factors": ["Display clarity", "Tactile keyboard", "Acoustic noise", "Chassis ergonomics"],
            },
            "futureProof": {
                "score": 86.0,
                "strengths": [
                    "Modern I/O connectivity and latest Wi-Fi standards ensure protocol longevity",
                    "Reliable manufacturer driver and firmware update roadmap",
                    "Thermal stability preserves component lifespan across 3–4 years",
                ],
                "concerns": [
                    "Fixed memory configuration restricts upgrade options if ML model sizes double in 3 years",
                ],
                "conclusion": "Reliable multi-year longevity with moderate hardware upgrade paths.",
                "factors": ["Longevity", "Upgradeability", "Future workload headroom", "Thermal headroom"],
            },
        },
        "electronics:laptop": {
            "performance": {
                "score": 92.0,
                "strengths": [
                    "High compute throughput suitable for intensive development workflows",
                    "Easily handles local data modeling, Docker, and multi-core compilation",
                    "Exceeds minimum RAM and processor benchmarks for AI/ML prototyping",
                ],
                "concerns": [
                    "Dedicated GPU may increase power usage under peak sustained workloads",
                ],
                "conclusion": "Strong choice for coding and AI/ML workloads.",
                "factors": ["CPU performance", "RAM capacity", "GPU capability", "Multitasking", "Compute throughput"],
            },
            "value": {
                "score": 86.0,
                "strengths": [
                    "Exceptional performance per price ratio in this budget bracket",
                    "Comes comfortably within the defined budget ceiling with good feature density",
                    "High component value compared to competing market alternatives",
                ],
                "concerns": [
                    "Minor budget compromises on secondary chassis finish and port selections",
                ],
                "conclusion": "Outstanding price-to-performance ratio within the defined budget.",
                "factors": ["Price-to-spec ratio", "Component value", "Budget fit", "Feature density"],
            },
            "battery": {
                "score": 81.0,
                "strengths": [
                    "Solid 6–8 hour battery life during general coding and web browsing",
                    "Fast-charging profile recovers 60% capacity in under 45 minutes",
                    "Excellent energy efficiency in low-power idle states",
                ],
                "concerns": [
                    "Heavy AI/ML execution significantly accelerates battery drain away from the wall",
                ],
                "conclusion": "Adequate mobility, but heavy AI/ML compute will require AC power.",
                "factors": ["Battery endurance", "Power efficiency", "Portability", "Idle power draw"],
            },
            "experience": {
                "score": 90.0,
                "strengths": [
                    "High-resolution anti-glare display minimizes eye fatigue during long sessions",
                    "Ergonomic tactile keyboard with crisp key travel ideal for developers",
                    "Low acoustic fan resonance under everyday productivity tasks",
                ],
                "concerns": [
                    "Built-in speakers and webcam are standard quality rather than studio grade",
                ],
                "conclusion": "Top-tier ergonomics and daily tactile comfort for continuous work.",
                "factors": ["Display clarity", "Tactile keyboard", "Acoustic noise", "Chassis ergonomics"],
            },
            "futureProof": {
                "score": 86.0,
                "strengths": [
                    "Modern I/O connectivity and latest Wi-Fi standards ensure protocol longevity",
                    "Reliable manufacturer driver and firmware update roadmap",
                    "Thermal stability preserves component lifespan across 3–4 years",
                ],
                "concerns": [
                    "Fixed memory configuration restricts upgrade options if ML model sizes double in 3 years",
                ],
                "conclusion": "Reliable multi-year longevity with moderate hardware upgrade paths.",
                "factors": ["Longevity", "Upgradeability", "Future workload headroom", "Thermal headroom"],
            },
        },
        "electronics:smartphone": {
            "camera": {
                "score": 91.0,
                "strengths": [
                    "50MP Sony main sensor with OIS produces razor-sharp low-light stills",
                    "Natural color reproduction and high dynamic range in outdoor daylight",
                    "4K 60fps video capture with smooth gyro-EIS stabilization",
                ],
                "concerns": [
                    "Ultra-wide secondary lens has softer edge sharpness in dim lighting",
                ],
                "conclusion": "Superb flagship-grade camera system for photography and content creation.",
                "factors": ["Main sensor size", "OIS stabilization", "Low-light imaging", "Dynamic range", "Video bitrate"],
            },
            "battery": {
                "score": 87.0,
                "strengths": [
                    "5,500mAh cell easily delivers 7.5+ hours of active screen-on time",
                    "100W fast charging achieves 0 to 100% in under 28 minutes",
                    "Intelligent power management minimizes background standby drain",
                ],
                "concerns": [
                    "Lack of wireless charging support in this specific trim",
                ],
                "conclusion": "All-day endurance with class-leading fast recharge speeds.",
                "factors": ["Screen-on time", "Recharge speed", "Standby efficiency", "Battery health management"],
            },
            "performance": {
                "score": 93.0,
                "strengths": [
                    "Snapdragon 8 Gen 2 chipset provides blazing app launches and multitasking",
                    "Vapor chamber cooling ensures sustained 60fps frame rates in gaming",
                    "16GB LPDDR5X RAM keeps 15+ apps resident in memory without reload",
                ],
                "concerns": [
                    "Peak sustained compute throttles slightly during prolonged 4K export",
                ],
                "conclusion": "Blazing fast performance with top-tier thermal dissipation.",
                "factors": ["SoC compute power", "Vapor chamber cooling", "RAM speed & capacity", "App launch latency"],
            },
            "display": {
                "score": 92.0,
                "strengths": [
                    "1.5K 120Hz LTPO 4.0 AMOLED panel with dynamic refresh rate adaptation",
                    "Peak brightness of 4,500 nits provides crystal-clear outdoor sunlight visibility",
                    "2160Hz high-frequency PWM dimming eliminates eye strain in the dark",
                ],
                "concerns": [
                    "Curved screen edge may lead to occasional accidental palm touches",
                ],
                "conclusion": "Gorgeous LTPO display with industry-leading outdoor brightness.",
                "factors": ["LTPO refresh rate", "Peak nits brightness", "Color gamut (DCI-P3)", "Touch sampling rate"],
            },
            "value": {
                "score": 90.0,
                "strengths": [
                    "Flagship-level processor and camera at a sub-flagship price tier",
                    "Includes 100W power adapter and protective case in the box",
                    "Comprehensive 3-year OS upgrade and 4-year security patch commitment",
                ],
                "concerns": [
                    "No official IP68 rating, only splash-resistant IP64",
                ],
                "conclusion": "Incredible value-for-money flagship killer in the current market.",
                "factors": ["Price-to-spec ratio", "In-box accessories", "Software support lifecycle", "Resale value"],
            },
        },
        "electronics:smartwatch": {
            "fitness": {
                "score": 92.0,
                "strengths": [
                    "Dual-band multi-constellation GPS locks coordinates in under 5 seconds",
                    "4th-gen optical HR sensor achieves 98.5% correlation with medical chest straps",
                    "Rich training metrics including HRV status, VO2 Max, and training readiness",
                ],
                "concerns": [
                    "ECG functionality requires regional health authority approval in some areas",
                ],
                "conclusion": "Outstanding biometric and GPS tracking accuracy for athletes and runners.",
                "factors": ["Dual-band GPS", "Heart-rate sensor accuracy", "HRV & VO2 Max", "Sleep stage tracking"],
            },
            "battery": {
                "score": 94.0,
                "strengths": [
                    "Exceptional 11-day battery life in smartwatch mode without recharging",
                    "Over 19 hours of continuous GPS activity tracking on a single charge",
                    "Proprietary power saving profiles ensure zero battery anxiety on trips",
                ],
                "concerns": [
                    "Proprietary magnetic charging puck instead of universal Qi wireless charging",
                ],
                "conclusion": "Phenomenal multi-day battery endurance that eliminates daily recharge routines.",
                "factors": ["Smartwatch mode runtime", "GPS tracking endurance", "Standby drain", "Charge speed"],
            },
            "durability": {
                "score": 90.0,
                "strengths": [
                    "5 ATM water resistance rated for swimming, surfing, and open-water workouts",
                    "Reinforced fiber polymer bezel and Corning Gorilla Glass 3 display crystal",
                    "Tested against thermal shock and sweat corrosion under high intensity use",
                ],
                "concerns": [
                    "Polymer casing lacks the luxury jewelry finish of stainless steel or titanium",
                ],
                "conclusion": "Rugged and sweat-resistant build tailored for intense athletics.",
                "factors": ["Water resistance (5 ATM)", "Impact resistance", "Sweat & corrosion proofing", "Display glass hardness"],
            },
            "display": {
                "score": 88.0,
                "strengths": [
                    "Vibrant 1.2-inch AMOLED touchscreen with deep blacks and rich colors",
                    "Automatic ambient brightness sensor adjusts seamlessly between direct sun and dark rooms",
                    "Responsive wrist-raise wake gesture with optional Always-On Display mode",
                ],
                "concerns": [
                    "Always-On mode reduces total battery life from 11 days down to 5 days",
                ],
                "conclusion": "Bright, vivid AMOLED screen easily readable under direct sunlight.",
                "factors": ["AMOLED contrast", "Sunlight legibility", "Touch responsiveness", "Always-On Display efficiency"],
            },
            "value": {
                "score": 89.0,
                "strengths": [
                    "Delivers pro-tier Garmin running dynamics without the ₹50,000+ price tag",
                    "Zero subscription fees for all health metrics, recovery plans, and coaching",
                    "High resale value retention and durable software ecosystem support",
                ],
                "concerns": [
                    "No built-in speaker or mic for answering Bluetooth phone calls directly",
                ],
                "conclusion": "Best-in-class price-to-performance ratio for fitness enthusiasts.",
                "factors": ["Feature density per rupee", "Zero mandatory subscription fees", "Ecosystem longevity", "Build longevity"],
            },
        },

        # 2. FINANCE
        "finance": {
            "returnPotential": {
                "score": 89.0,
                "strengths": [
                    "Strong historical risk-adjusted compounding returns projected at 12–14% CAGR",
                    "Disciplined index tracking and minimal management fee drag",
                    "High statistical probability of outpacing inflation over a 3–5 year horizon",
                ],
                "concerns": [
                    "Demands holding patience through cyclical macroeconomic drawdowns",
                ],
                "conclusion": "High return potential with solid long-term upside.",
                "factors": ["Expected CAGR", "Annualized yield", "Compounding horizon", "Inflation beat"],
            },
            "risk": {
                "score": 84.0,
                "strengths": [
                    "Diversified multi-asset allocation significantly dampens single-sector volatility",
                    "Downside mitigation buffers protect baseline capital preservation",
                    "Low portfolio beta relative to speculative market instruments",
                ],
                "concerns": [
                    "Short-term market corrections can cause temporary mark-to-market drawdowns",
                ],
                "conclusion": "Controlled downside risk with robust capital preservation.",
                "factors": ["Drawdown risk", "Capital preservation", "Volatility beta", "Diversification"],
            },
            "liquidity": {
                "score": 86.0,
                "strengths": [
                    "T+1 settlement turnaround on open-ended liquid allocations",
                    "Zero punitive lock-in clauses on primary withdrawal facilities",
                    "Direct online redemption capability to linked savings accounts",
                ],
                "concerns": [
                    "Partial exit loads apply if redeemed within the initial 90-day window",
                ],
                "conclusion": "Healthy liquidity with rapid emergency redemption access.",
                "factors": ["Cash access speed", "Redemption turnaround", "Lock-in terms", "Exit loads"],
            },
            "stability": {
                "score": 88.0,
                "strengths": [
                    "Managed by established tier-1 asset management institutions",
                    "Strict regulatory oversight and segregated client asset custody",
                    "Proven operational resilience across diverse rate cycles",
                ],
                "concerns": [
                    "Macro-economic interest rate shifts may temporarily adjust yields",
                ],
                "conclusion": "High institutional stability with consistent regulatory governance.",
                "factors": ["Valuation predictability", "Manager track record", "Stress resilience", "Asset safety"],
            },
            "growth": {
                "score": 91.0,
                "strengths": [
                    "Superior reinvestment compounding efficiency across multi-year cycles",
                    "Secular exposure to expanding digital and domestic growth sectors",
                    "Protects purchasing power against persistent inflationary erosion",
                ],
                "concerns": [
                    "Requires multi-year commitment to unlock full compounding exponential curve",
                ],
                "conclusion": "Exceptional long-term wealth compounding engine.",
                "factors": ["Capital growth", "Compounding multiplier", "Inflation hedge", "Long-term horizon"],
            },
        },

        # 3. CAREER
        "career": {
            "salary": {
                "score": 88.0,
                "strengths": [
                    "Competitive base compensation package above 75th percentile market benchmarks",
                    "Transparent annual appraisal schedule and performance bonus upside",
                    "Comprehensive family healthcare and professional development stipends",
                ],
                "concerns": [
                    "Variable bonus component is tied to quarterly departmental revenue targets",
                ],
                "conclusion": "Attractive compensation structure with meaningful financial momentum.",
                "factors": ["Base salary", "Bonus upside", "Benefits package", "Market percentile"],
            },
            "skillFit": {
                "score": 93.0,
                "strengths": [
                    "Direct 1:1 application of core technical strengths and academic background",
                    "Significant architectural autonomy and problem-solving ownership",
                    "Modern toolchain and high-velocity engineering standards",
                ],
                "concerns": [
                    "Initial onboarding orientation required on proprietary domain workflows in the first 60 days",
                ],
                "conclusion": "Exceptional skill alignment with immediate day-to-day impact.",
                "factors": ["Technical skill fit", "Role autonomy", "Problem complexity", "Ownership"],
            },
            "growth": {
                "score": 90.0,
                "strengths": [
                    "Accelerated promotion velocity with clear technical lead career milestones",
                    "Direct mentorship from distinguished senior engineering leadership",
                    "High-visibility product exposure accelerating resume equity",
                ],
                "concerns": [
                    "High peer caliber requires continuous learning and proactive communication",
                ],
                "conclusion": "Outstanding career launchpad with steep upward progression.",
                "factors": ["Promotion track", "Mentorship access", "Resume equity", "Leadership visibility"],
            },
            "workLifeBalance": {
                "score": 82.0,
                "strengths": [
                    "Flexible hybrid schedule with core collaboration hours",
                    "Generous paid time-off policy and no-meeting focus days",
                    "Supportive management culture actively discouraging weekend messaging",
                ],
                "concerns": [
                    "Occasional sprint crunch during major quarterly platform launch windows",
                ],
                "conclusion": "Sustainable work rhythm with healthy team boundaries.",
                "factors": ["Schedule flexibility", "Work hours sustainability", "Burnout safeguards", "PTO policy"],
            },
            "stability": {
                "score": 86.0,
                "strengths": [
                    "Strong corporate balance sheet with 3+ years verified operational runway",
                    "Low employee turnover across core technical departments",
                    "Diversified enterprise revenue streams reducing market risk",
                ],
                "concerns": [
                    "Broader industry macroeconomic shifts can moderate annual hiring pace",
                ],
                "conclusion": "Solid organizational stability with dependable job security.",
                "factors": ["Company runway", "Team retention", "Revenue fundamentals", "Job security"],
            },
        },

        # 4. EDUCATION
        "education": {
            "academicQuality": {
                "score": 91.0,
                "strengths": [
                    "Accredited rigorous curriculum aligned with modern industry standards",
                    "World-class faculty with active research publications and industry ties",
                    "State-of-the-art computational labs and comprehensive digital libraries",
                ],
                "concerns": [
                    "Intense coursework load demands disciplined weekly study schedules",
                ],
                "conclusion": "Top-tier academic rigor and exceptional educational depth.",
                "factors": ["Curriculum rigor", "Faculty credentials", "Lab infrastructure", "Research output"],
            },
            "cost": {
                "score": 84.0,
                "strengths": [
                    "Transparent fee schedule with merit scholarships and flexible installment plans",
                    "Strong projected return on educational investment within 24 months post-graduation",
                ],
                "concerns": [
                    "Living expenses and course materials add moderate ancillary financial overhead",
                ],
                "conclusion": "Balanced cost structure with strong lifetime earning dividend.",
                "factors": ["Tuition cost", "Scholarship aid", "Educational ROI", "Living overhead"],
            },
            "placements": {
                "score": 90.0,
                "strengths": [
                    "94%+ historical placement rate across top-tier multinational companies",
                    "Dedicated career guidance cell offering mock interviews and resume coaching",
                    "High median starting package benchmarked across competing institutions",
                ],
                "concerns": [
                    "Premier tier-1 placement slots require maintaining top quartile academic standing",
                ],
                "conclusion": "Outstanding career placement pipeline with reliable corporate recruitment.",
                "factors": ["Placement rate", "Median salary", "Corporate recruiting", "Career coaching"],
            },
            "experience": {
                "score": 88.0,
                "strengths": [
                    "Vibrant multicultural campus community with active student clubs and hackathons",
                    "Modern campus sports, dining, and co-working amenities",
                ],
                "concerns": [
                    "Urban campus environment has limited dedicated on-campus student housing",
                ],
                "conclusion": "Enriching campus experience fostering lasting personal and professional networks.",
                "factors": ["Campus life", "Peer collaboration", "Student clubs", "Amenities"],
            },
            "futureOpportunity": {
                "score": 92.0,
                "strengths": [
                    "Globally recognized institutional brand recognized by leading international employers",
                    "Extensive active alumni network holding senior leadership positions worldwide",
                ],
                "concerns": [
                    "International work authorization remains dependent on destination country visa rules",
                ],
                "conclusion": "Prestigious institutional credential unlocking lifelong career mobility.",
                "factors": ["Brand prestige", "Global alumni network", "Career mobility", "Graduate pedigree"],
            },
        },

        # 5. TRAVEL
        "travel": {
            "cost": {
                "score": 87.0,
                "strengths": [
                    "Affordable lodging, dining, and transport options within defined budget parameters",
                    "High value per rupee compared to commercialized international destinations",
                ],
                "concerns": [
                    "Peak tourist seasons introduce localized surge pricing on private transit",
                ],
                "conclusion": "Highly economical itinerary with exceptional experiential value.",
                "factors": ["Lodging rates", "Transit costs", "Dining expenses", "Budget headroom"],
            },
            "safety": {
                "score": 92.0,
                "strengths": [
                    "Low regional crime index and welcoming local hospitality culture",
                    "Accessible emergency healthcare facilities and 24/7 tourist helpline",
                ],
                "concerns": [
                    "Monsoon season may trigger temporary localized mountain road warnings",
                ],
                "conclusion": "Dependable safety rating with secure traveler infrastructure.",
                "factors": ["Regional safety index", "Emergency healthcare", "Traveler security", "Tourist support"],
            },
            "experience": {
                "score": 91.0,
                "strengths": [
                    "Pristine scenic vistas, rich cultural heritage, and exceptional local culinary options",
                    "Peaceful serene ambiance ideal for rest, creative work, and rejuvenation",
                ],
                "concerns": [
                    "High altitude may require 24-hour acclimatization for sensitive travelers",
                ],
                "conclusion": "Unforgettable travel experience offering deep cultural and scenic immersion.",
                "factors": ["Scenic vistas", "Cultural heritage", "Culinary quality", "Relaxation index"],
            },
            "convenience": {
                "score": 85.0,
                "strengths": [
                    "Direct highway connectivity and regular domestic flight/rail links",
                    "Widespread digital payment acceptance and reliable 5G cellular coverage",
                ],
                "concerns": [
                    "Last-mile mountain transit requires experienced local taxi operators",
                ],
                "conclusion": "Smooth logistics with minimal travel friction.",
                "factors": ["Transit duration", "Airport/rail access", "Connectivity", "Payment ease"],
            },
            "attractions": {
                "score": 89.0,
                "strengths": [
                    "High density of heritage monasteries, nature trails, and viewpoint excursions",
                    "Engaging day trips suitable for both leisure and adventure enthusiasts",
                ],
                "concerns": [
                    "Certain historic viewpoints require advance entry permits during weekends",
                ],
                "conclusion": "Rich sightseeing density with diverse recreational activities.",
                "factors": ["Sightseeing density", "Heritage landmarks", "Trail access", "Activity variety"],
            },
        },

        # 6. SHOPPING
        "shopping": {
            "price": {
                "score": 88.0,
                "strengths": [
                    "Competitive market pricing well within defined budget boundaries",
                    "High component value without premium brand markup overhead",
                ],
                "concerns": [
                    "Infrequent promotional discounts due to consistent retail demand",
                ],
                "conclusion": "Great value for money with transparent pricing.",
                "factors": ["Price-to-quality ratio", "Retail discount", "Budget fit", "Value proposition"],
            },
            "quality": {
                "score": 91.0,
                "strengths": [
                    "High-grade materials with premium manufacturing tolerances",
                    "Thorough quality control testing verifying structural integrity",
                ],
                "concerns": [
                    "Slightly heavier build footprint due to reinforced structural components",
                ],
                "conclusion": "Outstanding build quality and premium craftsmanship.",
                "factors": ["Material quality", "Manufacturing standards", "Finish and feel", "Tolerances"],
            },
            "features": {
                "score": 89.0,
                "strengths": [
                    "Comprehensive feature set fulfilling all primary and secondary use cases",
                    "Intuitive ergonomic adjustability and straightforward maintenance",
                ],
                "concerns": [
                    "Secondary accessory bundle is sold separately",
                ],
                "conclusion": "Feature-packed design delivering high daily utility.",
                "factors": ["Feature completeness", "Everyday utility", "Versatility", "Ease of use"],
            },
            "reviews": {
                "score": 92.0,
                "strengths": [
                    "Overwhelmingly positive user ratings (4.6/5 across 2,000+ verified purchases)",
                    "High praise for dependable day-to-day reliability and after-sales support",
                ],
                "concerns": [
                    "Occasional shipping packaging feedback noted by a small minority of buyers",
                ],
                "conclusion": "Verified customer satisfaction with proven market reputation.",
                "factors": ["Buyer sentiment", "Average rating", "Defect rate", "Review consensus"],
            },
            "durability": {
                "score": 86.0,
                "strengths": [
                    "Tested for multi-year continuous use with wear-resistant finishes",
                    "Comprehensive 3-year manufacturer warranty with responsive service",
                ],
                "concerns": [
                    "Replacement wear components must be sourced directly from authorized channels",
                ],
                "conclusion": "Durable construction built to last multiple years.",
                "factors": ["Expected lifespan", "Warranty coverage", "Wear resistance", "Service availability"],
            },
        },

        # 7. OTHER / GENERIC
        "other": {
            "optionFit": {
                "score": 90.0,
                "strengths": [
                    "Direct strategic alignment with primary decision objectives and criteria",
                    "High compatibility with current operational and personal constraints",
                ],
                "concerns": [
                    "Requires clear prioritization to prevent secondary goal dilution",
                ],
                "conclusion": "Strong strategic fit matching the core intent of the dilemma.",
                "factors": ["Goal alignment", "Strategic fit", "Constraint compatibility", "Core intent"],
            },
            "value": {
                "score": 86.0,
                "strengths": [
                    "Prudent balance of cost versus delivered outcomes",
                    "Maximizes utility without wasteful excess expenditure",
                ],
                "concerns": [
                    "May require upfront investment before tangible benefits fully materialize",
                ],
                "conclusion": "High economic value with sensible resource allocation.",
                "factors": ["Cost-benefit ratio", "Resource efficiency", "Utility yield", "Budget balance"],
            },
            "risk": {
                "score": 84.0,
                "strengths": [
                    "Low catastrophic downside risk with clear reversibility options",
                    "Well-defined mitigation steps for potential secondary obstacles",
                ],
                "concerns": [
                    "Unforeseen external developments require periodic review checkpoints",
                ],
                "conclusion": "Manageable risk exposure with comfortable safety margins.",
                "factors": ["Downside protection", "Reversibility", "Safety margin", "Contingency planning"],
            },
            "experience": {
                "score": 88.0,
                "strengths": [
                    "High qualitative satisfaction and peace of mind upon execution",
                    "Smooth day-to-day workflow with minimal administrative overhead",
                ],
                "concerns": [
                    "Initial transition adjustment period during the first month",
                ],
                "conclusion": "Positive qualitative experience supporting overall well-being.",
                "factors": ["Daily satisfaction", "Execution friction", "Peace of mind", "Quality of life"],
            },
            "longTermImpact": {
                "score": 89.0,
                "strengths": [
                    "Compound positive benefits that multiply over multi-year horizons",
                    "Creates durable foundations adaptable to evolving future conditions",
                ],
                "concerns": [
                    "Demands sustained discipline to capture full long-term upside",
                ],
                "conclusion": "Substantial positive multi-year impact with enduring relevance.",
                "factors": ["Multi-year durability", "Future adaptability", "Compounding value", "Long-term relevance"],
            },
        },
    }

    def evaluate_dimension(
        self,
        agent_id: str,
        agent_name: str,
        specialization: str,
        decision: DecisionInputSchema,
    ) -> AgentResult:
        category = (decision.category or "electronics").strip().lower()
        sub = (decision.subcategory or "").strip().lower()
        desc_lower = (decision.description or "").lower()

        # Keyword auto-detection if subcategory is not explicitly provided
        if not sub and category == "electronics":
            if "watch" in desc_lower:
                sub = "smartwatch"
            elif "phone" in desc_lower or "mobile" in desc_lower:
                sub = "smartphone"
            elif "laptop" in desc_lower or "notebook" in desc_lower or "macbook" in desc_lower:
                sub = "laptop"

        # Look up subcategory- or category-tailored evaluation
        composite_key = f"{category}:{sub}"
        category_evals = (
            self.EVALUATION_CATALOG.get(composite_key)
            or self.EVALUATION_CATALOG.get(category)
            or self.EVALUATION_CATALOG["other"]
        )
        agent_data = category_evals.get(agent_id)

        # Fallback if agent_id key differs
        if not agent_data:
            # Try fuzzy match on agent name
            for k, v in category_evals.items():
                if k.lower() in agent_name.lower() or agent_name.lower() in k.lower():
                    agent_data = v
                    break

        if agent_data:
            return AgentResult(
                agent=agent_name,
                score=float(agent_data["score"]),
                strengths=list(agent_data["strengths"]),
                concerns=list(agent_data["concerns"]),
                conclusion=str(agent_data["conclusion"]),
                factors=list(agent_data["factors"]),
            )

        # Clean generic fallback if ever missing
        return AgentResult(
            agent=agent_name,
            score=86.0,
            strengths=[
                f"Meets fundamental criteria for {specialization}",
                "Favorable alignment with defined user requirements",
            ],
            concerns=[
                "Requires careful monitoring under high-variance constraints",
            ],
            conclusion=f"Satisfactory performance regarding {specialization}.",
            factors=[
                specialization,
                "User constraints",
                "Baseline criteria",
            ],
        )


def get_ai_provider() -> AIProvider:
    """
    Factory function to instantiate the configured AI Provider.
    Defaults to MockAIProvider when AI_PROVIDER='mock'.
    """
    provider_name = getattr(settings, "AI_PROVIDER", "mock").lower()
    if provider_name == "mock":
        return MockAIProvider()
    return MockAIProvider()
