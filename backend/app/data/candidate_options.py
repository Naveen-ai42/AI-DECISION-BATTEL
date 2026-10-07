"""
Candidate Options Dataset for Decision Arena.
Provides realistic sample / benchmark datasets for multi-option decision evaluation.
Clearly designated as DEMO / SAMPLE DATA.
"""

from typing import Dict, List, Any

DEMO_OPTIONS_CATALOG: Dict[str, List[Dict[str, Any]]] = {
    # =========================================================================
    # ELECTRONICS
    # =========================================================================
    "electronics:laptop": [
        {
            "id": "asus-tuf-a15",
            "name": "ASUS TUF Gaming A15",
            "price": "₹54,990",
            "description": "AMD Ryzen 7 7735HS, RTX 4050 6GB, 16GB DDR5, 144Hz FHD IPS display, 90Wh battery",
            "tags": ["Ryzen 7", "RTX 4050", "16GB RAM", "144Hz", "90Wh Battery"],
            "attributes": {
                "performance": 92.0,
                "value": 86.0,
                "battery": 81.0,
                "experience": 90.0,
                "futureProof": 86.0
            },
            "strengths": [
                "Class-leading compute throughput for coding, Docker, and local AI prototyping",
                "High-capacity 90Wh battery delivers 7+ hours of general productivity",
                "Expandable dual-channel DDR5 RAM and second M.2 NVMe slot"
            ],
            "concerns": [
                "Chassis weighs 2.2kg which is heavier for everyday commuting",
                "Webcam is standard 720p rather than studio grade"
            ]
        },
        {
            "id": "lenovo-legion-pro-5",
            "name": "Lenovo Legion Pro 5",
            "price": "₹89,990",
            "description": "Intel Core i7-13700HX, RTX 4060 8GB, 16GB DDR5, 240Hz WQXGA 500 nits display",
            "tags": ["Core i7", "RTX 4060", "240Hz 2K", "Coldfront 5.0", "500 nits"],
            "attributes": {
                "performance": 96.0,
                "value": 78.0,
                "battery": 72.0,
                "experience": 93.0,
                "futureProof": 88.0
            },
            "strengths": [
                "Exceptional desktop-grade multi-core compilation speed and GPU headroom",
                "Superb 500 nits 2.5K color-calibrated display with HDR support",
                "Premium TrueStrike tactile keyboard with full-sized numeric keypad"
            ],
            "concerns": [
                "Substantially higher price ceiling compared to entry-budget alternatives",
                "Heavier 300W power adapter required for full performance"
            ]
        },
        {
            "id": "acer-nitro-v15",
            "name": "Acer Nitro V 15",
            "price": "₹49,990",
            "description": "Intel Core i5-13420H, RTX 3050 6GB, 16GB DDR5, 144Hz IPS display, Thunderbolt 4",
            "tags": ["Core i5", "RTX 3050 6GB", "16GB RAM", "Thunderbolt 4", "Budget Pick"],
            "attributes": {
                "performance": 85.0,
                "value": 92.0,
                "battery": 76.0,
                "experience": 82.0,
                "futureProof": 80.0
            },
            "strengths": [
                "Highest performance-to-price ratio in the sub-₹50k tier",
                "Generous 6GB VRAM buffer handles modern ML models better than older 4GB GPUs",
                "Includes full Thunderbolt 4 connectivity for external docks"
            ],
            "concerns": [
                "Display color gamut is standard 45% NTSC which is average for color grading",
                "Fans become distinctly audible under sustained maximum synthetic workloads"
            ]
        },
        {
            "id": "macbook-air-m2",
            "name": "Apple MacBook Air M2",
            "price": "₹94,900",
            "description": "Apple M2 8-core CPU / 10-core GPU, 16GB Unified Memory, 13.6\" Liquid Retina, MagSafe",
            "tags": ["Apple M2", "16GB Unified", "Liquid Retina", "Fanless", "18hr Battery"],
            "attributes": {
                "performance": 88.0,
                "value": 76.0,
                "battery": 97.0,
                "experience": 95.0,
                "futureProof": 89.0
            },
            "strengths": [
                "Unmatched 15–18 hour real-world battery life away from wall power",
                "Dead-silent fanless thermal design with zero fan noise ever",
                "Industry-best glass Force Touch trackpad and speaker acoustics"
            ],
            "concerns": [
                "Non-upgradeable unified memory and storage after purchase",
                "Limited to a single external monitor without specialized DisplayLink adapters"
            ]
        },
        {
            "id": "hp-victus-15",
            "name": "HP Victus 15",
            "price": "₹44,990",
            "description": "AMD Ryzen 5 7535HS, RTX 2050 4GB, 8GB DDR5, 144Hz FHD display, Fast Charge",
            "tags": ["Ryzen 5", "RTX 2050", "144Hz", "Fast Charge", "Sub-₹45k"],
            "attributes": {
                "performance": 79.0,
                "value": 88.0,
                "battery": 75.0,
                "experience": 80.0,
                "futureProof": 74.0
            },
            "strengths": [
                "Entry-level accessible pricing with discrete GPU acceleration",
                "Clean minimalist chassis aesthetic suitable for professional offices",
                "Fast charging recovers 50% capacity in 30 minutes"
            ],
            "concerns": [
                "Base 8GB RAM will require an immediate upgrade for intensive ML pipelines",
                "Slight screen hinge wobble under vigorous typing"
            ]
        }
    ],

    "electronics:smartphone": [
        {
            "id": "oneplus-12r",
            "name": "OnePlus 12R (5G)",
            "price": "₹39,999",
            "description": "Snapdragon 8 Gen 2, 50MP Sony IMX890 OIS, 5500mAh battery, 100W charging, 1.5K LTPO4 120Hz",
            "tags": ["Snapdragon 8 Gen 2", "50MP OIS", "5500mAh", "100W", "LTPO4"],
            "attributes": {
                "performance": 93.0,
                "camera": 91.0,
                "battery": 87.0,
                "display": 92.0,
                "value": 90.0
            },
            "strengths": [
                "Flagship-tier Snapdragon 8 Gen 2 chipset handles gaming and multi-tasking effortlessly",
                "Huge 5,500mAh cell with 100W flash charging (0–100% in under 28 mins)",
                "Vibrant 1.5K LTPO4 AMOLED with 4,500 nits peak outdoor brightness"
            ],
            "concerns": [
                "Lacks dedicated telephoto zoom lens; relies on digital crop",
                "No official wireless charging support"
            ]
        },
        {
            "id": "google-pixel-8a",
            "name": "Google Pixel 8a",
            "price": "₹37,999",
            "description": "Google Tensor G3, 64MP Dual Camera with Best Take, 120Hz Actua OLED, 7-year OS updates",
            "tags": ["Tensor G3", "Best-in-Class Camera", "7yr Updates", "IP67", "Wireless Charging"],
            "attributes": {
                "performance": 85.0,
                "camera": 95.0,
                "battery": 81.0,
                "display": 89.0,
                "value": 88.0
            },
            "strengths": [
                "Industry-leading computational photography and low-light portrait capture",
                "7 full years of guaranteed Android OS, feature drops, and security updates",
                "Clean stock Android interface with no bloatware or ads"
            ],
            "concerns": [
                "18W wired charging speed is slower than competing fast chargers",
                "Slightly thicker display bezels compared to curved edge flagships"
            ]
        },
        {
            "id": "samsung-s23-fe",
            "name": "Samsung Galaxy S23 FE",
            "price": "₹38,999",
            "description": "Exynos 2200, 50MP Main with 3x Optical Telephoto, Dynamic AMOLED 2X 120Hz, IP68 rated",
            "tags": ["3x Telephoto", "IP68 Water Resistant", "DeX Mode", "Dynamic AMOLED", "One UI"],
            "attributes": {
                "performance": 87.0,
                "camera": 90.0,
                "battery": 79.0,
                "display": 91.0,
                "value": 84.0
            },
            "strengths": [
                "Only option in price bracket with dedicated 3x optical telephoto lens",
                "Full IP68 dust and water submersion resistance rating",
                "Samsung DeX desktop workstation mode via USB-C"
            ],
            "concerns": [
                "Battery runtime tops out at ~6 hours SOT under heavy cellular data use",
                "No power adapter included in retail packaging"
            ]
        },
        {
            "id": "nothing-phone-2",
            "name": "Nothing Phone (2)",
            "price": "₹36,999",
            "description": "Snapdragon 8+ Gen 1, Dual 50MP Sony sensors, Glyph Interface LEDs, 4700mAh, Nothing OS 2.5",
            "tags": ["Glyph Interface", "Snapdragon 8+", "Clean OS", "Wireless Charging", "Unique Design"],
            "attributes": {
                "performance": 89.0,
                "camera": 84.0,
                "battery": 85.0,
                "display": 90.0,
                "value": 86.0
            },
            "strengths": [
                "Unique Glyph notification lighting with custom LED ringtone sequencing",
                "Extremely fast and bloat-free Nothing OS software experience",
                "Symmetrical slim display bezels with 1–120Hz LTPO refresh"
            ],
            "concerns": [
                "Camera tuning occasionally exhibits oversaturated contrast in harsh sunlight",
                "Water resistance is splash-only IP54 rather than full submersion"
            ]
        },
        {
            "id": "xiaomi-13t-pro",
            "name": "Xiaomi 13T Pro",
            "price": "₹41,999",
            "description": "MediaTek Dimensity 9200+, 50MP Leica Optics with 2x Telephoto, 5000mAh, 120W HyperCharge",
            "tags": ["Dimensity 9200+", "Leica Optics", "120W Charging", "144Hz AMOLED", "IP68"],
            "attributes": {
                "performance": 91.0,
                "camera": 88.0,
                "battery": 84.0,
                "display": 90.0,
                "value": 85.0
            },
            "strengths": [
                "Blazing 120W HyperCharge recovers 100% capacity in 19 minutes flat",
                "Co-engineered Leica Authentic and Vibrant optical color tuning modes",
                "Ultra-smooth 144Hz AMOLED screen with 2,600 nits peak brightness"
            ],
            "concerns": [
                "HyperOS includes pre-installed promotional partner apps that require removal",
                "Slightly priced above strict sub-₹40k ceiling without bank offers"
            ]
        }
    ],

    "electronics:smartwatch": [
        {
            "id": "garmin-forerunner-165",
            "name": "Garmin Forerunner 165",
            "price": "₹14,990",
            "description": "Dual-frequency GPS, Elevate V4 optical HR, 1.2\" AMOLED, 11-day battery, HRV Status, 5 ATM",
            "tags": ["Dual-band GPS", "11-Day Battery", "HRV Status", "AMOLED", "Zero Subscriptions"],
            "attributes": {
                "fitness": 95.0,
                "battery": 94.0,
                "durability": 90.0,
                "display": 88.0,
                "value": 89.0
            },
            "strengths": [
                "Pro-tier GPS accuracy and medical-grade heart rate correlation for runners",
                "11 days of real-world battery life completely eliminates daily charging anxiety",
                "Zero paywalled metrics; training plans and recovery insights are 100% free forever"
            ],
            "concerns": [
                "Lacks built-in microphone for answering voice calls on the wrist",
                "Polymer bezel prioritizes athletic light weight over metallic jewelry luxury"
            ]
        },
        {
            "id": "amazfit-gtr-4",
            "name": "Amazfit GTR 4",
            "price": "₹12,999",
            "description": "Dual-band circularly polarized GPS, BioTracker 4.0, 1.43\" AMOLED, 14-day battery, Bluetooth calls",
            "tags": ["14-Day Battery", "Bluetooth Calls", "Dual-band GPS", "Aluminum Alloy", "Offline Music"],
            "attributes": {
                "fitness": 86.0,
                "battery": 93.0,
                "durability": 87.0,
                "display": 90.0,
                "value": 91.0
            },
            "strengths": [
                "Outstanding 14-day battery endurance with classic metallic watch styling",
                "Supports direct Bluetooth voice calling and offline onboard MP3 storage",
                "Large 1.43-inch sharp AMOLED display with anti-fingerprint coating"
            ],
            "concerns": [
                "HR sensor accuracy dips slightly during high-intensity interval sprints",
                "Third-party app ecosystem is basic compared to WearOS or watchOS"
            ]
        },
        {
            "id": "samsung-galaxy-watch-6",
            "name": "Samsung Galaxy Watch 6",
            "price": "₹18,999",
            "description": "BioActive 3-in-1 Sensor, Sapphire Crystal glass, WearOS 4, 1.5\" Super AMOLED 2000 nits, ECG/BP",
            "tags": ["WearOS 4", "Sapphire Glass", "ECG & BP", "Google Play Apps", "Samsung Ecosystem"],
            "attributes": {
                "fitness": 89.0,
                "battery": 72.0,
                "durability": 88.0,
                "display": 94.0,
                "value": 80.0
            },
            "strengths": [
                "Full WearOS smartwatch experience with Google Maps, Play Store, and WhatsApp",
                "Premium Sapphire Crystal front glass resists keys and scratches",
                "Advanced body composition analysis (BIA) and FDA-cleared ECG"
            ],
            "concerns": [
                "Battery requires daily charging (approx 30–40 hours runtime)",
                "Select advanced health features (ECG/BP) require a paired Samsung Galaxy phone"
            ]
        },
        {
            "id": "fitbit-charge-6",
            "name": "Fitbit Charge 6",
            "price": "₹11,990",
            "description": "Built-in GPS, Google Maps navigation, ECG app, EDA stress sensor, 7-day battery, 5 ATM water",
            "tags": ["Built-in GPS", "Google Integration", "Sleep Stages", "7-Day Battery", "Compact"],
            "attributes": {
                "fitness": 88.0,
                "battery": 88.0,
                "durability": 84.0,
                "display": 82.0,
                "value": 85.0
            },
            "strengths": [
                "Slim lightweight fitness band form factor ideal for 24/7 sleep tracking",
                "Deep integration with Google Wallet contactless tap-and-pay",
                "7 days of continuous battery life with automatic workout detection"
            ],
            "concerns": [
                "Smaller screen is less suited for reading long text notifications",
                "Comprehensive historical trend analytics require a Fitbit Premium subscription"
            ]
        },
        {
            "id": "apple-watch-se",
            "name": "Apple Watch SE (2nd Gen)",
            "price": "₹24,900",
            "description": "Optical HR sensor V2, S8 SiP dual-core, Crash Detection, 1000 nits Retina OLED, 50m water",
            "tags": ["Apple Ecosystem", "Crash Detection", "Retina OLED", "watchOS 10", "Premium Haptics"],
            "attributes": {
                "fitness": 90.0,
                "battery": 70.0,
                "durability": 85.0,
                "display": 92.0,
                "value": 78.0
            },
            "strengths": [
                "Flawless integration with iOS ecosystem, Apple Pay, and iMessage",
                "Class-leading Taptic Engine haptics and responsive watchOS animations",
                "Accurate heart rate monitoring and automatic high/low heart rate notifications"
            ],
            "concerns": [
                "Strictly incompatible with Android smartphones",
                "Requires daily overnight charging (approx 18 hours standard battery life)"
            ]
        }
    ],

    # =========================================================================
    # FINANCE
    # =========================================================================
    "finance:investment": [
        {
            "id": "diversified-index-flexicap",
            "name": "Diversified Index & Flexi-Cap Allocation",
            "price": "₹2,00,000",
            "description": "60% Nifty 50 Index + 40% Tier-1 Flexi-Cap equity allocation with dynamic rebalancing",
            "tags": ["12-14% CAGR", "Nifty 50", "Flexi-Cap", "Long-Term", "T+1 Liquidity"],
            "attributes": {
                "returnPotential": 91.0,
                "risk": 88.0,
                "liquidity": 86.0,
                "stability": 88.0,
                "growth": 90.0
            },
            "strengths": [
                "Historical 12–14% CAGR comfortably outpaces long-term retail inflation",
                "Low overall expense ratio (<0.35%) minimizes fee drag across a 5-year horizon",
                "T+1 settlement turnaround on open-ended liquid allocations with zero lock-in",
                "Broad large-cap diversification provides resilient downside risk protection"
            ],
            "concerns": [
                "Subject to interim equity market drawdown volatility during macro corrections",
                "Demands a 3–5 year minimum holding discipline to realize full compounding"
            ]
        },
        {
            "id": "high-yield-arbitrage-liquid",
            "name": "High-Yield Liquid & Arbitrage Allocation",
            "price": "₹2,00,000",
            "description": "70% Arbitrage Fund + 30% Overnight Liquid Fund with equity tax efficiency",
            "tags": ["7.2-7.8% Yield", "Equity Taxation", "Capital Preservation", "Instant Cash", "Low Risk"],
            "attributes": {
                "returnPotential": 76.0,
                "risk": 95.0,
                "liquidity": 96.0,
                "stability": 94.0,
                "growth": 72.0
            },
            "strengths": [
                "Nearly zero mark-to-market drawdown risk; principal capital is highly shielded",
                "Treated as equity for capital gains taxation, reducing effective tax drag",
                "Instant redemption access with linked debit card or same-day NEFT/RTGS"
            ],
            "concerns": [
                "Compounding yield (~7.5%) will not aggressively beat high inflation over a decade",
                "Limited long-term wealth multiplication compared to active equity"
            ]
        },
        {
            "id": "balanced-hybrid-sip",
            "name": "Balanced 50:50 Equity & Debt Hybrid",
            "price": "₹2,00,000",
            "description": "50% High-dividend equity basket + 50% High-grade corporate debt instruments",
            "tags": ["10-12% Blended CAGR", "Auto Rebalancing", "Moderate Risk", "Downside Buffer"],
            "attributes": {
                "returnPotential": 84.0,
                "risk": 88.0,
                "liquidity": 85.0,
                "stability": 89.0,
                "growth": 83.0
            },
            "strengths": [
                "Automatic quarterly rebalancing locks in gains during market peaks",
                "Significant downside buffer cushions against equity corrections",
                "Healthy predictable regular distribution yield option"
            ],
            "concerns": [
                "Slightly higher total expense ratio due to active hybrid fund management",
                "Sacrifices peak bull market upside relative to 100% pure equity"
            ]
        },
        {
            "id": "sovereign-gold-bonds",
            "name": "Sovereign Gold & Dynamic Bond Basket",
            "price": "₹2,00,000",
            "description": "40% Sovereign Gold Reserve + 60% Target Maturity AAA Central Government Securities",
            "tags": ["Sovereign Guarantee", "Gold Hedge", "Fixed 2.5% Coupon", "Zero Credit Risk"],
            "attributes": {
                "returnPotential": 80.0,
                "risk": 91.0,
                "liquidity": 82.0,
                "stability": 92.0,
                "growth": 79.0
            },
            "strengths": [
                "Backed by central sovereign guarantee with zero default or credit risk",
                "Gold provides direct portfolio hedging against currency devaluation and geopolitical shocks",
                "Tax-free capital gains on gold if held until sovereign maturity"
            ],
            "concerns": [
                "Secondary market trading volumes can experience modest bid-ask price spreads",
                "Fixed tenure structure rewards patient holding"
            ]
        },
        {
            "id": "target-maturity-debt",
            "name": "Target Maturity Index Debt Fund",
            "price": "₹2,00,000",
            "description": "AAA Public Sector Undertakings & State Development Loans maturing in 2028",
            "tags": ["7.5% Predictable YTM", "AAA Safety", "Zero Duration Risk", "Institutional Grade"],
            "attributes": {
                "returnPotential": 78.0,
                "risk": 93.0,
                "liquidity": 88.0,
                "stability": 95.0,
                "growth": 75.0
            },
            "strengths": [
                "Known yield-to-maturity (YTM) locks in returns upon holding to maturity date",
                "Zero credit risk as portfolio comprises only top-tier state and PSU paper",
                "Lower expense ratio than traditional active debt funds"
            ],
            "concerns": [
                "Recent tax code changes align debt taxation with individual income tax slabs",
                "Fixed income returns do not benefit from corporate earnings expansions"
            ]
        }
    ],

    # =========================================================================
    # CAREER
    # =========================================================================
    "career:job": [
        {
            "id": "senior-data-scientist-product",
            "name": "Senior Applied Data Scientist (Product AI Track)",
            "price": "₹28–34 LPA",
            "description": "Leading machine learning & LLM evaluation for user-facing recommendation engines at a Series-C tech scaleup",
            "tags": ["LLM & RecSys", "Product Impact", "Modern Stack", "Hybrid 2-day", "Tier-1 Equity"],
            "attributes": {
                "salary": 92.0,
                "skillFit": 90.0,
                "growth": 93.0,
                "workLifeBalance": 82.0,
                "stability": 87.0
            },
            "strengths": [
                "Direct architectural ownership of core revenue-generating AI algorithms",
                "Generous equity component with clear secondary liquidation history",
                "High peer density working alongside former tier-1 tech leads"
            ],
            "concerns": [
                "Quarterly product releases occasionally involve sprint deadline crunches",
                "High expectation of rapid autonomous delivery with minimal initial hand-holding"
            ]
        },
        {
            "id": "staff-platform-engineer",
            "name": "Staff Platform & Distributed Systems Engineer",
            "price": "₹32–38 LPA",
            "description": "Architecting global high-throughput streaming pipelines, Kubernetes clusters, and multi-region infrastructure",
            "tags": ["Kubernetes", "High Scale", "Staff Track", "Competitive Base", "Remote-First"],
            "attributes": {
                "salary": 94.0,
                "skillFit": 88.0,
                "growth": 89.0,
                "workLifeBalance": 80.0,
                "stability": 91.0
            },
            "strengths": [
                "Highest cash base compensation offer among current candidate options",
                "Full remote flexibility with comprehensive home office allowance",
                "Strategic technical leadership role mentoring 12+ backend developers"
            ],
            "concerns": [
                "Requires periodic rotational on-call escalations for core tier-0 services",
                "Legacy technical debt in older microservices requires diplomatic refactoring"
            ]
        },
        {
            "id": "startup-founding-engineer",
            "name": "High-Growth Tech Scaleup Lead",
            "price": "₹24–28 LPA + 0.5% Equity",
            "description": "Early-stage technical lead building end-to-end cloud products from ground zero with venture backing",
            "tags": ["Founding Engineer", "High Equity", "Zero to One", "Rapid Velocity", "Full Ownership"],
            "attributes": {
                "salary": 85.0,
                "skillFit": 87.0,
                "growth": 95.0,
                "workLifeBalance": 72.0,
                "stability": 78.0
            },
            "strengths": [
                "Maximum exponential career trajectory if company scales to Series-A/B",
                "Complete freedom across tech stack selection, hiring, and system architecture",
                "Zero corporate red tape or bureaucratic review committees"
            ],
            "concerns": [
                "Work-life balance is demanding with frequent evening and weekend sprints",
                "Company runway is tied to venture milestones across an 18-month horizon"
            ]
        },
        {
            "id": "enterprise-cloud-architect",
            "name": "Enterprise Cloud Infrastructure Architect",
            "price": "₹29–33 LPA",
            "description": "Designing secure multi-cloud governance and compliance frameworks for global Fortune 500 financial clients",
            "tags": ["Enterprise Security", "Predictable Hours", "Fortune 500", "High Job Stability"],
            "attributes": {
                "salary": 90.0,
                "skillFit": 85.0,
                "growth": 84.0,
                "workLifeBalance": 88.0,
                "stability": 94.0
            },
            "strengths": [
                "Extremely predictable 40-hour work weeks with strict boundary enforcement",
                "Exceptional job security and institutional stability across recession cycles",
                "Comprehensive executive healthcare, pension, and tuition benefits"
            ],
            "concerns": [
                "Slower promotion cadence due to formal enterprise annual review cycles",
                "Rigid compliance and security approvals required before deploying code"
            ]
        },
        {
            "id": "applied-ai-engineering-specialist",
            "name": "Applied AI Engineering Specialist",
            "price": "₹27–31 LPA",
            "description": "Fine-tuning open weights, managing vector databases, and deploying low-latency agentic workflows",
            "tags": ["Generative AI", "Vector DBs", "RAG Pipelines", "High Market Demand"],
            "attributes": {
                "salary": 91.0,
                "skillFit": 92.0,
                "growth": 91.0,
                "workLifeBalance": 83.0,
                "stability": 86.0
            },
            "strengths": [
                "Working on cutting-edge generative AI and multi-agent systems in production",
                "Skills gained possess immense hiring market premium for the next decade",
                "Balanced hybrid schedule with budget for attending global research conferences"
            ],
            "concerns": [
                "Fast-moving tooling landscape means frameworks require continuous learning",
                "Occasional scope creep as business stakeholders experiment with novel AI use cases"
            ]
        }
    ]
}

