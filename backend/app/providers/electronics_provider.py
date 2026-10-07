"""
Electronics Candidate Providers for Decision Arena.
Provides dynamic candidate pools for Laptops, Smartphones, Smartwatches, Tablets, and Headphones.
Data source is currently marked as 'demo'.
"""

from typing import List, Dict, Any, Optional
from .base import BaseCandidateProvider, create_candidate_option
from ..schemas.decision import DecisionInputSchema

class LaptopProvider(BaseCandidateProvider):
    """Provides dynamic candidate options for laptops."""

    DEMO_LAPTOPS = [
        create_candidate_option(
            id="asus-tuf-a15",
            name="ASUS TUF Gaming A15",
            category="electronics",
            subcategory="laptop",
            price="₹54,990",
            description="AMD Ryzen 7 7735HS, RTX 4050 6GB, 16GB DDR5, 144Hz FHD IPS display, 90Wh battery",
            tags=["Ryzen 7", "RTX 4050", "16GB RAM", "144Hz", "90Wh Battery", "Dedicated GPU"],
            attributes={"performance": 92.0, "value": 92.0, "battery": 88.0, "experience": 90.0, "futureProof": 88.0},
            strengths=[
                "Class-leading compute throughput for coding, Docker, and local AI prototyping",
                "High-capacity 90Wh battery delivers 7+ hours of productivity",
                "Expandable dual-channel DDR5 RAM and second M.2 NVMe slot",
            ],
            concerns=[
                "Chassis weighs 2.2kg which is heavier for everyday commuting",
                "Webcam is standard 720p rather than studio grade",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="apple-macbook-air-m2",
            name="Apple MacBook Air M2",
            category="electronics",
            subcategory="laptop",
            price="₹94,900",
            description="Apple M2 8-core CPU / 10-core GPU, 16GB Unified Memory, 13.6\" Liquid Retina, MagSafe",
            tags=["Apple M2", "16GB Unified", "Liquid Retina", "Fanless", "18hr Battery"],
            attributes={"performance": 88.0, "value": 76.0, "battery": 97.0, "experience": 95.0, "futureProof": 89.0},
            strengths=[
                "Unmatched 15–18 hour real-world battery life away from wall power",
                "Dead-silent fanless thermal design with zero fan noise ever",
                "Industry-best glass Force Touch trackpad and speaker acoustics",
            ],
            concerns=[
                "Non-upgradeable unified memory and storage after purchase",
                "Limited to a single external monitor without specialized DisplayLink adapters",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="acer-nitro-v15",
            name="Acer Nitro V 15",
            category="electronics",
            subcategory="laptop",
            price="₹49,990",
            description="Intel Core i5-13420H, RTX 3050 6GB, 16GB DDR5, 144Hz IPS display, Thunderbolt 4",
            tags=["Core i5", "RTX 3050 6GB", "16GB RAM", "Thunderbolt 4", "Budget Pick"],
            attributes={"performance": 85.0, "value": 92.0, "battery": 76.0, "experience": 82.0, "futureProof": 80.0},
            strengths=[
                "Highest performance-to-price ratio in the sub-₹50k tier",
                "Generous 6GB VRAM buffer handles modern ML models better than older 4GB GPUs",
                "Includes full Thunderbolt 4 connectivity for external docks",
            ],
            concerns=[
                "Display color gamut is standard 45% NTSC which is average for color grading",
                "Fans become distinctly audible under sustained maximum synthetic workloads",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="lenovo-legion-pro-5",
            name="Lenovo Legion Pro 5",
            category="electronics",
            subcategory="laptop",
            price="₹89,990",
            description="Intel Core i7-13700HX, RTX 4060 8GB, 16GB DDR5, 240Hz WQXGA 500 nits display",
            tags=["Core i7", "RTX 4060", "240Hz 2K", "Coldfront 5.0", "500 nits"],
            attributes={"performance": 96.0, "value": 78.0, "battery": 72.0, "experience": 93.0, "futureProof": 88.0},
            strengths=[
                "Exceptional desktop-grade multi-core compilation speed and GPU headroom",
                "Superb 500 nits 2.5K color-calibrated display with HDR support",
                "Premium TrueStrike tactile keyboard with full-sized numeric keypad",
            ],
            concerns=[
                "Substantially higher price ceiling compared to entry-budget alternatives",
                "Heavier 300W power adapter required for full performance",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="hp-victus-15",
            name="HP Victus 15",
            category="electronics",
            subcategory="laptop",
            price="₹44,990",
            description="AMD Ryzen 5 7535HS, RTX 2050 4GB, 8GB DDR5, 144Hz FHD display, Fast Charge",
            tags=["Ryzen 5", "RTX 2050", "144Hz", "Fast Charge", "Sub-₹45k"],
            attributes={"performance": 79.0, "value": 88.0, "battery": 75.0, "experience": 80.0, "futureProof": 74.0},
            strengths=[
                "Entry-level accessible pricing with discrete GPU acceleration",
                "Clean minimalist chassis aesthetic suitable for professional offices",
                "Fast charging recovers 50% capacity in 30 minutes",
            ],
            concerns=[
                "Base 8GB RAM will require an immediate upgrade for intensive ML pipelines",
                "Slight screen hinge wobble under vigorous typing",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="dell-g15-5530",
            name="Dell G15 5530 Gaming",
            category="electronics",
            subcategory="laptop",
            price="₹72,990",
            description="Intel Core i5-13450HX, RTX 4050 6GB, 16GB DDR5, 120Hz FHD, Alienware-inspired cooling",
            tags=["Core i5 HX", "RTX 4050", "16GB RAM", "G-Key Boost"],
            attributes={"performance": 89.0, "value": 83.0, "battery": 70.0, "experience": 85.0, "futureProof": 84.0},
            strengths=[
                "Rugged retro-industrial chassis with robust component durability",
                "Dedicated G-key instantly boosts thermal fans for maximum cooling",
            ],
            concerns=["Heavier chassis at 2.65kg", "Average battery life when running discrete graphics"],
            source="demo",
        ),
        create_candidate_option(
            id="lenovo-ideapad-gaming-3",
            name="Lenovo IdeaPad Gaming 3",
            category="electronics",
            subcategory="laptop",
            price="₹47,990",
            description="AMD Ryzen 5 5600H, RTX 3050 4GB, 16GB DDR4, 120Hz IPS display, Rapid Charge",
            tags=["Ryzen 5", "RTX 3050", "16GB RAM", "Sub-₹50k"],
            attributes={"performance": 81.0, "value": 90.0, "battery": 74.0, "experience": 81.0, "futureProof": 76.0},
            strengths=[
                "Affordable high-value gaming and coding machine under ₹50,000",
                "Comfortable keyboard layout with standard arrow keys",
            ],
            concerns=["DDR4 memory architecture rather than modern DDR5", "Older generation CPU"],
            source="demo",
        ),
        create_candidate_option(
            id="asus-zephyrus-g14",
            name="ASUS ROG Zephyrus G14",
            category="electronics",
            subcategory="laptop",
            price="₹1,19,990",
            description="AMD Ryzen 9 8945HS, RTX 4060 8GB, 16GB LPDDR5X, 120Hz 3K OLED, 1.5kg CNC aluminum",
            tags=["Ryzen 9", "RTX 4060", "3K OLED", "Ultraportable", "1.5kg"],
            attributes={"performance": 95.0, "value": 72.0, "battery": 86.0, "experience": 97.0, "futureProof": 91.0},
            strengths=[
                "Pinnacle ultra-portable engineering weighing just 1.5kg",
                "Gorgeous 3K 120Hz OLED screen with 100% DCI-P3 color accuracy",
            ],
            concerns=["Premium luxury price tag", "Soldered RAM limits future hardware expansion"],
            source="demo",
        ),
        create_candidate_option(
            id="acer-predator-helios-neo",
            name="Acer Predator Helios Neo 16",
            category="electronics",
            subcategory="laptop",
            price="₹99,990",
            description="Intel Core i7-13700HX, RTX 4050 6GB, 16GB DDR5, 165Hz WUXGA 400 nits, Liquid Metal cooling",
            tags=["Core i7 HX", "RTX 4050", "165Hz", "Liquid Metal"],
            attributes={"performance": 93.0, "value": 80.0, "battery": 68.0, "experience": 89.0, "futureProof": 85.0},
            strengths=[
                "Liquid metal thermal compound delivers extraordinary sustained boost clocks",
                "16:10 aspect ratio display offers extra vertical space for code editors",
            ],
            concerns=["Aggressive gamer branding might not suit corporate boardrooms", "Bulky brick charger"],
            source="demo",
        ),
        create_candidate_option(
            id="msi-thin-gf63",
            name="MSI Thin GF63",
            category="electronics",
            subcategory="laptop",
            price="₹42,990",
            description="Intel Core i5-12450H, RTX 2050 4GB, 8GB DDR4, 144Hz IPS display, 1.86kg slim chassis",
            tags=["Core i5", "RTX 2050", "Slim Design", "Entry Budget"],
            attributes={"performance": 76.0, "value": 87.0, "battery": 71.0, "experience": 78.0, "futureProof": 72.0},
            strengths=[
                "One of the lightest budget gaming laptops available at 1.86kg",
                "Accessible entry price point",
            ],
            concerns=["Requires RAM upgrade to 16GB", "Single fan cooling architecture can run warm"],
            source="demo",
        ),
    ]

    def get_candidates(
        self,
        category: str,
        subcategory: str = "",
        decision: Optional[DecisionInputSchema] = None,
    ) -> List[Dict[str, Any]]:
        candidates = list(self.DEMO_LAPTOPS)
        if decision and decision.maxCandidates and decision.maxCandidates > 0:
            return candidates[:decision.maxCandidates]
        return candidates


class SmartphoneProvider(BaseCandidateProvider):
    """Provides dynamic candidate options for smartphones."""

    DEMO_PHONES = [
        create_candidate_option(
            id="oneplus-12r",
            name="OnePlus 12R (5G)",
            category="electronics",
            subcategory="smartphone",
            price="₹39,999",
            description="Snapdragon 8 Gen 2, 50MP Sony IMX890 OIS, 5500mAh battery, 100W charging, 1.5K LTPO4 120Hz",
            tags=["Snapdragon 8 Gen 2", "50MP OIS", "5500mAh", "100W", "LTPO4"],
            attributes={"performance": 93.0, "camera": 92.0, "battery": 94.0, "display": 93.0, "value": 91.0},
            strengths=[
                "Flagship-tier Snapdragon 8 Gen 2 chipset handles gaming and multi-tasking effortlessly",
                "Huge 5,500mAh cell with 100W flash charging (0–100% in under 28 mins)",
                "Vibrant 1.5K LTPO4 AMOLED with 4,500 nits peak outdoor brightness",
            ],
            concerns=[
                "Lacks dedicated telephoto zoom lens; relies on digital crop",
                "No official wireless charging support",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="xiaomi-13t-pro",
            name="Xiaomi 13T Pro",
            category="electronics",
            subcategory="smartphone",
            price="₹41,999",
            description="MediaTek Dimensity 9200+, 50MP Leica Optics with 2x Telephoto, 5000mAh, 120W HyperCharge",
            tags=["Dimensity 9200+", "Leica Optics", "120W Charging", "144Hz AMOLED", "IP68"],
            attributes={"performance": 91.0, "camera": 88.0, "battery": 84.0, "display": 90.0, "value": 85.0},
            strengths=[
                "Blazing 120W HyperCharge recovers 100% capacity in 19 minutes flat",
                "Co-engineered Leica Authentic and Vibrant optical color tuning modes",
                "Ultra-smooth 144Hz AMOLED screen with 2,600 nits peak brightness",
            ],
            concerns=[
                "HyperOS includes pre-installed promotional partner apps that require removal",
                "Slightly priced above strict sub-₹40k ceiling without bank offers",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="samsung-s23-fe",
            name="Samsung Galaxy S23 FE",
            category="electronics",
            subcategory="smartphone",
            price="₹38,999",
            description="Exynos 2200, 50MP Main with 3x Optical Telephoto, Dynamic AMOLED 2X 120Hz, IP68 rated",
            tags=["3x Telephoto", "IP68 Water Resistant", "DeX Mode", "Dynamic AMOLED", "One UI"],
            attributes={"performance": 87.0, "camera": 90.0, "battery": 79.0, "display": 91.0, "value": 84.0},
            strengths=[
                "Only option in price bracket with dedicated 3x optical telephoto lens",
                "Full IP68 dust and water submersion resistance rating",
                "Samsung DeX desktop workstation mode via USB-C",
            ],
            concerns=[
                "Battery runtime tops out at ~6 hours SOT under heavy cellular data use",
                "No power adapter included in retail packaging",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="nothing-phone-2",
            name="Nothing Phone (2)",
            category="electronics",
            subcategory="smartphone",
            price="₹36,999",
            description="Snapdragon 8+ Gen 1, Dual 50MP Sony sensors, Glyph Interface LEDs, 4700mAh, Nothing OS 2.5",
            tags=["Glyph Interface", "Snapdragon 8+", "Clean OS", "Wireless Charging", "Unique Design"],
            attributes={"performance": 89.0, "camera": 84.0, "battery": 85.0, "display": 90.0, "value": 86.0},
            strengths=[
                "Unique Glyph notification lighting with custom LED ringtone sequencing",
                "Extremely fast and bloat-free Nothing OS software experience",
                "Symmetrical slim display bezels with 1–120Hz LTPO refresh",
            ],
            concerns=[
                "Camera tuning occasionally exhibits oversaturated contrast in harsh sunlight",
                "Water resistance is splash-only IP54 rather than full submersion",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="google-pixel-8a",
            name="Google Pixel 8a",
            category="electronics",
            subcategory="smartphone",
            price="₹37,999",
            description="Google Tensor G3, 64MP Dual Camera with Best Take, 120Hz Actua OLED, 7-year OS updates",
            tags=["Tensor G3", "Best-in-Class Camera", "7yr Updates", "IP67", "Wireless Charging"],
            attributes={"performance": 85.0, "camera": 95.0, "battery": 81.0, "display": 89.0, "value": 88.0},
            strengths=[
                "Industry-leading computational photography and low-light portrait capture",
                "7 full years of guaranteed Android OS, feature drops, and security updates",
                "Clean stock Android interface with no bloatware or ads",
            ],
            concerns=[
                "18W wired charging speed is slower than competing fast chargers",
                "Slightly thicker display bezels compared to curved edge flagships",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="iqoo-neo-9-pro",
            name="iQOO Neo 9 Pro",
            category="electronics",
            subcategory="smartphone",
            price="₹34,999",
            description="Snapdragon 8 Gen 2, Supercomputing Chip Q1, 50MP Sony IMX920, 120W FlashCharge, 144Hz LTPO",
            tags=["Snapdragon 8 Gen 2", "Gaming Q1", "120W Charging", "144Hz"],
            attributes={"performance": 94.0, "camera": 86.0, "battery": 88.0, "display": 91.0, "value": 90.0},
            strengths=[
                "Top-tier esports gaming frame rates with dedicated Q1 graphics chip",
                "120W flash charge recovers 50% in 11 minutes",
            ],
            concerns=["FuntouchOS has minor pre-installed app recommendations", "No wireless charging"],
            source="demo",
        ),
        create_candidate_option(
            id="realme-gt-6t",
            name="Realme GT 6T",
            category="electronics",
            subcategory="smartphone",
            price="₹30,999",
            description="Snapdragon 7+ Gen 3, 6000 nits Hyper Display, 5500mAh battery, 120W SUPERVOOC charging",
            tags=["Snapdragon 7+ Gen 3", "6000 nits", "5500mAh", "120W"],
            attributes={"performance": 88.0, "camera": 83.0, "battery": 91.0, "display": 92.0, "value": 89.0},
            strengths=[
                "World-record 6,000 nits peak brightness panel for blazing outdoor visibility",
                "Massive 5500mAh cell with rapid 120W wired charge",
            ],
            concerns=["Secondary 8MP ultra-wide camera has modest resolution", "Plastic frame finish"],
            source="demo",
        ),
        create_candidate_option(
            id="motorola-edge-50-pro",
            name="Motorola Edge 50 Pro",
            category="electronics",
            subcategory="smartphone",
            price="₹31,999",
            description="Snapdragon 7 Gen 3, Pantone Validated 144Hz pOLED, 50MP OIS with 3x Telephoto, IP68, Vegan Leather",
            tags=["3x Telephoto", "IP68 Submersion", "125W Wired", "50W Wireless", "Vegan Leather"],
            attributes={"performance": 84.0, "camera": 89.0, "battery": 80.0, "display": 91.0, "value": 88.0},
            strengths=[
                "Includes dedicated 3x optical telephoto lens and 50W wireless charging",
                "Full IP68 water resistance with luxurious vegan leather back finish",
            ],
            concerns=["Smaller 4500mAh battery capacity compared to 5500mAh peers", "Processor throttles earlier"],
            source="demo",
        ),
    ]

    def get_candidates(
        self,
        category: str,
        subcategory: str = "",
        decision: Optional[DecisionInputSchema] = None,
    ) -> List[Dict[str, Any]]:
        candidates = list(self.DEMO_PHONES)
        if decision and decision.maxCandidates and decision.maxCandidates > 0:
            return candidates[:decision.maxCandidates]
        return candidates


class SmartwatchProvider(BaseCandidateProvider):
    """Provides dynamic candidate options for smartwatches."""

    DEMO_WATCHES = [
        create_candidate_option(
            id="garmin-forerunner-165",
            name="Garmin Forerunner 165",
            category="electronics",
            subcategory="smartwatch",
            price="₹14,990",
            description="Dual-frequency GPS, Elevate V4 optical HR, 1.2\" AMOLED, 11-day battery, HRV Status, 5 ATM",
            tags=["Dual-band GPS", "11-Day Battery", "HRV Status", "AMOLED", "Zero Subscriptions"],
            attributes={"fitness": 96.0, "battery": 95.0, "durability": 91.0, "display": 88.0, "value": 90.0},
            strengths=[
                "Pro-tier GPS accuracy and medical-grade heart rate correlation for runners",
                "11 days of real-world battery life completely eliminates daily charging anxiety",
                "Zero paywalled metrics; training plans and recovery insights are 100% free forever",
            ],
            concerns=[
                "Lacks built-in microphone for answering voice calls on the wrist",
                "Polymer bezel prioritizes athletic light weight over metallic jewelry luxury",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="fitbit-charge-6",
            name="Fitbit Charge 6",
            category="electronics",
            subcategory="smartwatch",
            price="₹11,990",
            description="Built-in GPS, Google Maps navigation, ECG app, EDA stress sensor, 7-day battery, 5 ATM water",
            tags=["Built-in GPS", "Google Integration", "Sleep Stages", "7-Day Battery", "Compact"],
            attributes={"fitness": 88.0, "battery": 88.0, "durability": 84.0, "display": 82.0, "value": 85.0},
            strengths=[
                "Slim lightweight fitness band form factor ideal for 24/7 sleep tracking",
                "Deep integration with Google Wallet contactless tap-and-pay",
                "7 days of continuous battery life with automatic workout detection",
            ],
            concerns=[
                "Smaller screen is less suited for reading long text notifications",
                "Comprehensive historical trend analytics require a Fitbit Premium subscription",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="amazfit-gtr-4",
            name="Amazfit GTR 4",
            category="electronics",
            subcategory="smartwatch",
            price="₹12,999",
            description="Dual-band circularly polarized GPS, BioTracker 4.0, 1.43\" AMOLED, 14-day battery, Bluetooth calls",
            tags=["14-Day Battery", "Bluetooth Calls", "Dual-band GPS", "Aluminum Alloy", "Offline Music"],
            attributes={"fitness": 86.0, "battery": 93.0, "durability": 87.0, "display": 90.0, "value": 91.0},
            strengths=[
                "Outstanding 14-day battery endurance with classic metallic watch styling",
                "Supports direct Bluetooth voice calling and offline onboard MP3 storage",
                "Large 1.43-inch sharp AMOLED display with anti-fingerprint coating",
            ],
            concerns=[
                "HR sensor accuracy dips slightly during high-intensity interval sprints",
                "Third-party app ecosystem is basic compared to WearOS or watchOS",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="apple-watch-se",
            name="Apple Watch SE (2nd Gen)",
            category="electronics",
            subcategory="smartwatch",
            price="₹24,900",
            description="Optical HR sensor V2, S8 SiP dual-core, Crash Detection, 1000 nits Retina OLED, 50m water",
            tags=["Apple Ecosystem", "Crash Detection", "Retina OLED", "watchOS 10", "Premium Haptics"],
            attributes={"fitness": 90.0, "battery": 70.0, "durability": 85.0, "display": 92.0, "value": 78.0},
            strengths=[
                "Flawless integration with iOS ecosystem, Apple Pay, and iMessage",
                "Class-leading Taptic Engine haptics and responsive watchOS animations",
                "Accurate heart rate monitoring and automatic high/low heart rate notifications",
            ],
            concerns=[
                "Strictly incompatible with Android smartphones",
                "Requires daily overnight charging (approx 18 hours standard battery life)",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="samsung-galaxy-watch-6",
            name="Samsung Galaxy Watch 6",
            category="electronics",
            subcategory="smartwatch",
            price="₹18,999",
            description="BioActive 3-in-1 Sensor, Sapphire Crystal glass, WearOS 4, 1.5\" Super AMOLED 2000 nits, ECG/BP",
            tags=["WearOS 4", "Sapphire Glass", "ECG & BP", "Google Play Apps", "Samsung Ecosystem"],
            attributes={"fitness": 89.0, "battery": 72.0, "durability": 88.0, "display": 94.0, "value": 80.0},
            strengths=[
                "Full WearOS smartwatch experience with Google Maps, Play Store, and WhatsApp",
                "Premium Sapphire Crystal front glass resists keys and scratches",
                "Advanced body composition analysis (BIA) and FDA-cleared ECG",
            ],
            concerns=[
                "Battery requires daily charging (approx 30–40 hours runtime)",
                "Select advanced health features (ECG/BP) require a paired Samsung Galaxy phone",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="coros-pace-3",
            name="COROS PACE 3",
            category="electronics",
            subcategory="smartwatch",
            price="₹19,990",
            description="Dual-frequency all-systems GPS, 30g featherweight, memory-in-pixel screen, 17-day battery, 5 ATM",
            tags=["Featherweight 30g", "17-Day Battery", "Dual GPS", "EvoLab Analytics"],
            attributes={"fitness": 95.0, "battery": 96.0, "durability": 88.0, "display": 82.0, "value": 89.0},
            strengths=[
                "Lightest dedicated marathon GPS watch at just 30 grams on the wrist",
                "Phenomenal 38 hours of continuous standard GPS workout recording",
            ],
            concerns=["Transflective display has muted indoor contrast without backlight", "No touch payment"],
            source="demo",
        ),
    ]

    def get_candidates(
        self,
        category: str,
        subcategory: str = "",
        decision: Optional[DecisionInputSchema] = None,
    ) -> List[Dict[str, Any]]:
        candidates = list(self.DEMO_WATCHES)
        if decision and decision.maxCandidates and decision.maxCandidates > 0:
            return candidates[:decision.maxCandidates]
        return candidates


class ElectronicsCandidateProvider(BaseCandidateProvider):
    """
    Main Electronics Candidate Provider.
    Routes to specialized subcategory providers (Laptop, Smartphone, Smartwatch, etc.).
    """

    def __init__(self):
        self.laptop_provider = LaptopProvider()
        self.smartphone_provider = SmartphoneProvider()
        self.smartwatch_provider = SmartwatchProvider()

    def get_candidates(
        self,
        category: str,
        subcategory: str = "",
        decision: Optional[DecisionInputSchema] = None,
    ) -> List[Dict[str, Any]]:
        sub = (subcategory or "").strip().lower()
        desc_lower = (decision.description if decision else "").lower()

        if sub == "laptop" or ("laptop" in desc_lower or "notebook" in desc_lower or "macbook" in desc_lower):
            return self.laptop_provider.get_candidates(category, sub, decision)
        elif sub == "smartphone" or ("phone" in desc_lower or "mobile" in desc_lower):
            return self.smartphone_provider.get_candidates(category, sub, decision)
        elif sub == "smartwatch" or ("watch" in desc_lower or "fitness band" in desc_lower):
            return self.smartwatch_provider.get_candidates(category, sub, decision)
        else:
            # Default to laptop provider
            return self.laptop_provider.get_candidates(category, sub, decision)
