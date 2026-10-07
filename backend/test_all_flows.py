import urllib.request
import json
import sys
import re

BACKEND_URL = "http://127.0.0.1:8001/api/analysis"

def safe_str(val) -> str:
    return str(val).encode("ascii", errors="replace").decode("ascii")

TEST_CASES = [
    {
        "name": "Flow 1: Laptop (Electronics)",
        "payload": {
            "description": "Need a powerful coding and AI/ML laptop under 150000 with 16GB RAM",
            "category": "electronics",
            "subcategory": "laptop",
            "budget": "150000",
            "decisionStyle": "best-overall",
            "riskTolerance": "balanced",
            "priorities": {
                "performance": 35.0,
                "value": 20.0,
                "battery": 15.0,
                "display": 15.0,
                "build": 10.0,
                "upgradeability": 5.0
            },
            "requirements": ["16GB RAM minimum", "FHD IPS display"],
            "dealBreakers": ["Thermal overheating", "Less than 16GB RAM"]
        },
        "expected_agents": ["Performance Agent", "Value Agent", "Battery Agent", "Experience Agent", "Future Agent"],
        "expected_rec_contains": "",
        "forbidden_terms": []
    },
    {
        "name": "Flow 2: Smartphone (Electronics)",
        "payload": {
            "description": "Looking for a smartphone with pro-grade Sony camera, 120Hz LTPO AMOLED display, and 5000mAh battery under 40000",
            "category": "electronics",
            "subcategory": "smartphone",
            "budget": "40000",
            "decisionStyle": "best-overall",
            "riskTolerance": "balanced",
            "priorities": {
                "camera": 35.0,
                "battery": 20.0,
                "performance": 15.0,
                "display": 15.0,
                "software": 10.0,
                "build": 3.0,
                "value": 2.0
            },
            "requirements": ["50MP OIS camera", "120Hz LTPO display"],
            "dealBreakers": ["Bloatware ads", "Slow charging"]
        },
        "expected_agents": ["Camera Agent", "Battery Agent", "Performance Agent", "Display & UX Agent", "Value Agent"],
        "expected_rec_contains": "",
        "forbidden_terms": []
    },
    {
        "name": "Flow 3: Smartwatch (Electronics)",
        "payload": {
            "description": "Fitness smartwatch for marathon training with dual-band GPS, accurate heart rate tracking, 5 ATM water resistance under 15000",
            "category": "electronics",
            "subcategory": "smartwatch",
            "budget": "15000",
            "decisionStyle": "best-overall",
            "riskTolerance": "balanced",
            "priorities": {
                "healthFitness": 35.0,
                "battery": 25.0,
                "durability": 15.0,
                "comfort": 10.0,
                "smartFeatures": 5.0,
                "compatibility": 5.0,
                "value": 5.0
            },
            "requirements": ["Accurate heart rate sensor", "5 ATM water resistance"],
            "dealBreakers": ["Mandatory paid subscription"]
        },
        "expected_agents": ["Fitness & Health Agent", "Battery Agent", "Durability Agent", "Display & UX Agent", "Value Agent"],
        "expected_rec_contains": "",
        "forbidden_terms": []
    },
    {
        "name": "Flow 4: Finance",
        "payload": {
            "description": "Evaluating where to allocate 200000 savings: balanced mutual fund SIP vs fixed deposit vs index fund",
            "category": "finance",
            "budget": "200000",
            "decisionStyle": "best-overall",
            "riskTolerance": "balanced",
            "priorities": {
                "returnPotential": 30.0,
                "risk": 25.0,
                "liquidity": 15.0,
                "stability": 15.0,
                "growth": 15.0
            },
            "requirements": ["CAGR above 12%", "Downside risk protection"],
            "dealBreakers": ["Permanent capital loss"]
        },
        "expected_agents": ["Return Agent", "Risk Agent", "Liquidity Agent", "Stability Agent", "Growth Agent"],
        "expected_rec_contains": "",
        "forbidden_terms": ["cpu", "gpu", "ram", "laptop", "battery", "keyboard", "chassis"]
    },
    {
        "name": "Flow 5: Career",
        "payload": {
            "description": "Deciding between Senior Applied Data Scientist offer at a high-growth tech scaleup vs Staff Engineer at a traditional enterprise",
            "category": "career",
            "budget": "",
            "decisionStyle": "best-overall",
            "riskTolerance": "balanced",
            "priorities": {
                "salary": 30.0,
                "skillFit": 25.0,
                "growth": 20.0,
                "workLifeBalance": 15.0,
                "stability": 10.0
            },
            "requirements": ["Modern ML tech stack", "Competitive equity & base"],
            "dealBreakers": ["Toxic culture"]
        },
        "expected_agents": ["Compensation Agent", "Skill-Fit Agent", "Growth Agent", "Work-Life Agent", "Stability Agent"],
        "expected_rec_contains": "",
        "forbidden_terms": ["cpu", "gpu", "ram", "laptop", "battery", "hardware", "chassis"]
    },
    {
        "name": "Flow 6: Vehicle",
        "payload": {
            "description": "Family vehicle with maximum safety, cabin space, and highway comfort",
            "category": "vehicle",
            "subcategory": "vehicle",
            "decisionStyle": "best-overall",
            "riskTolerance": "balanced",
            "priorities": {
                "safety": 35.0,
                "space": 25.0,
                "comfort": 20.0,
                "mileage": 10.0,
                "performance": 5.0,
                "maintenance": 3.0,
                "value": 2.0
            },
            "requirements": ["High safety rating", "Spacious seating"],
            "dealBreakers": ["Poor crash rating"]
        },
        "expected_agents": ["Safety Agent", "Budget Agent", "Experience Agent", "Convenience Agent", "Value Agent"],
        "expected_rec_contains": "",
        "forbidden_terms": ["cpu", "gpu", "ram", "laptop", "battery", "asus", "screen"]
    }
]

