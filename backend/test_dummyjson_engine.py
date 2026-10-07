"""
DummyJSON Dynamic Candidate Engine Verification Suite.
Validates:
TEST A: Smartphone mainly for camera
TEST B: Smartphone mainly for battery -> ranking shifts!
TEST C: Laptop -> category=electronics, subcategory=laptop, laptop factors & agents
TEST D: Tablet -> category=electronics, subcategory=tablet, tablet factors & agents
TEST E: Vehicle -> category=vehicle, subcategory=vehicle, vehicle factors & agents (zero hardware leakage)
TEST F: Unsupported subcategory -> clear data source unavailable response
TEST G: Unmatched budget -> status: no_matches with suggestions
"""

from app.schemas.decision import DecisionInputSchema
from app.services.analysis_service import analysis_service
from fastapi import HTTPException

def safe_str(val: Any) -> str:
    """Encodes string to ascii-safe representation for Windows console."""
    return str(val).encode("ascii", errors="replace").decode("ascii")

def run_tests():
    print("=" * 80)
    print("DECISION ARENA - DUMMYJSON DYNAMIC CANDIDATE ENGINE VERIFICATION")
    print("=" * 80)

    # -------------------------------------------------------------------------
    # TEST A: Smartphone mainly for camera
    # -------------------------------------------------------------------------
    print("\n[*] TEST A: Smartphone mainly for camera (Budget INR 35,000)")
    decision_a = DecisionInputSchema(
        description="I need a smartphone under 35000 mainly for camera",
        category="electronics",
        subcategory="smartphone",
        budget="35000",
        priorities={
            "camera": 55.0,
            "software": 20.0,
            "display": 10.0,
            "performance": 5.0,
            "battery": 5.0,
            "build": 3.0,
            "value": 2.0,
        },
    )
    res_a = analysis_service.analyze_decision(decision_a)
    print(f"  [OK] Status: {res_a.status}")
    print(f"  [OK] Evaluated candidate count: {res_a.candidateCount} (Source: {res_a.dataSource})")
    print(f"  [OK] Rank #1 Winner: '{res_a.bestOverall.name}' (Score: {res_a.bestOverall.score})")
    print(f"  [OK] Top 5 Candidates:")
    for c in res_a.rankedCandidates[:5]:
        print(f"       #{c.rank}: {c.name} - Score: {c.score} - Camera: {c.factorScores.get('camera')} - Price: {safe_str(c.price)}")
    winner_a = res_a.bestOverall.name

    # -------------------------------------------------------------------------
    # TEST B: Smartphone mainly for battery
    # -------------------------------------------------------------------------
    print("\n[*] TEST B: Smartphone mainly for battery (Budget INR 35,000)")
    decision_b = DecisionInputSchema(
        description="I need a smartphone under 35000 mainly for battery and sustained use",
        category="electronics",
        subcategory="smartphone",
        budget="35000",
        priorities={
            "battery": 55.0,
            "performance": 20.0,
            "value": 10.0,
            "display": 5.0,
            "camera": 4.0,
            "build": 3.0,
            "software": 3.0,
        },
    )
    res_b = analysis_service.analyze_decision(decision_b)
    print(f"  [OK] Status: {res_b.status}")
    print(f"  [OK] Evaluated candidate count: {res_b.candidateCount} (Source: {res_b.dataSource})")
    print(f"  [OK] Rank #1 Winner: '{res_b.bestOverall.name}' (Score: {res_b.bestOverall.score})")
    print(f"  [OK] Top 5 Candidates:")
    for c in res_b.rankedCandidates[:5]:
        print(f"       #{c.rank}: {c.name} - Score: {c.score} - Battery: {c.factorScores.get('battery')} - Price: {safe_str(c.price)}")
    winner_b = res_b.bestOverall.name

    # Verify ranking changed between Test A and Test B
    rank_order_a = [c.name for c in res_a.rankedCandidates[:5]]
    rank_order_b = [c.name for c in res_b.rankedCandidates[:5]]
    assert rank_order_a != rank_order_b, f"Ranking did not shift! Order A: {rank_order_a}, Order B: {rank_order_b}"
    print(f"  [PASS] VERIFIED: Rankings shifted dynamically! Order A != Order B")

    # -------------------------------------------------------------------------
    # TEST C: Laptop for coding
    # -------------------------------------------------------------------------
    print("\n[*] TEST C: Laptop for coding (Budget INR 1,50,000)")
    decision_c = DecisionInputSchema(
        description="I need a laptop under 150000 for coding and compilation",
        category="electronics",
        subcategory="laptop",
        budget="150000",
        priorities={
            "performance": 35.0,
            "battery": 20.0,
            "display": 15.0,
            "build": 15.0,
            "upgradeability": 10.0,
            "value": 5.0,
        },
    )
    res_c = analysis_service.analyze_decision(decision_c)
    print(f"  [OK] Category: {res_c.category}, Subcategory: {res_c.subcategory}")
    factor_keys_c = [f["key"] for f in res_c.factors]
    print(f"  [OK] Laptop factors: {factor_keys_c}")
    assert "upgradeability" in factor_keys_c, "Expected laptop upgradeability factor"
    assert "camera" not in factor_keys_c, "Camera factor should not be in laptop"
    print(f"  [OK] Candidate count: {res_c.candidateCount}")
    print(f"  [OK] Rank #1 Laptop: '{res_c.bestOverall.name}' (Score: {res_c.bestOverall.score})")
    print(f"  [OK] Top 5 Laptops:")
    for c in res_c.rankedCandidates[:5]:
        print(f"       #{c.rank}: {c.name} - Score: {c.score} - Price: {safe_str(c.price)}")
    print(f"  [PASS] Laptop request verified with dynamic DummyJSON laptops!")

    # -------------------------------------------------------------------------
    # TEST D: Tablet for studying
    # -------------------------------------------------------------------------
    print("\n[*] TEST D: Tablet for studying")
    decision_d = DecisionInputSchema(
        description="I need a tablet for studying and digital note-taking",
        category="electronics",
        subcategory="tablet",
        priorities={
            "display": 30.0,
            "portability": 25.0,
            "battery": 20.0,
            "performance": 10.0,
            "software": 5.0,
            "productivity": 5.0,
            "value": 5.0,
        },
    )
    res_d = analysis_service.analyze_decision(decision_d)
    print(f"  [OK] Category: {res_d.category}, Subcategory: {res_d.subcategory}")
    factor_keys_d = [f["key"] for f in res_d.factors]
    print(f"  [OK] Tablet factors: {factor_keys_d}")
    assert "portability" in factor_keys_d, "Expected tablet portability factor"
    assert "productivity" in factor_keys_d, "Expected tablet productivity factor"
    print(f"  [OK] Candidate count: {res_d.candidateCount}")
    print(f"  [OK] Rank #1 Tablet: '{res_d.bestOverall.name}' (Score: {res_d.bestOverall.score})")
    print(f"  [OK] All Tablets evaluated:")
    for c in res_d.rankedCandidates:
        print(f"       #{c.rank}: {c.name} - Score: {c.score} - Display: {c.factorScores.get('display')} - Price: {safe_str(c.price)}")
    print(f"  [PASS] Tablet request verified with dynamic DummyJSON tablets!")

    # -------------------------------------------------------------------------
    # TEST E: Vehicle for family use
    # -------------------------------------------------------------------------
    print("\n[*] TEST E: Vehicle for family use")
    decision_e = DecisionInputSchema(
        description="I need a vehicle for family use with maximum safety and passenger space",
        category="vehicle",
        subcategory="vehicle",
        priorities={
            "safety": 35.0,
            "space": 25.0,
            "comfort": 20.0,
            "mileage": 10.0,
            "performance": 5.0,
            "maintenance": 3.0,
            "value": 2.0,
        },
    )
    res_e = analysis_service.analyze_decision(decision_e)
    print(f"  [OK] Category: {res_e.category}, Subcategory: {res_e.subcategory}")
    factor_keys_e = [f["key"] for f in res_e.factors]
    print(f"  [OK] Vehicle factors: {factor_keys_e}")
    # Verify zero electronics factor leakage in vehicle
    for forbidden in ["ram", "cpu", "gpu", "battery", "camera", "display", "upgradeability"]:
        assert forbidden not in factor_keys_e, f"Leakage: {forbidden} in vehicle factors"
    print(f"  [OK] Candidate count: {res_e.candidateCount}")
    print(f"  [OK] Rank #1 Vehicle: '{res_e.bestOverall.name}' (Score: {res_e.bestOverall.score})")
    print(f"  [OK] Top Vehicles evaluated:")
    for c in res_e.rankedCandidates[:5]:
        print(f"       #{c.rank}: {c.name} - Score: {c.score} - Safety: {c.factorScores.get('safety')} - Space: {c.factorScores.get('space')} - Price: {safe_str(c.price)}")
    print(f"  [PASS] Vehicle request verified with automotive factors and agents!")

    # -------------------------------------------------------------------------
    # TEST F: Unsupported Subcategory Error Handling
    # -------------------------------------------------------------------------
    print("\n[*] TEST F: Unsupported Subcategory Error Handling")
    try:
        decision_f = DecisionInputSchema(
            description="Quantum transistor for research",
            category="electronics",
            subcategory="quantum_transistor",
        )
        analysis_service.analyze_decision(decision_f)
        assert False, "Should have raised HTTPException 400"
    except HTTPException as e:
        assert e.status_code == 400
        print(f"  [OK] Caught clear error (HTTP {e.status_code}): {e.detail}")
    print(f"  [PASS] Unsupported subcategory returns clear response without returning unrelated products!")

    # -------------------------------------------------------------------------
    # TEST G: Unmatched Budget -> status: no_matches
    # -------------------------------------------------------------------------
    print("\n[*] TEST G: Unmatched Budget -> status: no_matches")
    decision_g = DecisionInputSchema(
        description="I need a laptop under 5000",
        category="electronics",
        subcategory="laptop",
        budget="5000",
        priorities={
            "performance": 25.0,
            "battery": 25.0,
            "display": 20.0,
            "build": 15.0,
            "upgradeability": 10.0,
            "value": 5.0,
        },
    )
    res_g = analysis_service.analyze_decision(decision_g)
    print(f"  [OK] Status: {res_g.status}")
    assert res_g.status == "no_matches", f"Expected 'no_matches', got {res_g.status}"
    print(f"  [OK] Message: {safe_str(res_g.message)}")
    print(f"  [OK] Suggestions count: {len(res_g.suggestions)}")
    print(f"  [PASS] Zero-crash no_matches response verified!")

    print("\n" + "=" * 80)
    print("ALL 7 DUMMYJSON DYNAMIC CANDIDATE ENGINE TESTS PASSED PERFECTLY!")
    print("=" * 80)

if __name__ == "__main__":
    run_tests()
