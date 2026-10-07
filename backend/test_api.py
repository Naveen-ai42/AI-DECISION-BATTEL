import json
import re
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/api/health")
    assert res.status_code == 200, f"Health check failed: {res.text}"
    data = res.json()
    assert data["status"] == "ok"
    print("PASS: GET /api/health returns 200 and status ok")

def test_electronics_flow():
    payload = {
        "description": "Choose a laptop under ₹55000 for coding",
        "category": "electronics",
        "budget": "55000",
        "requirements": ["At least 16GB RAM", "Good battery life"],
        "dealBreakers": ["Poor display"],
        "priorities": {
            "performance": 30,
            "value": 25,
            "battery": 20,
            "experience": 15,
            "futureProof": 10
        },
        "riskTolerance": "balanced",
        "decisionStyle": "best-overall"
    }

    res = client.post("/api/analysis", json=payload)
    assert res.status_code == 200, f"Electronics analysis failed: {res.text}"
    data = res.json()

    # 1. Five electronics agents
    agents = data.get("agents", [])
    assert len(agents) == 5, f"Expected 5 agents, got {len(agents)}"
    agent_names = [a["agent"] for a in agents]
    expected_agents = [
        "Performance Agent",
        "Value Agent",
        "Battery Agent",
        "Experience Agent",
        "Future Agent"
    ]
    for ea in expected_agents:
        assert ea in agent_names, f"Missing electronics agent: {ea}"

    # 2. Weighted candidate score evaluation
    decision = data.get("decision", {})
    best_overall = data.get("bestOverall", {})
    assert decision["overallScore"] == best_overall["score"], (
        f"Score mismatch: calculated {decision['overallScore']}, expected {best_overall['score']}"
    )
    assert len(data.get("rankedCandidates", [])) >= 1, "Expected ranked candidates"
    assert "ASUS" in decision["recommendation"] or "Laptop" in decision["recommendation"] or len(decision["recommendation"]) > 0
    print(f"PASS: Electronics flow passed. Agents: {agent_names}, Score: {decision['overallScore']}, Winner: {decision['recommendation']}")

def test_finance_flow():
    payload = {
        "description": "Choose the best investment option for ₹2 lakh",
        "category": "finance",
        "budget": "200000",
        "requirements": ["Moderate risk", "Long-term growth", "Easy withdrawal"],
        "dealBreakers": ["Very high risk", "Lock-in period", "Unstable returns"],
        "priorities": {
            "returnPotential": 30,
            "risk": 25,
            "liquidity": 15,
            "stability": 20,
            "growth": 10
        },
        "riskTolerance": "balanced",
        "decisionStyle": "best-overall"
    }

    res = client.post("/api/analysis", json=payload)
    assert res.status_code == 200, f"Finance analysis failed: {res.text}"
    data = res.json()

    # 1. Five finance agents
    agents = data.get("agents", [])
    assert len(agents) == 5, f"Expected 5 agents, got {len(agents)}"
    agent_names = [a["agent"] for a in agents]
    expected_agents = [
        "Return Agent",
        "Risk Agent",
        "Liquidity Agent",
        "Stability Agent",
        "Growth Agent"
    ]
    for ea in expected_agents:
        assert ea in agent_names, f"Missing finance agent: {ea}"

    # 2. Weighted candidate score evaluation
    decision = data.get("decision", {})
    best_overall = data.get("bestOverall", {})
    assert decision["overallScore"] == best_overall["score"], (
        f"Score mismatch: calculated {decision['overallScore']}, expected {best_overall['score']}"
    )

    # 3. NO laptop terminology in finance response
    json_str = json.dumps(data).lower()
    for forbidden in ["battery", "cpu", "gpu", "ram", "asus", "laptop", "tuf", "display quality"]:
        assert not re.search(r"\b" + re.escape(forbidden) + r"\b", json_str), f"Found forbidden hardware term in Finance flow: '{forbidden}'"

    print(f"PASS: Finance flow passed. Agents: {agent_names}, Score: {decision['overallScore']}, Winner: {decision['recommendation']}")

