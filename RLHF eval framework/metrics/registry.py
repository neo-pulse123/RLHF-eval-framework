# metrics/registry.py
from typing import Dict, List
from .base import BaseMetric
from .safety import SafetyMetric
from .helpfulness import HelpfulnessMetric
from .factuality import FactualityMetric
from .harmlessness import HarmlessnessMetric

class MetricRegistry:
    def __init__(self):
        self._metrics: Dict[str, BaseMetric] = {}

    def register(self, metric: BaseMetric):
        self._metrics[metric.name] = metric

    def get(self, name: str) -> BaseMetric:
        return self._metrics[name]

    def list_metrics(self) -> List[str]:
        return list(self._metrics.keys())

    def all(self) -> Dict[str, BaseMetric]:
        return self._metrics

def default_registry() -> MetricRegistry:
    reg = MetricRegistry()
    reg.register(SafetyMetric())
    reg.register(HelpfulnessMetric())
    reg.register(FactualityMetric())
    reg.register(HarmlessnessMetric())
    return reg