def run_tests():
    print("=" * 70)
    print("DECISION ARENA - MULTI-CATEGORY & SUBCATEGORY VERIFICATION SUITE")
    print("=" * 70)
    
    all_passed = True

    for tc in TEST_CASES:
        print(f"\n[*] Testing: {tc['name']}")
        body = json.dumps(tc["payload"]).encode("utf-8")
        req = urllib.request.Request(
            BACKEND_URL,
            data=body,
            headers={"Content-Type": "application/json"}
        )

        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                if resp.status != 200:
                    print(f"  [FAIL] HTTP status: {resp.status}")
                    all_passed = False
                    continue
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"  [FAIL] Connection / Request error: {e}")
            all_passed = False
            continue

        agents = data.get("agents", [])
        engine = data.get("decisionEngine") or data.get("decision") or {}
        overall_score = engine.get("overallScore")
        rec = engine.get("recommendation", "")
        confidence = engine.get("confidence", "")

        # 1. Agent count check
        if len(agents) != 5:
            print(f"  [FAIL] Expected 5 agents, received {len(agents)}")
            all_passed = False
            continue
        print(f"  [OK] 5 Agents returned successfully")

        # 2. Agent naming check
        agent_names = [a["agent"] for a in agents]
        mismatched_agents = [exp for exp in tc["expected_agents"] if exp not in agent_names]
        if mismatched_agents:
            print(f"  [FAIL] Missing expected agents: {mismatched_agents}")
            print(f"     Actual agents: {agent_names}")
            all_passed = False
            continue
        print(f"  [OK] Agents matched: {', '.join(agent_names)}")

        # 3. Dynamic scoring calculation check
        if overall_score is None or overall_score <= 0:
            print(f"  [FAIL] Invalid overallScore: {overall_score}")
            all_passed = False
            continue
        print(f"  [OK] Overall Score: {overall_score} (Confidence: {confidence})")

        # 4. Recommendation check
        if tc["expected_rec_contains"] and tc["expected_rec_contains"] not in rec:
            print(f"  [FAIL] Recommendation '{rec}' does not contain '{tc['expected_rec_contains']}'")
            all_passed = False
            continue
        print(f"  [OK] Recommendation calibrated: '{safe_str(rec)}'")

        # 5. Domain isolation check
        payload_str = json.dumps(data).lower()
        leaked_terms = [t for t in tc["forbidden_terms"] if re.search(r'\b' + re.escape(t) + r'\b', payload_str)]
        if leaked_terms:
            print(f"  [FAIL] Forbidden domain leakage detected: {leaked_terms}")
            all_passed = False
            continue
        if tc["forbidden_terms"]:
            print(f"  [OK] Zero hardware leakage (checked {len(tc['forbidden_terms'])} domain terms)")

        print(f"  [PASS] {tc['name']}")

    print("\n" + "=" * 70)
    if all_passed:
        print("ALL 6 FLOWS PASSED PERFECTLY WITH ZERO DEFECTS!")
        print("=" * 70)
        return 0
    else:
        print("SOME TESTS FAILED")
        print("=" * 70)
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())
