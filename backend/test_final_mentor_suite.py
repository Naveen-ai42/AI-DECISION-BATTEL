"""
Mentor Requirements Live Verification Script for Decision Arena.
Executes live HTTP POST calls to http://127.0.0.1:8001/api/analysis for:
1. Laptop request: "I need a laptop under ₹60,000 for coding."
2. Smartphone request: "I need a smartphone under ₹30,000 with good camera."
3. Tablet request: "I need a tablet for studying."
4. Vehicle request: "I need a vehicle for family use."
5. Dynamic priority test: Smartphone with battery priority vs camera priority.
"""

import urllib.request
import json

BACKEND_URL = "http://127.0.0.1:8001/api/analysis"

def post_decision(payload):
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        BACKEND_URL,
        data=body,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=12) as resp:
        return json.loads(resp.read().decode("utf-8"))

def safe_str(val):
    return str(val).encode("ascii", errors="replace").decode("ascii")

def main():
    print("=" * 80)
    print("DECISION ARENA - MENTOR VERIFICATION LIVE HTTP SUITE")
    print("=" * 80)

    # 1. Laptop Request
    print("\n" + "=" * 80)
    print("1. LAPTOP TEST: 'I need a laptop under INR 60,000 for coding.'")
    print("=" * 80)
    laptop_payload = {
        "description": "I need a laptop under ₹60,000 for coding.",
        "category": "electronics",
        "subcategory": "laptop",
        "budget": "60000",
        "requirements": ["coding", "good performance"],
        "dealBreakers": ["poor build quality"],
        "priorities": {
            "performance": 35.0,
            "value": 20.0,
            "battery": 15.0,
            "display": 15.0,
            "build": 10.0,
            "upgradeability": 5.0
        },
        "decisionStyle": "best-overall",
        "riskTolerance": "balanced"
    }
    laptop_res = post_decision(laptop_payload)
    print(f"Status: {laptop_res.get('status')}")
    print(f"Category: {laptop_res.get('category')}")
    print(f"Subcategory: {laptop_res.get('subcategory')}")
    print(f"Factors: {[f['name'] for f in laptop_res.get('factors', [])]}")
    print(f"Candidate Count Evaluated: {laptop_res.get('candidateCount')}")
    print("Top 5 Ranked Candidates:")
    for idx, c in enumerate(laptop_res.get("rankedCandidates", [])[:5]):
        print(f"  #{c.get('rank')}: {c.get('name')} | Score: {c.get('overallScore')} | Price: {safe_str(c.get('price'))} | Why: {c.get('why')[:70]}...")
    print(f"Best Overall: {laptop_res.get('bestOverall', {}).get('name')} (Score: {laptop_res.get('bestOverall', {}).get('score')})")

    # 2. Smartphone Request
    print("\n" + "=" * 80)
    print("2. SMARTPHONE TEST: 'I need a smartphone under INR 30,000 with good camera.'")
    print("=" * 80)
    phone_payload = {
        "description": "I need a smartphone under ₹30,000 with good camera.",
        "category": "electronics",
        "subcategory": "smartphone",
        "budget": "30000",
        "requirements": ["good camera", "fast processor"],
        "dealBreakers": ["bloatware ads"],
        "priorities": {
            "camera": 40.0,
            "performance": 20.0,
            "battery": 20.0,
            "display": 10.0,
            "software": 5.0,
            "build": 3.0,
            "value": 2.0
        },
        "decisionStyle": "best-overall",
        "riskTolerance": "balanced"
    }
    phone_res = post_decision(phone_payload)
    print(f"Status: {phone_res.get('status')}")
    print(f"Category: {phone_res.get('category')}")
    print(f"Subcategory: {phone_res.get('subcategory')}")
    print(f"Factors: {[f['name'] for f in phone_res.get('factors', [])]}")
    print(f"Candidate Count Evaluated: {phone_res.get('candidateCount')}")
    print("Top 5 Ranked Candidates:")
    for idx, c in enumerate(phone_res.get("rankedCandidates", [])[:5]):
        print(f"  #{c.get('rank')}: {c.get('name')} | Score: {c.get('overallScore')} | Price: {safe_str(c.get('price'))} | Why: {c.get('why')[:70]}...")
    print(f"Best Overall: {phone_res.get('bestOverall', {}).get('name')} (Score: {phone_res.get('bestOverall', {}).get('score')})")

    # 3. Tablet Request
    print("\n" + "=" * 80)
    print("3. TABLET TEST: 'I need a tablet for studying.'")
    print("=" * 80)
    tablet_payload = {
        "description": "I need a tablet for studying.",
        "category": "electronics",
        "subcategory": "tablet",
        "requirements": ["studying", "note taking"],
        "dealBreakers": ["poor battery"],
        "priorities": {
            "display": 30.0,
            "battery": 25.0,
            "portability": 20.0,
            "performance": 10.0,
            "software": 5.0,
            "productivity": 5.0,
            "value": 5.0
        },
        "decisionStyle": "best-overall",
        "riskTolerance": "balanced"
    }
    tablet_res = post_decision(tablet_payload)
    print(f"Status: {tablet_res.get('status')}")
    print(f"Category: {tablet_res.get('category')}")
    print(f"Subcategory: {tablet_res.get('subcategory')}")
    print(f"Factors: {[f['name'] for f in tablet_res.get('factors', [])]}")
    print(f"Candidate Count Evaluated: {tablet_res.get('candidateCount')}")
    print("Top Candidates:")
    for idx, c in enumerate(tablet_res.get("rankedCandidates", [])[:5]):
        print(f"  #{c.get('rank')}: {c.get('name')} | Score: {c.get('overallScore')} | Price: {safe_str(c.get('price'))} | Why: {c.get('why')[:70]}...")
    print(f"Best Overall: {tablet_res.get('bestOverall', {}).get('name')} (Score: {tablet_res.get('bestOverall', {}).get('score')})")

    # 4. Vehicle Request
    print("\n" + "=" * 80)
    print("4. VEHICLE TEST: 'I need a vehicle for family use.'")
    print("=" * 80)
    vehicle_payload = {
        "description": "I need a vehicle for family use.",
        "category": "vehicle",
        "subcategory": "vehicle",
        "requirements": ["family comfort", "spacious cabin", "high safety"],
        "dealBreakers": ["low safety rating"],
        "priorities": {
            "safety": 35.0,
            "space": 25.0,
            "comfort": 20.0,
            "mileage": 10.0,
            "performance": 5.0,
            "maintenance": 3.0,
            "value": 2.0
        },
        "decisionStyle": "best-overall",
        "riskTolerance": "balanced"
    }
    vehicle_res = post_decision(vehicle_payload)
    print(f"Status: {vehicle_res.get('status')}")
    print(f"Category: {vehicle_res.get('category')}")
    print(f"Subcategory: {vehicle_res.get('subcategory')}")
    print(f"Factors: {[f['name'] for f in vehicle_res.get('factors', [])]}")
    print(f"Candidate Count Evaluated: {vehicle_res.get('candidateCount')}")
    print("Top 5 Ranked Candidates:")
    for idx, c in enumerate(vehicle_res.get("rankedCandidates", [])[:5]):
        print(f"  #{c.get('rank')}: {c.get('name')} | Score: {c.get('overallScore')} | Price: {safe_str(c.get('price'))} | Why: {c.get('why')[:70]}...")
    print(f"Best Overall: {vehicle_res.get('bestOverall', {}).get('name')} (Score: {vehicle_res.get('bestOverall', {}).get('score')})")

    # 5. Smartphone Battery Priority Shift Test
    print("\n" + "=" * 80)
    print("5. SMARTPHONE (BATTERY PRIORITY SHIFT TEST):")
    print("=" * 80)
    phone_battery_payload = dict(phone_payload)
    phone_battery_payload["priorities"] = {
        "battery": 45.0,
        "performance": 20.0,
        "camera": 15.0,
        "display": 10.0,
        "software": 5.0,
        "build": 3.0,
        "value": 2.0
    }
    phone_battery_res = post_decision(phone_battery_payload)
    camera_ranks = [c["name"] for c in phone_res.get("rankedCandidates", [])[:5]]
    battery_ranks = [c["name"] for c in phone_battery_res.get("rankedCandidates", [])[:5]]
    print(f"Camera Priorities Top 5: {camera_ranks}")
    print(f"Battery Priorities Top 5: {battery_ranks}")
    print(f"Rankings Shifted: {camera_ranks != battery_ranks}")

    print("\n" + "=" * 80)
    print("ALL MENTOR LIVE HTTP SCENARIOS COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    main()
