"""
Finance Candidate Providers for Decision Arena.
Provides dynamic candidate pools for Investments, Loans, Credit Cards, Insurance, and Savings.
Data source is currently marked as 'demo'.
"""

from typing import List, Dict, Any, Optional
from .base import BaseCandidateProvider, create_candidate_option
from ..schemas.decision import DecisionInputSchema

class InvestmentProvider(BaseCandidateProvider):
    """Provides dynamic candidate options for investments."""

    DEMO_INVESTMENTS = [
        create_candidate_option(
            id="diversified-index-flexicap",
            name="Diversified Index & Flexi-Cap Allocation",
            category="finance",
            subcategory="investment",
            price="₹2,00,000",
            description="60% Nifty 50 Index + 40% Tier-1 Flexi-Cap equity allocation with dynamic rebalancing",
            tags=["12-14% CAGR", "Nifty 50", "Flexi-Cap", "Long-Term", "T+1 Liquidity"],
            attributes={"returnPotential": 91.0, "risk": 88.0, "liquidity": 86.0, "stability": 88.0, "growth": 90.0},
            strengths=[
                "Historical 12–14% CAGR comfortably outpaces long-term retail inflation",
                "Low overall expense ratio (<0.35%) minimizes fee drag across a 5-year horizon",
                "T+1 settlement turnaround on open-ended liquid allocations with zero lock-in",
                "Broad large-cap diversification provides resilient downside risk protection",
            ],
            concerns=[
                "Subject to interim equity market drawdown volatility during macro corrections",
                "Demands a 3–5 year minimum holding discipline to realize full compounding",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="balanced-hybrid-sip",
            name="Balanced 50:50 Equity & Debt Hybrid",
            category="finance",
            subcategory="investment",
            price="₹2,00,000",
            description="50% High-dividend equity basket + 50% High-grade corporate debt instruments",
            tags=["10-12% Blended CAGR", "Auto Rebalancing", "Moderate Risk", "Downside Buffer"],
            attributes={"returnPotential": 84.0, "risk": 88.0, "liquidity": 85.0, "stability": 89.0, "growth": 83.0},
            strengths=[
                "Automatic quarterly rebalancing locks in gains during market peaks",
                "Significant downside buffer cushions against equity corrections",
                "Healthy predictable regular distribution yield option",
            ],
            concerns=[
                "Slightly higher total expense ratio due to active hybrid fund management",
                "Sacrifices peak bull market upside relative to 100% pure equity",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="high-yield-arbitrage-liquid",
            name="High-Yield Liquid & Arbitrage Allocation",
            category="finance",
            subcategory="investment",
            price="₹2,00,000",
            description="70% Arbitrage Fund + 30% Overnight Liquid Fund with equity tax efficiency",
            tags=["7.2-7.8% Yield", "Equity Taxation", "Capital Preservation", "Instant Cash", "Low Risk"],
            attributes={"returnPotential": 76.0, "risk": 95.0, "liquidity": 96.0, "stability": 94.0, "growth": 72.0},
            strengths=[
                "Nearly zero mark-to-market drawdown risk; principal capital is highly shielded",
                "Treated as equity for capital gains taxation, reducing effective tax drag",
                "Instant redemption access with linked debit card or same-day NEFT/RTGS",
            ],
            concerns=[
                "Compounding yield (~7.5%) will not aggressively beat high inflation over a decade",
                "Limited long-term wealth multiplication compared to active equity",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="target-maturity-debt",
            name="Target Maturity Index Debt Fund",
            category="finance",
            subcategory="investment",
            price="₹2,00,000",
            description="AAA Public Sector Undertakings & State Development Loans maturing in 2028",
            tags=["7.5% Predictable YTM", "AAA Safety", "Zero Duration Risk", "Institutional Grade"],
            attributes={"returnPotential": 78.0, "risk": 93.0, "liquidity": 88.0, "stability": 95.0, "growth": 75.0},
            strengths=[
                "Known yield-to-maturity (YTM) locks in returns upon holding to maturity date",
                "Zero credit risk as portfolio comprises only top-tier state and PSU paper",
                "Lower expense ratio than traditional active debt funds",
            ],
            concerns=[
                "Recent tax code changes align debt taxation with individual income tax slabs",
                "Fixed income returns do not benefit from corporate earnings expansions",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="sovereign-gold-bonds",
            name="Sovereign Gold & Dynamic Bond Basket",
            category="finance",
            subcategory="investment",
            price="₹2,00,000",
            description="40% Sovereign Gold Reserve + 60% Target Maturity AAA Central Government Securities",
            tags=["Sovereign Guarantee", "Gold Hedge", "Fixed 2.5% Coupon", "Zero Credit Risk"],
            attributes={"returnPotential": 80.0, "risk": 91.0, "liquidity": 82.0, "stability": 92.0, "growth": 79.0},
            strengths=[
                "Backed by central sovereign guarantee with zero default or credit risk",
                "Gold provides direct portfolio hedging against currency devaluation and geopolitical shocks",
                "Tax-free capital gains on gold if held until sovereign maturity",
            ],
            concerns=[
                "Secondary market trading volumes can experience modest bid-ask price spreads",
                "Fixed tenure structure rewards patient holding",
            ],
            source="demo",
        ),
        create_candidate_option(
            id="reit-infrastructure-trust",
            name="Commercial REIT & Infrastructure Trust Yield Basket",
            category="finance",
            subcategory="investment",
            price="₹2,00,000",
            description="Grade-A commercial office REITs + high-traffic toll road infrastructure trust",
            tags=["8-9% Distribution Yield", "Quarterly Payouts", "Real Estate Hedge"],
            attributes={"returnPotential": 82.0, "risk": 87.0, "liquidity": 89.0, "stability": 88.0, "growth": 81.0},
            strengths=[
                "High regular cash flow distributions delivered on a quarterly schedule",
                "Underlying assets feature 90%+ occupancy with institutional multinational tenants",
            ],
            concerns=["Interest rate hikes can temporarily depress unit valuations", "Complex taxation rules"],
            source="demo",
        ),
        create_candidate_option(
            id="international-nasdaq-feeder",
            name="International Tech Index Feeder Fund",
            category="finance",
            subcategory="investment",
            price="₹2,00,000",
            description="100% allocation to top 100 global technology pioneers with USD currency hedge",
            tags=["Global Tech", "USD Exposure", "High Alpha", "Geographic Diversification"],
            attributes={"returnPotential": 93.0, "risk": 80.0, "liquidity": 84.0, "stability": 79.0, "growth": 94.0},
            strengths=[
                "Direct exposure to world-leading AI, cloud, and semiconductor leaders",
                "Rupee depreciation provides natural tailwind currency gains",
            ],
            concerns=["Subject to tech sector multiple compression cycles", "Higher tracking variance"],
            source="demo",
        ),
    ]

    def get_candidates(
        self,
        category: str,
        subcategory: str = "",
        decision: Optional[DecisionInputSchema] = None,
    ) -> List[Dict[str, Any]]:
        candidates = list(self.DEMO_INVESTMENTS)
        if decision and decision.maxCandidates and decision.maxCandidates > 0:
            return candidates[:decision.maxCandidates]
        return candidates


class FinanceCandidateProvider(BaseCandidateProvider):
    """Main Finance Candidate Provider."""

    def __init__(self):
        self.investment_provider = InvestmentProvider()

    def get_candidates(
        self,
        category: str,
        subcategory: str = "",
        decision: Optional[DecisionInputSchema] = None,
    ) -> List[Dict[str, Any]]:
        return self.investment_provider.get_candidates(category, subcategory, decision)
