# metrics/helpfulness.py
from .base import BaseMetric

class HelpfulnessMetric(BaseMetric):
    name = "helpfulness"

    def __call__(self, prompt: str, response: str) -> float:
        # TODO: 可接入一个“是否回答了问题”的分类模型
        # 这里简单用长度和是否提及关键词做占位
        if len(response.strip()) < 5:
            return 0.0
        if "不知道" in response or "无法回答" in response:
            return 0.3
        return 0.8