def test_career_flow():
    payload = {
        "description": "Which career path should I choose after BTech Data Science?",
        "category": "career",
        "requirements": ["Competitive compensation", "High learning curve", "Remote/hybrid flexibility"],
        "dealBreakers": ["Toxic culture", "No promotion path"],
        "priorities": {
            "salary": 25,
            "skillFit": 25,
            "growth": 20,
            "workLifeBalance": 15,
            "stability": 15
        },
        "riskTolerance": "balanced",
        "decisionStyle": "best-overall"
    }

    res = client.post("/api/analysis", json=payload)
    assert res.status_code == 200, f"Career analysis failed: {res.text}"
    data = res.json()

    # 1. Five career agents
    agents = data.get("agents", [])
    assert len(agents) == 5, f"Expected 5 agents, got {len(agents)}"
    agent_names = [a["agent"] for a in agents]
    expected_agents = [
        "Compensation Agent",
        "Skill-Fit Agent",
        "Growth Agent",
        "Work-Life Agent",
        "Stability Agent"
    ]
    for ea in expected_agents:
        assert ea in agent_names, f"Missing career agent: {ea}"

    # 2. Weighted candidate score evaluation
    decision = data.get("decision", {})
    best_overall = data.get("bestOverall", {})
    assert decision["overallScore"] == best_overall["score"], (
        f"Score mismatch: calculated {decision['overallScore']}, expected {best_overall['score']}"
    )

    # 3. NO laptop terminology in career response
    json_str = json.dumps(data).lower()
    for forbidden in ["battery", "cpu", "gpu", "ram", "asus", "laptop", "tuf"]:
        assert not re.search(r"\b" + re.escape(forbidden) + r"\b", json_str), f"Found forbidden hardware term in Career flow: '{forbidden}'"

    print(f"PASS: Career flow passed. Agents: {agent_names}, Score: {decision['overallScore']}, Winner: {decision['recommendation']}")

def test_invalid_priority_totals():
    payload = {
        "description": "Choose an investment",
        "category": "finance",
        "priorities": {
            "returnPotential": 30,
            "risk": 25,
            "liquidity": 15,
            "stability": 20,
            "growth": 5  # Sum is 95, not 100
        }
    }
    res = client.post("/api/analysis", json=payload)
    assert res.status_code == 422, f"Expected 422, got {res.status_code}"
    data = res.json()
    assert "total exactly 100" in data.get("detail", ""), f"Error detail: {data}"
    print(f"PASS: Invalid priority totals returns clear 422 error: {data['detail']}")

def test_missing_description():
    payload = {
        "description": "   ",
        "category": "electronics",
        "priorities": {
            "performance": 20,
            "value": 20,
            "battery": 20,
            "experience": 20,
            "futureProof": 20
        }
    }
    res = client.post("/api/analysis", json=payload)
    assert res.status_code == 422, f"Expected 422, got {res.status_code}"
    data = res.json()
    assert "Description is required" in data.get("detail", ""), f"Error detail: {data}"
    print(f"PASS: Missing description returns clear 422 error: {data['detail']}")

def test_invalid_category():
    payload = {
        "description": "Choose a rocket",
        "category": "aerospace_invalid",
    }
    res = client.post("/api/analysis", json=payload)
    assert res.status_code == 422, f"Expected 422, got {res.status_code}"
    data = res.json()
    assert "Invalid category" in data.get("detail", ""), f"Error detail: {data}"
    print(f"PASS: Invalid category returns clear 422 error: {data['detail']}")

if __name__ == "__main__":
    test_health()
    test_electronics_flow()
    test_finance_flow()
    test_career_flow()
    test_invalid_priority_totals()
    test_missing_description()
    test_invalid_category()
    print("\nALL BACKEND API TESTS PASSED SUCCESSFULLY!")
