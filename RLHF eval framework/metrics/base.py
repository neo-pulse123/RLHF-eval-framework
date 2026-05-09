# metrics/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseMetric(ABC):
    name: str

    @abstractmethod
    def __call__(self, prompt: str, response: str) -> float:
        """返回 0-1 之间的分数"""
        raise NotImplementedError

    @property
    def info(self) -> Dict[str, Any]:
        return {"name": self.name, "range": [0.0, 1.0]}
