"""
Specialized Electronics Candidate Evaluation Agents for Decision Arena.
Each agent evaluates every candidate along its specific factor dimension
and returns concise user-facing reasoning without chain-of-thought leakage.
"""

from typing import Dict, Any, Optional
from ..base_agent import BaseCandidateAgent, CandidateEvaluation
from ...schemas.decision import DecisionInputSchema

def _extract_reason(
    candidate: Dict[str, Any],
    factor_key: str,
    factor_label: str,
    keywords: list[str],
    score: float,
) -> str:
    """
    Synthesizes concise, domain-specific user-facing reasoning from
    candidate metadata, strengths, and concerns.
    """
    strengths = candidate.get("strengths", [])
    concerns = candidate.get("concerns", [])
    cand_name = candidate.get("name", "Candidate")

    # If low score, prioritize surfacing trade-offs from concerns
    if score < 82.0:
        for c in concerns:
            c_low = str(c).lower()
            if any(k in c_low for k in keywords):
                return f"{cand_name}: {c}"

    # Check for direct strength matches
    for s in strengths:
        s_low = str(s).lower()
        if any(k in s_low for k in keywords):
            return f"{cand_name}: {s}"

    # Fallback to concise metric summary
    if score >= 94.0:
        return f"{cand_name}: Class-leading {factor_label.lower()} ({score:.0f}/100) with top-tier hardware calibration."
    elif score >= 88.0:
        return f"{cand_name}: High-performance {factor_label.lower()} ({score:.0f}/100) exceeding segment expectations."
    elif score >= 80.0:
        return f"{cand_name}: Competent {factor_label.lower()} ({score:.0f}/100) suitable for daily workflows."
    else:
        return f"{cand_name}: Moderate {factor_label.lower()} ({score:.0f}/100) reflecting category trade-offs."


class ElectronicsFactorAgent(BaseCandidateAgent):
    """General reusable factor agent for electronics dimensions."""
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
        reason = _extract_reason(
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


# Laptop & Smartphone Factor Agents
class PerformanceAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Performance", "performance", ["processor", "cpu", "gpu", "snapdragon", "dimensity", "tensor", "ryzen", "core i7", "rtx", "compute", "gaming", "throughput"])

class BatteryAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Battery", "battery", ["battery", "mah", "charging", "runtime", "supervooc", "hours", "endurance", "turbopower", "90wh", "5500mah"])

class DisplayAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Display", "display", ["display", "screen", "amoled", "oled", "120hz", "144hz", "retina", "wqxga", "nits", "pantone", "proxdr"])

class BuildAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Build", "build", ["build", "chassis", "aluminum", "victus", "ip68", "ip67", "metal", "unibody", "finish", "durability"])

class UpgradeabilityAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Upgradeability", "upgradeability", ["upgrade", "ram", "ssd", "so-dimm", "m.2", "expansion", "slots", "soldered", "unified memory"])

class ValueAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Value", "value", ["price", "value", "cost", "budget", "sub-", "affordable", "ratio"])

# Smartphone Specialized
class CameraAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Camera", "camera", ["camera", "sensor", "ois", "photo", "hdr", "portrait", "lens", "optics", "zeiss", "200mp", "50mp", "64mp"])

class SoftwareAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Software", "software", ["software", "os", "updates", "pixel", "clean", "bloatware", "hello ui", "hyperos", "funtouch", "knox", "nothing os"])

# Smartwatch Specialized
class HealthFitnessAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Health & Fitness", "healthFitness", ["health", "fitness", "gps", "hrv", "heart rate", "biometric", "training", "workout", "sleep", "ecg", "bia"])

class SmartFeaturesAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Smart Features", "smartFeatures", ["smart", "wear os", "watchos", "siri", "assistant", "call", "nfc", "pay", "apps", "notifications"])

class ComfortAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Comfort", "comfort", ["comfort", "weight", "lightweight", "strap", "wrist", "ergonomic", "30g", "39g"])

class DurabilityAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Durability", "durability", ["durability", "atm", "water resistance", "sapphire", "rugged", "glass"])

class CompatibilityAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Compatibility", "compatibility", ["compatibility", "android", "ios", "pairing", "cross-platform", "ecosystem"])

# Tablet & Headphones Specialized
class PortabilityAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Portability", "portability", ["portability", "weight", "slim", "thin", "carry"])

class ProductivityAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Productivity", "productivity", ["productivity", "stylus", "s-pen", "pencil", "keyboard", "multitasking"])

class SoundQualityAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Sound Quality", "soundQuality", ["sound", "audio", "acoustic", "bass", "clarity", "codec", "driver"])

class NoiseCancellationAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Noise Cancellation", "noiseCancellation", ["anc", "noise cancellation", "transparency", "isolation", "attenuation"])

class ConnectivityAgent(ElectronicsFactorAgent):
    def __init__(self):
        super().__init__("Connectivity", "connectivity", ["bluetooth", "multipoint", "wireless", "latency", "connection"])
