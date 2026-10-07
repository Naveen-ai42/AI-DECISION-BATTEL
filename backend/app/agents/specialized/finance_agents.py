"""
Specialized Finance Candidate Evaluation Agents for Decision Arena.
Evaluates investment instruments, loans, credit cards, and insurance products
strictly using financial economics terminology (zero hardware leakage).
"""

from typing import Dict, Any, Optional
from ..base_agent import BaseCandidateAgent, CandidateEvaluation
from ...schemas.decision import DecisionInputSchema

def _extract_finance_reason(
    candidate: Dict[str, Any],
    factor_key: str,
    factor_label: str,
    keywords: list[str],
    score: float,
) -> str:
    strengths = candidate.get("strengths", [])
    concerns = candidate.get("concerns", [])
    cand_name = candidate.get("name", "Asset")

    if score < 82.0:
        for c in concerns:
            c_low = str(c).lower()
            if any(k in c_low for k in keywords):
                return f"{cand_name}: {c}"

    for s in strengths:
        s_low = str(s).lower()
        if any(k in s_low for k in keywords):
            return f"{cand_name}: {s}"

    if score >= 94.0:
        return f"{cand_name}: Institutional-grade {factor_label.lower()} ({score:.0f}/100) with favorable risk-adjusted profile."
    elif score >= 88.0:
        return f"{cand_name}: Strong {factor_label.lower()} metrics ({score:.0f}/100) beating benchmark averages."
    elif score >= 80.0:
        return f"{cand_name}: Moderate {factor_label.lower()} ({score:.0f}/100) aligned with portfolio diversification standards."
    else:
        return f"{cand_name}: Conservative {factor_label.lower()} ({score:.0f}/100) carrying structural trade-offs."


class FinanceFactorAgent(BaseCandidateAgent):
    def __init__(self, agent_name: str, factor_key: str, keywords: list[str]):
        super().__init__(agent_name=agent_name, factor_key=factor_key)
        self.keywords = keywords

    def evaluate(
        self,
        candidate: Dict[str, Any],
        decision: Optional[DecisionInputSchema] = None,
    ) -> CandidateEvaluation:
        attrs = candidate.get("attributes", {})
        score = float(attrs.get(self.factor_key, 80.0))
        reason = _extract_finance_reason(
            candidate=candidate,
            factor_key=self.factor_key,
            factor_label=self.agent_name,
            keywords=self.keywords,
            score=score,
        )
        return CandidateEvaluation(
            agent=self.agent_name,
            candidateId=str(candidate.get("id", "")),
            score=score,
            reason=reason,
        )


# Investment Factor Agents
class ReturnPotentialAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Return Potential", "returnPotential", ["cagr", "alpha", "upside", "yield", "return", "compounding", "bull"])

class RiskAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Risk Assessment", "risk", ["risk", "drawdown", "volatility", "downside", "preservation", "guarantee"])

class LiquidityAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Liquidity", "liquidity", ["liquidity", "redemption", "t+2", "instant", "lock-in", "exit load", "withdrawal"])

class StabilityAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Stability", "stability", ["stability", "sovereign", "arbitrage", "default", "fixed", "variance"])

class GrowthAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Growth", "growth", ["growth", "compounding", "capital", "long-term", "equity", "wealth", "inflation"])

# Loan Factor Agents
class InterestRateAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Interest Rate", "interestRate", ["interest", "apr", "rate", "spread", "benchmark"])

class EMIAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("EMI Affordability", "emi", ["emi", "monthly", "repayment", "affordability", "burden"])

class TotalCostAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Total Cost", "totalCost", ["total cost", "processing fee", "documentation", "charges"])

class TenureAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Tenure", "tenure", ["tenure", "prepayment", "schedule", "foreclosure"])

class FlexibilityAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Flexibility", "flexibility", ["flexibility", "restructuring", "moratorium"])

class EligibilityAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Eligibility", "eligibility", ["eligibility", "approval", "turnaround", "cibil", "credit score"])

# Credit Card Factor Agents
class RewardsAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Rewards", "rewards", ["reward", "cashback", "points", "miles", "multiplier"])

class AnnualFeeAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Annual Fee", "annualFee", ["fee", "waiver", "renewal", "joining"])

class BenefitsAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Benefits", "benefits", ["lounge", "dining", "golf", "concierge", "insurance perk"])

class InterestChargesAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Interest Charges", "interestCharges", ["forex", "markup", "apr", "finance charge", "late fee"])

class AcceptanceAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Acceptance", "acceptance", ["visa", "mastercard", "amex", "rupay", "merchant"])

class FinanceValueAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Value", "value", ["net value", "fee to reward", "effective return"])

# Insurance Factor Agents
class CoverageAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Coverage", "coverage", ["coverage", "sum insured", "rider", "critical illness", "room rent"])

class PremiumAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Premium", "premium", ["premium", "annual cost", "slab", "pricing"])

class ClaimSupportAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Claim Settlement", "claimSupport", ["claim", "settlement ratio", "cashless", "network"])

class ExclusionsAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Exclusions", "exclusions", ["exclusion", "waiting period", "co-pay", "ped"])

class ReliabilityAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Insurer Reliability", "reliability", ["solvency", "grievance", "track record", "financial health"])

class LongTermValueAgent(FinanceFactorAgent):
    def __init__(self):
        super().__init__("Long-Term Value", "longTermValue", ["inflation", "restoration benefit", "no claim bonus", "longevity"])
