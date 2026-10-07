"""
Demo Candidate Provider for Decision Arena.
Provides realistic sample candidate pools with diverse attribute values
so that winners and rankings dynamically shift when user priorities, budget,
or requirements change.

Architecturally isolated: can be cleanly replaced with a real database or
external API provider without touching the decision engine.
"""

from typing import List, Dict, Any, Optional
from .base_provider import BaseCandidateProvider
from ..decision.factor_selector import get_decision_config

# Sample Candidate Pools across categories and subcategories
DEMO_CANDIDATES: Dict[str, List[Dict[str, Any]]] = {
    # =========================================================================
    # ELECTRONICS: SMARTPHONE
    # =========================================================================
    "electronics:smartphone": [
        {
            "id": "phone-pixel8a",
            "name": "Google Pixel 8a",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹31,999",
            "attributes": {
                "camera": 96.0,
                "software": 95.0,
                "display": 88.0,
                "performance": 84.0,
                "build": 86.0,
                "battery": 80.0,
                "value": 85.0,
            },
            "description": "Google Tensor G3, 64MP OIS camera, 7-year OS updates, Actua 120Hz display.",
            "strengths": [
                "Industry-leading computational photography and skin-tone rendering",
                "Clean Google Pixel experience with 7 years guaranteed OS updates",
                "Compact, pocket-friendly ergonomic aluminum architecture",
            ],
            "concerns": [
                "18W wired charging speed is noticeably slow compared to rivals",
                "Tensor G3 throttles peak frame rates during sustained 3D gaming",
            ],
            "tags": ["Best Camera", "Clean Android", "7-Year Updates"],
            "source": "demo",
        },
        {
            "id": "phone-oneplus12r",
            "name": "OnePlus 12R (5G)",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹35,999",
            "attributes": {
                "battery": 96.0,
                "performance": 94.0,
                "display": 92.0,
                "build": 88.0,
                "value": 86.0,
                "camera": 82.0,
                "software": 84.0,
            },
            "description": "Snapdragon 8 Gen 2, 5500mAh battery, 100W SUPERVOOC, 1.5K 120Hz ProXDR LTPO.",
            "strengths": [
                "Massive 5500mAh dual-cell battery with 100W blazing fast charger",
                "Flagship Snapdragon 8 Gen 2 processing with vapor chamber cooling",
                "Gorgeous 1.5K 120Hz LTPO 4.0 display with 4500 nits peak brightness",
            ],
            "concerns": [
                "Secondary cameras (8MP ultra-wide and 2MP macro) are average",
                "No official IP68 rating against deep water immersion",
            ],
            "tags": ["Battery Champion", "Sustained Gaming", "100W Fast Charge"],
            "source": "demo",
        },
        {
            "id": "phone-motoedge50pro",
            "name": "Motorola Edge 50 Pro",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹27,999",
            "attributes": {
                "value": 95.0,
                "build": 91.0,
                "display": 93.0,
                "camera": 88.0,
                "software": 89.0,
                "battery": 83.0,
                "performance": 82.0,
            },
            "description": "Snapdragon 7 Gen 3, Pantone Validated 1.5K 144Hz pOLED, 125W TurboPower, IP68.",
            "strengths": [
                "Aggressive sub-₹30,000 price point with flagship IP68 water resistance",
                "Stunning 144Hz curved pOLED display with true-to-life Pantone colors",
                "Clean Hello UI near-stock software without aggressive promotional ads",
            ],
            "concerns": [
                "4500mAh battery capacity offers only single-day battery reserve",
                "Snapdragon 7 Gen 3 is upper-mid silicon rather than flagship tier",
            ],
            "tags": ["Sub-30k Value", "IP68 Waterproof", "144Hz Display"],
            "source": "demo",
        },
        {
            "id": "phone-iqooneo9pro",
            "name": "iQOO Neo 9 Pro",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹32,999",
            "attributes": {
                "performance": 97.0,
                "battery": 90.0,
                "display": 91.0,
                "value": 90.0,
                "camera": 86.0,
                "build": 84.0,
                "software": 78.0,
            },
            "description": "Snapdragon 8 Gen 2 + Supercomputing Chip Q1, 120W FlashCharge, 144Hz LTPO AMOLED.",
            "strengths": [
                "Raw compute monster with dedicated Q1 display chip for 144 FPS frame interpolation",
                "120W FlashCharge powers to 50% in under 11 minutes",
                "Sony IMX920 50MP main sensor delivers great primary shots",
            ],
            "concerns": [
                "Funtouch OS includes promotional bloatware apps and notifications",
                "Plastic composite frame instead of aluminum",
            ],
            "tags": ["Extreme Performance", "Hardcore Gaming", "120W Fast Charge"],
            "source": "demo",
        },
        {
            "id": "phone-galaxy-a55",
            "name": "Samsung Galaxy A55 5G",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹36,999",
            "attributes": {
                "build": 95.0,
                "software": 92.0,
                "display": 93.0,
                "camera": 87.0,
                "battery": 86.0,
                "performance": 80.0,
                "value": 79.0,
            },
            "description": "Exynos 1480, Metal frame + Gorilla Glass Victus+, 50MP OIS, Samsung Knox Vault.",
            "strengths": [
                "Premium build with solid metal frame and Corning Gorilla Glass Victus+",
                "Samsung Knox Vault security with 4 OS upgrades and 5 years security patches",
                "Vibrant 120Hz Super AMOLED with high outdoor visibility",
            ],
            "concerns": [
                "Charging is capped at 25W and no power adapter in the retail box",
                "Exynos 1480 GPU struggles in heavy emulation and demanding 3D games",
            ],
            "tags": ["Premium Metal Build", "Enterprise Security", "Samsung Ecosystem"],
            "source": "demo",
        },
        {
            "id": "phone-redmi-note13pro",
            "name": "Redmi Note 13 Pro+ 5G",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹28,999",
            "attributes": {
                "value": 93.0,
                "camera": 89.0,
                "battery": 89.0,
                "display": 92.0,
                "build": 89.0,
                "performance": 83.0,
                "software": 76.0,
            },
            "description": "Dimensity 7200 Ultra, 200MP OIS camera, 120W HyperCharge, IP68 curved AMOLED.",
            "strengths": [
                "200MP high-res camera sensor with 4x in-sensor lossless crop",
                "120W HyperCharge included in the box with IP68 certification",
                "Sharp 1.5K 120Hz curved display with minimal bezels",
            ],
            "concerns": [
                "HyperOS interface carries promotional partner app recommendations",
                "Dimensity 7200 Ultra shows occasional thermal throttling under stress",
            ],
            "tags": ["200MP Camera", "Sub-30k Value", "IP68 Certified"],
            "source": "demo",
        },
        {
            "id": "phone-nothing-2a-plus",
            "name": "Nothing Phone (2a) Plus",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹24,999",
            "attributes": {
                "value": 96.0,
                "software": 91.0,
                "display": 89.0,
                "battery": 88.0,
                "build": 85.0,
                "camera": 82.0,
                "performance": 80.0,
            },
            "description": "Dimensity 7350 Pro, Glyph Interface, Nothing OS 2.6, 50MP dual cameras, 50W fast charge.",
            "strengths": [
                "Sub-₹25,000 pricing with distinctive transparent industrial aesthetic",
                "Nothing OS is exceptionally snappy, minimalist, and ad-free",
                "Symmetrical front bezels with bright 120Hz AMOLED panel",
            ],
            "concerns": [
                "Plastic polycarbonate back panel scratches more easily than glass",
                "Camera processing in low light is softer than Pixel or Samsung",
            ],
            "tags": ["Unique Design", "Clean Software", "Budget Friendly"],
            "source": "demo",
        },
        {
            "id": "phone-vivo-v30pro",
            "name": "Vivo V30 Pro",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹39,999",
            "attributes": {
                "camera": 94.0,
                "build": 90.0,
                "display": 91.0,
                "battery": 86.0,
                "performance": 85.0,
                "value": 81.0,
                "software": 80.0,
            },
            "description": "Dimensity 8200, ZEISS Co-engineered triple 50MP cameras, Smart Aura Light portrait.",
            "strengths": [
                "Triple 50MP ZEISS optics including dedicated 2x portrait telephoto lens",
                "Sleek and lightweight 7.45mm body with studio-grade Aura light",
                "Bright 1.5K 120Hz curved AMOLED screen",
            ],
            "concerns": [
                "Mono single bottom speaker (no stereo speakers)",
                "Priced near ₹40,000 where flagship chipsets are expected",
            ],
            "tags": ["ZEISS Optics", "Studio Portrait", "Ultra Slim"],
            "source": "demo",
        },
        {
            "id": "phone-oneplus-nord4",
            "name": "OnePlus Nord 4",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹29,999",
            "attributes": {
                "performance": 89.0,
                "camera": 82.0,
                "battery": 95.0,
                "display": 91.0,
                "software": 88.0,
                "build": 94.0,
                "value": 96.0,
            },
            "description": "Snapdragon 7+ Gen 3, 5500mAh battery, 100W charging, aluminum body, and 120Hz AMOLED display.",
            "strengths": [
                "Strong battery life with very fast wired charging",
                "Metal unibody construction at a midrange price",
                "Fast chipset for everyday use and gaming",
            ],
            "concerns": [
                "Camera versatility trails phones with a dedicated telephoto lens",
                "No expandable storage",
            ],
            "tags": ["Battery Focus", "Metal Build", "Value Pick"],
            "source": "demo",
        },
        {
            "id": "phone-samsung-s24fe",
            "name": "Samsung Galaxy S24 FE",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹59,999",
            "attributes": {
                "performance": 90.0,
                "camera": 93.0,
                "battery": 85.0,
                "display": 94.0,
                "software": 96.0,
                "build": 94.0,
                "value": 78.0,
            },
            "description": "Exynos 2400e, triple rear cameras with optical zoom, AMOLED display, and long-term software support.",
            "strengths": [
                "Versatile camera system with a dedicated telephoto lens",
                "Long software support and broad accessory availability",
                "Bright AMOLED display with a premium water-resistant build",
            ],
            "concerns": [
                "Charging is slower than several similarly priced competitors",
                "Battery endurance is good but not a category leader",
            ],
            "tags": ["Camera Versatility", "Long Software Support", "Premium Build"],
            "source": "demo",
        },
        {
            "id": "phone-iphone15",
            "name": "Apple iPhone 15",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹59,900",
            "attributes": {
                "performance": 98.0,
                "camera": 94.0,
                "battery": 84.0,
                "display": 88.0,
                "software": 97.0,
                "build": 94.0,
                "value": 73.0,
            },
            "description": "A16 Bionic, 48MP main camera, USB-C, and a compact OLED display with long iOS support.",
            "strengths": [
                "Fast and consistent performance across demanding apps",
                "Reliable video capture and a strong main camera",
                "Long software support and a compact premium design",
            ],
            "concerns": [
                "Display refresh rate is lower than many similarly priced Android phones",
                "Charging speed and included storage are modest for the price",
            ],
            "tags": ["Performance", "Video Camera", "Long Software Support"],
            "source": "demo",
        },
        {
            "id": "phone-iqoo12",
            "name": "iQOO 12",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹52,999",
            "attributes": {
                "performance": 99.0,
                "camera": 93.0,
                "battery": 90.0,
                "display": 96.0,
                "software": 80.0,
                "build": 89.0,
                "value": 87.0,
            },
            "description": "Snapdragon 8 Gen 3, 144Hz AMOLED display, 120W charging, and a triple-camera system with telephoto.",
            "strengths": [
                "Flagship-level gaming and sustained performance",
                "High-refresh display and fast charging",
                "More versatile cameras than most gaming-focused phones",
            ],
            "concerns": [
                "Preinstalled apps and interface polish may not suit every user",
                "Large display and fast chipset can reduce battery life under heavy use",
            ],
            "tags": ["Flagship Performance", "Gaming", "Fast Charging"],
            "source": "demo",
        },
        {
            "id": "phone-pixel9",
            "name": "Google Pixel 9",
            "category": "electronics",
            "subcategory": "smartphone",
            "price": "₹79,999",
            "attributes": {
                "performance": 89.0,
                "camera": 98.0,
                "battery": 87.0,
                "display": 94.0,
                "software": 98.0,
                "build": 93.0,
                "value": 68.0,
            },
            "description": "Tensor G4, computational photography, bright OLED display, and extended Android and security updates.",
            "strengths": [
                "Excellent still photography and computational image processing",
                "Clean software with an extended update commitment",
                "Premium build and bright high-refresh OLED display",
            ],
            "concerns": [
                "Price-to-performance is weaker than several gaming-focused competitors",
                "Charging and sustained heavy-load performance are not category leaders",
            ],
            "tags": ["Camera Champion", "Clean Android", "Long Software Support"],
            "source": "demo",
        },
    ],

    # =========================================================================
    # ELECTRONICS: LAPTOP
    # =========================================================================
    "electronics:laptop": [
        {
            "id": "laptop-asus-tuf-a15",
            "name": "ASUS TUF Gaming A15",
            "category": "electronics",
            "subcategory": "laptop",
            "price": "₹74,990",
            "attributes": {
                "upgradeability": 94.0,
                "performance": 91.0,
                "value": 92.0,
                "build": 87.0,
                "battery": 85.0,
                "display": 84.0,
            },
            "description": "AMD Ryzen 7 7735HS, 16GB DDR5, 512GB NVMe, RTX 4060 8GB (140W), 90Wh Battery.",
            "strengths": [
                "Full-powered RTX 4060 with 140W max TGP and MUX switch",
                "Dual accessible SO-DIMM RAM slots and dual M.2 NVMe SSD expansion bays",
                "Generous 90Wh battery offering up to 7 hours of non-gaming battery life",
            ],
            "concerns": [
                "Acoustic fan resonance is distinctly audible under heavy GPU compile loads",
                "Display panel is standard 250 nits FHD with 100% sRGB rather than wide-gamut",
            ],
            "tags": ["High Upgradeability", "RTX 4060", "90Wh Battery"],
            "source": "demo",
        },
        {
            "id": "laptop-macbook-air-m2",
            "name": "Apple MacBook Air 13\" M2",
            "category": "electronics",
            "subcategory": "laptop",
            "price": "₹89,900",
            "attributes": {
                "battery": 98.0,
                "build": 97.0,
                "display": 93.0,
                "performance": 87.0,
                "value": 82.0,
                "upgradeability": 40.0,
            },
            "description": "Apple M2 (8-core CPU, 8-core GPU), 8GB/16GB Unified Memory, 256GB SSD, Liquid Retina.",
            "strengths": [
                "Unmatched 16-18 hours real-world battery endurance on a single charge",
                "Completely fanless, 100% silent operation in a 1.24kg slim aluminum body",
                "500-nit Liquid Retina display with P3 wide color and crisp scaling",
            ],
            "concerns": [
                "Zero internal upgradeability: memory and storage are permanently soldered",
                "Base model has only 8GB unified memory and single external display support",
            ],
            "tags": ["Battery King", "Silent Fanless", "Ultra-Portable"],
            "source": "demo",
        },
        {
            "id": "laptop-lenovo-legion5",
            "name": "Lenovo Legion Pro 5 Gen 8",
            "category": "electronics",
            "subcategory": "laptop",
            "price": "₹1,12,000",
            "attributes": {
                "performance": 97.0,
                "display": 96.0,
                "build": 92.0,
                "upgradeability": 92.0,
                "value": 81.0,
                "battery": 74.0,
            },
            "description": "Intel Core i7-14700HX, 16GB DDR5, 1TB SSD, RTX 4070 8GB, 16\" WQXGA 240Hz 500 nits.",
            "strengths": [
                "Dominant workstation compute throughput with 20-core i7-14700HX and RTX 4070",
                "Sublime 16:10 240Hz WQXGA (2560x1600) 500-nit panel with factory calibration",
                "Legion Coldfront 5.0 vapor-chamber thermal system keeps temps stable",
            ],
            "concerns": [
                "Heavy 2.5kg chassis paired with a bulky 300W power brick reduces mobility",
                "Battery runtime drains in under 3.5 hours away from wall power",
            ],
            "tags": ["Max Performance", "240Hz 500-Nit Screen", "RTX 4070"],
            "source": "demo",
        },
        {
            "id": "laptop-acer-nitro-v15",
            "name": "Acer Nitro V 15",
            "category": "electronics",
            "subcategory": "laptop",
            "price": "₹54,990",
            "attributes": {
                "value": 96.0,
                "upgradeability": 88.0,
                "performance": 84.0,
                "build": 79.0,
                "display": 78.0,
                "battery": 76.0,
            },
            "description": "Intel Core i5-13420H, 16GB RAM, 512GB SSD, RTX 3050 6GB, 15.6\" 144Hz FHD.",
            "strengths": [
                "Extremely competitive sub-₹55,000 price point for a 16GB RAM gaming machine",
                "Dedicated RTX 3050 6GB VRAM handles entry esports and 1080p video editing",
                "Dual internal RAM slots expandable up to 32GB",
            ],
            "concerns": [
                "All-plastic chassis construction flexes slightly under pressure",
                "54Wh battery depletes quickly and display is 45% NTSC color gamut",
            ],
            "tags": ["Budget King", "Sub-55k Value", "RTX 3050 6GB"],
            "source": "demo",
        },
        {
            "id": "laptop-zephyrus-g14",
            "name": "ASUS ROG Zephyrus G14 (2024)",
            "category": "electronics",
            "subcategory": "laptop",
            "price": "₹1,34,990",
            "attributes": {
                "display": 98.0,
                "build": 96.0,
                "performance": 94.0,
                "battery": 88.0,
                "value": 75.0,
                "upgradeability": 70.0,
            },
            "description": "AMD Ryzen 9 8945HS, 16GB LPDDR5X, 1TB SSD, RTX 4060, 3K 120Hz ROG Nebula OLED.",
            "strengths": [
                "Gorgeous 3K 120Hz 0.2ms ROG Nebula OLED panel with infinite contrast and HDR",
                "CNC-milled unibody aluminum chassis weighing only 1.5kg",
                "Ryzen AI NPU accelerator and impressive 9-hour battery life for an ultraportable",
            ],
            "concerns": [
                "High price point above ₹1.3 lakh",
                "Soldered LPDDR5X RAM prevents post-purchase RAM expansion",
            ],
            "tags": ["3K OLED Screen", "CNC Aluminum", "Ultra-Slim 1.5kg"],
            "source": "demo",
        },
        {
            "id": "laptop-hp-victus16",
            "name": "HP Victus 16",
            "category": "electronics",
            "subcategory": "laptop",
            "price": "₹68,990",
            "attributes": {
                "value": 90.0,
                "upgradeability": 90.0,
                "performance": 86.0,
                "build": 83.0,
                "battery": 82.0,
                "display": 82.0,
            },
            "description": "AMD Ryzen 5 7640HS, 16GB DDR5, 512GB SSD, RTX 4050 6GB, 16.1\" FHD 144Hz.",
            "strengths": [
                "Large 16.1-inch screen with good thermal dissipation",
                "Modern Ryzen 7000 Zen 4 architecture with DDR5 memory bandwidth",
                "Dual SSD slots for future drive expansion",
            ],
            "concerns": [
                "Noticeable display hinge wobble when typing vigorously",
                "Keyboard backlight is single-zone white rather than RGB",
            ],
            "tags": ["16-Inch Screen", "Balanced Price", "Zen 4 CPU"],
            "source": "demo",
        },
        {
            "id": "laptop-dell-g15",
            "name": "Dell G15 5530",
            "category": "electronics",
            "subcategory": "laptop",
            "price": "₹78,990",
            "attributes": {
                "upgradeability": 91.0,
                "performance": 89.0,
                "build": 89.0,
                "display": 85.0,
                "value": 84.0,
                "battery": 78.0,
            },
            "description": "Intel Core i7-13650HX, 16GB DDR5, 1TB SSD, RTX 4050 6GB, Alienware-inspired thermals.",
            "strengths": [
                "Alienware-inspired thermal cooling architecture with Game Shift boost",
                "Robust, rigid chassis built like a tank",
                "Generous 1TB high-speed PCIe Gen 4 SSD standard",
            ],
            "concerns": [
                "Heavier than most laptops in its class at 2.8kg",
                "Alienware Command Center software can feel bloated",
            ],
            "tags": ["Alienware Thermals", "Rigid Tank Build", "1TB SSD"],
            "source": "demo",
        },
    ],

    # =========================================================================
    # ELECTRONICS: SMARTWATCH
    # =========================================================================
    "electronics:smartwatch": [
        {
            "id": "watch-garmin-165",
            "name": "Garmin Forerunner 165",
            "category": "electronics",
            "subcategory": "smartwatch",
            "price": "₹27,490",
            "attributes": {
                "healthFitness": 97.0,
                "battery": 94.0,
                "comfort": 93.0,
                "durability": 90.0,
                "compatibility": 92.0,
                "value": 88.0,
                "smartFeatures": 76.0,
            },
            "description": "AMOLED touch display, multi-band GPS, HRV status, Garmin Coach, 11-day battery.",
            "strengths": [
                "Industry-gold standard biometric tracking: HRV status, recovery time, training load",
                "Up to 11 days continuous battery runtime in smartwatch mode",
                "Featherweight 39g chassis designed for 24/7 sleep and running comfort",
            ],
            "concerns": [
                "No microphone or speaker for taking wrist phone calls",
                "Watch case is lightweight fiber-reinforced polymer instead of stainless steel",
            ],
            "tags": ["Marathon Training", "11-Day Battery", "HRV Analytics"],
            "source": "demo",
        },
        {
            "id": "watch-apple-s9",
            "name": "Apple Watch Series 9",
            "category": "electronics",
            "subcategory": "smartwatch",
            "price": "₹38,900",
            "attributes": {
                "smartFeatures": 98.0,
                "healthFitness": 92.0,
                "comfort": 92.0,
                "durability": 88.0,
                "value": 80.0,
                "battery": 68.0,
                "compatibility": 70.0,
            },
            "description": "S9 SiP chip, Double Tap gesture, 2000 nits Always-On display, ECG, Apple Pay.",
            "strengths": [
                "Unmatched smartwatch ecosystem: rich notifications, watch apps, Siri, Apple Pay",
                "FDA-cleared ECG sensor, blood oxygen, temperature sensing, and fall detection",
                "Intuitive Double Tap hand gesture for single-handed control",
            ],
            "concerns": [
                "18-hour battery endurance requires mandatory daily charging",
                "Completely incompatible with Android smartphones",
            ],
            "tags": ["Ultimate Smart Ecosystem", "ECG Certified", "Double Tap"],
            "source": "demo",
        },
        {
            "id": "watch-galaxy6",
            "name": "Samsung Galaxy Watch 6",
            "category": "electronics",
            "subcategory": "smartwatch",
            "price": "₹21,999",
            "attributes": {
                "smartFeatures": 94.0,
                "value": 90.0,
                "comfort": 90.0,
                "healthFitness": 89.0,
                "durability": 87.0,
                "compatibility": 85.0,
                "battery": 72.0,
            },
            "description": "Wear OS 4 (One UI Watch 5), Sapphire Crystal, BIA body composition sensor, Google Maps.",
            "strengths": [
                "Wear OS app ecosystem: Google Assistant, Google Maps, WhatsApp, and Play Store",
                "BIA biometric sensor measures body fat percentage, skeletal muscle, and body water",
                "Slim rotating bezel aesthetics with durable sapphire crystal display",
            ],
            "concerns": [
                "30-40 hour battery life requires charging every 1-2 days",
                "Certain advanced metrics (blood pressure, ECG) require a paired Samsung phone",
            ],
            "tags": ["Wear OS Ecosystem", "BIA Body Composition", "Sapphire Glass"],
            "source": "demo",
        },
        {
            "id": "watch-amazfit-active",
            "name": "Amazfit Active Edge",
            "category": "electronics",
            "subcategory": "smartwatch",
            "price": "₹12,999",
            "attributes": {
                "battery": 98.0,
                "value": 96.0,
                "comfort": 88.0,
                "durability": 88.0,
                "compatibility": 94.0,
                "healthFitness": 85.0,
                "smartFeatures": 78.0,
            },
            "description": "16-day battery life, 10 ATM water resistance, 5 satellite GPS systems, Zepp Coach.",
            "strengths": [
                "Astounding 16-day typical battery runtime off a single USB charge",
                "10 ATM water resistance rating suitable for serious swimming and watersports",
                "Unbeatable price-to-battery ratio with universal iOS and Android pairing",
            ],
            "concerns": [
                "Zepp OS has a limited third-party application catalog",
                "Optical HR sensor shows slight delay during rapid HIIT heart rate spikes",
            ],
            "tags": ["16-Day Battery", "10 ATM Water Resistance", "Sub-13k Value"],
            "source": "demo",
        },
        {
            "id": "watch-coros-pace3",
            "name": "Coros Pace 3",
            "category": "electronics",
            "subcategory": "smartwatch",
            "price": "₹24,999",
            "attributes": {
                "healthFitness": 95.0,
                "battery": 96.0,
                "comfort": 96.0,
                "compatibility": 93.0,
                "value": 91.0,
                "durability": 87.0,
                "smartFeatures": 70.0,
            },
            "description": "Dual-frequency GPS, 30g ultralight, 17-day battery / 38hr GPS, EvoLab training hub.",
            "strengths": [
                "Extremely lightweight 30-gram design that virtually disappears on your wrist",
                "Incredible 38 hours continuous active GPS tracking time",
                "Free professional training hub and metrics with zero subscription paywalls",
            ],
            "concerns": [
                "Memory-in-pixel display is dim in low-light environments without backlight",
                "Very basic smart notification support (no voice calls, no smart replies)",
            ],
            "tags": ["Ultralight 30g", "38hr GPS Endurance", "No Subscriptions"],
            "source": "demo",
        },
    ],

    # =========================================================================
    # FINANCE: INVESTMENT
    # =========================================================================
    "finance:investment": [
        {
            "id": "fin-index-fund",
            "name": "Nifty 50 & Flexi-Cap Index Allocation",
            "category": "finance",
            "subcategory": "investment",
            "price": "₹500/mo SIP min",
            "attributes": {
                "growth": 94.0,
                "liquidity": 92.0,
                "risk": 88.0,
                "returnPotential": 86.0,
                "stability": 85.0,
            },
            "description": "Low-cost index fund basket tracking India's top 50 enterprises and multi-cap leaders.",
            "strengths": [
                "12-14% historic 7-year annualized compounding with ultra-low 0.15% expense ratio",
                "High liquidity: T+2 business day redemption settlement with zero exit load after 1 year",
                "Zero individual stock selection risk or manager turnover risk",
            ],
            "concerns": [
                "Subject to market volatility drawdowns during macroeconomic corrections",
            ],
            "tags": ["Passive Compounding", "Low Expense Drag", "High Liquidity"],
            "source": "demo",
        },
        {
            "id": "fin-sovereign-bond",
            "name": "Sovereign Gold Bonds (SGB) & G-Sec Baskets",
            "category": "finance",
            "subcategory": "investment",
            "price": "₹1,000 face value",
            "attributes": {
                "stability": 98.0,
                "risk": 96.0,
                "growth": 84.0,
                "returnPotential": 82.0,
                "liquidity": 70.0,
            },
            "description": "Government of India sovereign backed securities with 2.5% annual coupon + gold price upside.",
            "strengths": [
                "Sovereign sovereign credit guarantee eliminating institutional default risk",
                "Tax-free capital gains upon 8-year maturity redemption",
                "Proven hedge against currency inflation and equity market turbulence",
            ],
            "concerns": [
                "8-year maturity duration limits instant liquidity on secondary market",
            ],
            "tags": ["Sovereign Guarantee", "Tax-Free Capital Gains", "Inflation Hedge"],
            "source": "demo",
        },
        {
            "id": "fin-liquid-fund",
            "name": "Ultra-Short Liquid & Arbitrage Fund",
            "category": "finance",
            "subcategory": "investment",
            "price": "Instant redemption",
            "attributes": {
                "liquidity": 98.0,
                "stability": 96.0,
                "risk": 95.0,
                "returnPotential": 72.0,
                "growth": 70.0,
            },
            "description": "High-safety parking vehicle for emergency liquidity in commercial paper and arbitrage spreads.",
            "strengths": [
                "Instant redemption up to ₹50,000 within minutes 24/7",
                "Virtually zero equity market volatility risk with steady 6.8-7.2% annualized yield",
                "Ideal capital parking solution for near-term cash requirements",
            ],
            "concerns": [
                "Yield barely outpaces inflation over multi-year horizons",
            ],
            "tags": ["Instant Liquidity", "Zero Equity Risk", "Emergency Parking"],
            "source": "demo",
        },
        {
            "id": "fin-midcap-fund",
            "name": "High-Alpha Active Mid-Cap Fund",
            "category": "finance",
            "subcategory": "investment",
            "price": "₹1,000/mo SIP min",
            "attributes": {
                "growth": 97.0,
                "returnPotential": 96.0,
                "liquidity": 88.0,
                "risk": 68.0,
                "stability": 65.0,
            },
            "description": "Aggressive growth mutual fund focused on emerging category leaders and disruptors.",
            "strengths": [
                "18-22% bull-market upside potential over 5+ year investment cycles",
                "Generates high alpha above benchmark indices during expansionary economies",
                "Managed by experienced fund team with proven stock-picking track record",
            ],
            "concerns": [
                "Higher volatility with potential 20-30% portfolio drawdowns in downturns",
            ],
            "tags": ["High Growth Upside", "Alpha Generation", "Aggressive"],
            "source": "demo",
        },
    ],

    # =========================================================================
    # CAREER: JOB
    # =========================================================================
    "career:job": [
        {
            "id": "career-data-science",
            "name": "Senior Applied AI Engineer (Growth Tech)",
            "category": "career",
            "subcategory": "job",
            "price": "₹38-45 LPA + Equity",
            "attributes": {
                "salary": 94.0,
                "growth": 93.0,
                "skillFit": 92.0,
                "learning": 91.0,
                "location": 90.0,
                "stability": 86.0,
                "workLifeBalance": 82.0,
            },
            "description": "Leading product AI LLM integration, agentic pipelines, and core retrieval architecture.",
            "strengths": [
                "Top-tier compensation package with meaningful employee stock equity upside",
                "Hands-on exposure to frontier multi-agent systems and foundation models",
                "Fast promotion cycle in a profitable, rapidly expanding division",
            ],
            "concerns": [
                "Occasional sprint crunch during major release cycles",
            ],
            "tags": ["High Compensation", "Frontier AI Stack", "Equity Upside"],
            "source": "demo",
        },
        {
            "id": "career-enterprise-arch",
            "name": "Principal Systems Engineer (Enterprise Cloud)",
            "category": "career",
            "subcategory": "job",
            "price": "₹42-50 LPA",
            "attributes": {
                "stability": 96.0,
                "workLifeBalance": 92.0,
                "salary": 93.0,
                "skillFit": 90.0,
                "location": 91.0,
                "learning": 86.0,
                "growth": 85.0,
            },
            "description": "Directing resilient cloud microservices, Kubernetes clusters, and 99.999% SLA platforms.",
            "strengths": [
                "Exceptional job security and revenue backing at a Fortune 500 tech leader",
                "Predictable 40-hour work weeks with hybrid flexibility and generous PTO",
                "Solid base salary with stable annual retention bonuses",
            ],
            "concerns": [
                "Architectural governance reviews can move more deliberately than startups",
            ],
            "tags": ["Maximum Job Stability", "Great Work-Life Balance", "Established Leader"],
            "source": "demo",
        },
        {
            "id": "career-fintech-lead",
            "name": "Founding Engineer (Fintech Series-A)",
            "category": "career",
            "subcategory": "job",
            "price": "₹32-40 LPA + 1.2% Equity",
            "attributes": {
                "growth": 97.0,
                "learning": 96.0,
                "salary": 88.0,
                "skillFit": 89.0,
                "location": 85.0,
                "stability": 74.0,
                "workLifeBalance": 72.0,
            },
            "description": "Building high-frequency real-time payment reconciliation and ledger systems from ground zero.",
            "strengths": [
                "Maximum autonomy, ownership, and direct impact on company architecture",
                "1.2% equity grant offering massive financial upside if company reaches IPO",
                "Steepest learning curve across infrastructure, product, and leadership",
            ],
            "concerns": [
                "Runway tied to investor milestones; requires high tolerance for ambiguity",
                "Frequent evening deployments and intensive sprint commitments",
            ],
            "tags": ["High Equity Upside", "Founding Impact", "Steep Learning"],
            "source": "demo",
        },
    ],
}