def get_candidate_options(category: str, subcategory: str = "") -> List[Dict[str, Any]]:
    """
    Retrieves the 5 candidate options for a category and subcategory.
    Falls back gracefully to category default or clean generic options.
    """
    cat = (category or "electronics").strip().lower()
    sub = (subcategory or "").strip().lower()
    
    # Check composite key
    composite_key = f"{cat}:{sub}"
    if composite_key in DEMO_OPTIONS_CATALOG:
        return DEMO_OPTIONS_CATALOG[composite_key]
        
    # Check category defaults
    if cat == "electronics":
        return DEMO_OPTIONS_CATALOG["electronics:laptop"]
    if cat == "finance":
        return DEMO_OPTIONS_CATALOG["finance:investment"]
    if cat == "career":
        return DEMO_OPTIONS_CATALOG["career:job"]
        
    # Generic fallback with 5 candidate options
    return [
        {
            "id": f"{cat}-option-a",
            "name": f"Strategic Choice A ({cat.capitalize()} Tier 1)",
            "price": "Balanced Tier",
            "description": f"Optimized for primary requirements with robust execution safety and long-term viability.",
            "tags": ["High Alignment", "Balanced Risk", "Recommended"],
            "attributes": {
                "optionFit": 92.0,
                "value": 88.0,
                "risk": 86.0,
                "experience": 90.0,
                "longTermImpact": 89.0
            },
            "strengths": [
                "Direct fulfillment of primary stated goals with proven reliability",
                "Manageable downside risk profile with clear contingency paths"
            ],
            "concerns": [
                "Demands consistent upfront onboarding and attention to detail"
            ]
        },
        {
            "id": f"{cat}-option-b",
            "name": f"High-Value Alternative B ({cat.capitalize()} Value)",
            "price": "Budget Tier",
            "description": f"Maximizes direct value return with minimal ongoing capital commitment.",
            "tags": ["High Value", "Low Cost", "Safe"],
            "attributes": {
                "optionFit": 86.0,
                "value": 94.0,
                "risk": 84.0,
                "experience": 83.0,
                "longTermImpact": 81.0
            },
            "strengths": [
                "Best efficiency per unit cost within the candidate pool",
                "Low barrier to entry with immediate time-to-value"
            ],
            "concerns": [
                "Secondary features require minor manual workarounds"
            ]
        },
        {
            "id": f"{cat}-option-c",
            "name": f"Performance Choice C ({cat.capitalize()} Pro)",
            "price": "Premium Tier",
            "description": f"High-spec execution designed for heavy sustained workloads and maximum headroom.",
            "tags": ["Pro Grade", "High Output", "Premium"],
            "attributes": {
                "optionFit": 94.0,
                "value": 78.0,
                "risk": 82.0,
                "experience": 94.0,
                "longTermImpact": 91.0
            },
            "strengths": [
                "Top-tier performance headroom accommodating expanding requirements",
                "Highest qualitative user experience in benchmark tests"
            ],
            "concerns": [
                "Demands higher budget or operational commitment"
            ]
        },
        {
            "id": f"{cat}-option-d",
            "name": f"Conservative Choice D ({cat.capitalize()} Standard)",
            "price": "Standard Tier",
            "description": f"Emphasizes capital preservation, high predictability, and low maintenance friction.",
            "tags": ["Predictable", "Low Risk", "Stable"],
            "attributes": {
                "optionFit": 84.0,
                "value": 85.0,
                "risk": 93.0,
                "experience": 85.0,
                "longTermImpact": 86.0
            },
            "strengths": [
                "Predictable outcomes with very low historical variance",
                "Zero risk of critical disruption or lock-in traps"
            ],
            "concerns": [
                "Does not offer aggressive upside growth acceleration"
            ]
        },
        {
            "id": f"{cat}-option-e",
            "name": f"Agile Choice E ({cat.capitalize()} Flexible)",
            "price": "Flexible Tier",
            "description": f"Adaptive modular option offering high pivot flexibility and reversible terms.",
            "tags": ["Modular", "Reversible", "Agile"],
            "attributes": {
                "optionFit": 88.0,
                "value": 86.0,
                "risk": 87.0,
                "experience": 88.0,
                "longTermImpact": 85.0
            },
            "strengths": [
                "Can be adapted or pivoted as external conditions change",
                "Favorable short-term commitment terms"
            ],
            "concerns": [
                "Requires periodic reassessment to maintain alignment"
            ]
        }
    ]
