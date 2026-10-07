import urllib.request
import urllib.error
import json

def test_live_errors():
    cases = [
        (
            {"description": "Laptop", "priorities": {"performance": 30, "value": 25, "battery": 20, "experience": 15, "futureProof": 5}},
            "Priority weights must total exactly 100%"
        ),
        (
            {"description": "   ", "priorities": {"performance": 20, "value": 20, "battery": 20, "experience": 20, "futureProof": 20}},
            "Description is required and must not be empty"
        ),
        (
            {"description": "Laptop", "category": "bad_cat", "priorities": {"performance": 20, "value": 20, "battery": 20, "experience": 20, "futureProof": 20}},
            "Invalid category 'bad_cat'"
        ),
        (
            {"description": "Laptop", "riskTolerance": "wild", "priorities": {"performance": 20, "value": 20, "battery": 20, "experience": 20, "futureProof": 20}},
            "Invalid riskTolerance 'wild'"
        ),
        (
            {"description": "Laptop", "decisionStyle": "wild", "priorities": {"performance": 20, "value": 20, "battery": 20, "experience": 20, "futureProof": 20}},
            "Invalid decisionStyle 'wild'"
        ),
    ]

    for payload, expected_substring in cases:
        req = urllib.request.Request(
            "http://127.0.0.1:8001/api/analysis",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            urllib.request.urlopen(req)
            assert False, f"Expected HTTP 422 for payload: {payload}"
        except urllib.error.HTTPError as e:
            assert e.code == 422, f"Expected 422, got {e.code}"
            err_data = json.loads(e.read().decode("utf-8"))
            detail = err_data.get("detail", "")
            assert expected_substring.lower() in detail.lower(), f"Expected '{expected_substring}' in '{detail}'"
            print(f"Verified live 422 error: {detail}")

if __name__ == "__main__":
    test_live_errors()
    print("ALL LIVE HTTP ERROR CASES VERIFIED SUCCESSFULLY!")
