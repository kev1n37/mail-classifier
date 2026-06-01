from dataclasses import dataclass


@dataclass
class ClassificationResult:
    category: str
    reason: str
    status: str = "ok"
