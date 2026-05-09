# metrics/factuality.py
from .base import BaseMetric

class FactualityMetric(BaseMetric):
    name = "factuality"

    def __call__(self, prompt: str, response: str) -> float:
        # TODO: 可接入检索+NLI 或事实一致性模型
        # 这里仅占位：长一点、结构化一点就给高分
        if len(response.split()) > 50:
            return 0.8
        return 0.5
