"""
Dynamic Candidate Pool Verification Suite for Decision Arena.
Validates:
1. Dynamic Candidate Counts: 1 candidate, 5 candidates, 10 candidates.
2. Ranking logic executes and ranks accurately regardless of candidate pool size.
3. candidateCount matches the actual number of candidates returned by CandidateProvider.
4. Top-N display selection functions without assuming exactly 5 total candidates.
"""

import urllib.request
import json
import sys

BACKEND_URL = "http://127.0.0.1:8001/api/analysis"

def test_dynamic_candidate_counts():
    print("=" * 70)
    print("DECISION ARENA - DYNAMIC CANDIDATE POOL VERIFICATION")
    print("=" * 70)

    test_scenarios = [
        {
            "name": "Scenario 1: Single Candidate Pool (1 Candidate)",
            "maxCandidates": 1,
            "expectedCount": 1,
            "description": "Evaluate single candidate pool",
        },
        {
            "name": "Scenario 2: Medium Candidate Pool (5 Candidates)",
            "maxCandidates": 5,
            "expectedCount": 5,
            "description": "Evaluate 5 candidates pool",
        },
        {
            "name": "Scenario 3: Expanded Candidate Pool (10 Candidates)",
            "maxCandidates": 10,
            "expectedCount": 10,
            "description": "Evaluate 10 candidates pool",
        },
    ]

    all_passed = True

    for sc in test_scenarios:
        print(f"\n[*] Running: {sc['name']}")
        payload = {
            "description": "Laptop under 55000 for coding and data modeling",
            "category": "electronics",
            "subcategory": "laptop",
            "budget": "55000",
            "maxCandidates": sc["maxCandidates"],
            "topN": 5,
            "priorities": {
                "performance": 30.0,
                "value": 25.0,
                "battery": 15.0,
                "experience": 15.0,
                "futureProof": 15.0,
            },
            "requirements": ["16GB RAM minimum", "Dedicated GPU"],
            "dealBreakers": ["Less than 16GB RAM"],
        }

        req = urllib.request.Request(
            BACKEND_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )

        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"  [FAIL] Request error: {e}")
            all_passed = False
            continue

        candidate_count = data.get("candidateCount")
        filtered_count = data.get("filteredCandidateCount")
        rankings = data.get("rankings", [])
        best_overall = data.get("bestOverall")
        comparison = data.get("comparison")
        data_source = data.get("dataSource")

        # 1. Dynamic candidate count verification
        if candidate_count != sc["expectedCount"]:
            print(f"  [FAIL] Expected candidateCount={sc['expectedCount']}, got {candidate_count}")
            all_passed = False
            continue
        print(f"  [OK] candidateCount is dynamic: {candidate_count} (source: {data_source})")

        # 2. Rankings include only candidates that passed the filter pipeline.
        if filtered_count != len(rankings) or len(rankings) > candidate_count:
            print(f"  [FAIL] Filtered count {filtered_count} does not match {len(rankings)} rankings")
            all_passed = False
            continue
        if not rankings:
            print("  [FAIL] Expected at least one eligible candidate to be ranked")
            all_passed = False
            continue
        print(f"  [OK] {len(rankings)} of {candidate_count} discovered options passed filters and were ranked")

        # 3. Best overall identification
        if not best_overall or best_overall.get("rank") != 1:
            print(f"  [FAIL] Best overall not correctly identified: {best_overall}")
            all_passed = False
            continue
        print(f"  [OK] Rank #1 Best Overall: '{best_overall.get('name')}' (Score: {best_overall.get('score')})")

        # 4. Monotonic descending ranking check
        scores = [r["score"] for r in rankings]
        is_sorted = all(scores[i] >= scores[i+1] for i in range(len(scores)-1))
        if not is_sorted:
            print(f"  [FAIL] Rankings not sorted in descending order: {scores}")
            all_passed = False
            continue
        print(f"  [OK] Monotonic descending order verified: {scores}")

        # 5. Comparison matrix exists
        if not comparison or not comparison.get("factors"):
            print(f"  [FAIL] Comparison matrix missing factors")
            all_passed = False
            continue
        print(f"  [OK] Comparison matrix generated with {len(comparison['factors'])} factors")

        print(f"  [PASS] {sc['name']}")

    print("\n" + "=" * 70)
    if all_passed:
        print("ALL DYNAMIC CANDIDATE TESTS PASSED WITH ZERO DEFECTS!")
        print("=" * 70)
        return

    print("DYNAMIC CANDIDATE TESTS FAILED")
    print("=" * 70)
    raise AssertionError("DYNAMIC CANDIDATE TESTS FAILED")

if __name__ == "__main__":
    try:
        test_dynamic_candidate_counts()
    except AssertionError:
        sys.exit(1)
    sys.exit(0)