class DemoCandidateProvider(BaseCandidateProvider):
    """
    Demo candidate provider implementation.
    Returns dynamic candidate pools for testing and demonstration.
    Can be seamlessly substituted with a DatabaseCandidateProvider
    or ExternalAPICandidateProvider.
    """

    def get_candidates(
        self,
        category: str,
        subcategory: Optional[str] = None,
        decision: Optional[Any] = None,
    ) -> List[Dict[str, Any]]:
        cat = (category or "electronics").strip().lower()
        sub = (subcategory or "").strip().lower()
        composite_key = f"{cat}:{sub}"

        # 1. Look up exact composite key (e.g. electronics:smartphone)
        if composite_key in DEMO_CANDIDATES:
            candidates = [dict(c) for c in DEMO_CANDIDATES[composite_key]]
        else:
            # Keep fallback candidates scoped to the exact requested domain.
            candidates = self._generate_generic_candidates(cat, sub)

        # 3. Dynamic candidate pool size support:
        # If decision specifies maxCandidates, we can expand or slice
        if decision and hasattr(decision, "maxCandidates") and decision.maxCandidates:
            limit = int(decision.maxCandidates)
            if limit < len(candidates):
                candidates = candidates[:limit]
            elif limit > len(candidates):
                # Synthesize variations to support testing large pools (20, 50, 100+ candidates)
                expanded: List[Dict[str, Any]] = list(candidates)
                idx = 1
                base_len = len(candidates)
                while len(expanded) < limit:
                    seed = candidates[(idx - 1) % base_len]
                    variant = dict(seed)
                    variant["id"] = f"{seed['id']}-v{idx}"
                    variant["name"] = f"{seed['name']} (Spec Variant #{idx})"
                    variant["attributes"] = {
                        k: max(40.0, min(99.0, round(v + ((idx % 5) - 2) * 1.8, 1)))
                        for k, v in seed.get("attributes", {}).items()
                    }
                    expanded.append(variant)
                    idx += 1
                candidates = expanded

        return candidates

    def _generate_generic_candidates(self, category: str, subcategory: str) -> List[Dict[str, Any]]:
        """
        Synthesizes realistic candidates for unseeded categories.
        """
        label = subcategory.title() if subcategory else category.title()
        factor_keys = [factor.key for factor in get_decision_config(category, subcategory).factors]
        premium_profile = {
            "safety": 95.0, "stability": 92.0, "durability": 92.0, "maintenance": 90.0,
            "comfort": 91.0, "space": 91.0, "performance": 91.0, "skillFit": 92.0,
            "learning": 91.0, "growth": 90.0, "returnPotential": 89.0, "salary": 90.0,
            "workLifeBalance": 84.0, "value": 72.0, "mileage": 78.0, "liquidity": 82.0,
            "interestRate": 74.0, "emi": 78.0, "totalCost": 76.0,
            "tenure": 86.0, "eligibility": 88.0, "display": 99.0, "battery": 88.0,
            "portability": 87.0, "productivity": 84.0, "soundQuality": 94.0,
            "noiseCancellation": 90.0, "connectivity": 90.0,
            "academicQuality": 96.0, "cost": 72.0, "placements": 90.0,
            "experience": 90.0, "futureOpportunity": 95.0, "convenience": 82.0,
            "attractions": 96.0, "price": 72.0, "quality": 96.0, "features": 92.0,
            "reviews": 90.0, "optionFit": 94.0, "longTermImpact": 95.0,
            "risk": 94.0,
        }
        value_profile = {
            "safety": 84.0, "stability": 85.0, "durability": 84.0, "maintenance": 88.0,
            "comfort": 82.0, "space": 83.0, "performance": 83.0, "skillFit": 84.0,
            "learning": 82.0, "growth": 80.0, "returnPotential": 80.0, "salary": 82.0,
            "workLifeBalance": 86.0, "value": 97.0, "mileage": 96.0, "liquidity": 96.0,
            "interestRate": 96.0, "emi": 96.0, "totalCost": 96.0,
            "tenure": 82.0, "eligibility": 84.0, "display": 84.0, "battery": 96.0,
            "portability": 95.0, "productivity": 84.0, "soundQuality": 84.0,
            "noiseCancellation": 96.0, "connectivity": 84.0,
            "academicQuality": 82.0, "cost": 96.0, "placements": 84.0,
            "experience": 85.0, "futureOpportunity": 82.0, "convenience": 95.0,
            "attractions": 82.0, "price": 96.0, "quality": 84.0, "features": 86.0,
            "reviews": 86.0, "optionFit": 84.0, "longTermImpact": 82.0,
            "risk": 84.0,
        }
        specialist_profile = {
            "safety": 88.0, "stability": 80.0, "durability": 87.0, "maintenance": 94.0,
            "comfort": 85.0, "space": 96.0, "performance": 96.0, "skillFit": 88.0,
            "learning": 96.0, "growth": 96.0, "returnPotential": 96.0, "salary": 88.0,
            "workLifeBalance": 76.0, "value": 86.0, "mileage": 87.0, "liquidity": 88.0,
            "interestRate": 84.0, "emi": 82.0, "totalCost": 84.0,
            "tenure": 96.0, "eligibility": 96.0, "display": 88.0, "battery": 87.0,
            "portability": 88.0, "productivity": 96.0, "soundQuality": 96.0,
            "noiseCancellation": 86.0, "connectivity": 95.0,
            "academicQuality": 90.0, "cost": 84.0, "placements": 96.0,
            "experience": 96.0, "futureOpportunity": 96.0, "convenience": 88.0,
            "attractions": 92.0, "price": 86.0, "quality": 90.0, "features": 96.0,
            "reviews": 96.0, "optionFit": 96.0, "longTermImpact": 96.0,
            "risk": 88.0,
        }

        def profile_attributes(profile: Dict[str, float], default: float) -> Dict[str, float]:
            attributes = {
                "price": 86.0,
                "quality": 88.0,
                "features": 88.0,
                "reviews": 86.0,
                "durability": profile.get("durability", 88.0),
            }
            attributes.update({key: profile.get(key, default) for key in factor_keys})
            return attributes

        return [
            {
                "id": f"{category}-opt-1",
                "name": f"Premium {label} Choice",
                "category": category,
                "subcategory": subcategory,
                "price": "Standard Pricing",
                "attributes": profile_attributes(premium_profile, 88.0),
                "description": f"High-tier {label} offering top reliability and feature depth.",
                "strengths": ["Premium build quality", "Comprehensive feature set"],
                "concerns": ["Slightly higher premium cost"],
                "tags": ["Premium Pick", "High Quality"],
                "source": "demo",
            },
            {
                "id": f"{category}-opt-2",
                "name": f"Value-Balanced {label} Choice",
                "category": category,
                "subcategory": subcategory,
                "price": "Competitive Value",
                "attributes": profile_attributes(value_profile, 84.0),
                "description": f"Cost-effective {label} delivering exceptional value for money.",
                "strengths": ["Outstanding price-to-performance", "Reliable core functionality"],
                "concerns": ["Fewer luxury secondary perks"],
                "tags": ["Value Pick", "Budget Friendly"],
                "source": "demo",
            },
            {
                "id": f"{category}-opt-3",
                "name": f"Specialized {label} Alternative",
                "category": category,
                "subcategory": subcategory,
                "price": "Market Average",
                "attributes": profile_attributes(specialist_profile, 86.0),
                "description": f"Specialized {label} optimized for unique domain priorities.",
                "strengths": ["Targeted feature optimization", "Solid user ratings"],
                "concerns": ["Narrower specialization"],
                "tags": ["Specialized", "Domain Optimized"],
                "source": "demo",
            },
        ]
