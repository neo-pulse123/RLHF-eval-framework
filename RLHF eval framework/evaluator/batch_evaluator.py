# evaluator/batch_evaluator.py
from typing import List, Dict, Any
import torch
from tqdm import tqdm
from metrics.registry import MetricRegistry

class BatchEvaluator:
    def __init__(
        self,
        metric_registry: MetricRegistry,
        device: str = "cpu",
        batch_size: int = 32,
    ):
        self.metric_registry = metric_registry
        self.device = torch.device(device)
        self.batch_size = batch_size

    def evaluate(
        self,
        prompts: List[str],
        responses: List[str],
    ) -> Dict[str, torch.Tensor]:
        assert len(prompts) == len(responses)
        n = len(prompts)
        metric_names = self.metric_registry.list_metrics()

        scores = {
            name: torch.zeros(n, device=self.device, dtype=torch.float32)
            for name in metric_names
        }

        for start in tqdm(range(0, n, self.batch_size), desc="Evaluating"):
            end = min(start + self.batch_size, n)
            batch_prompts = prompts[start:end]
            batch_responses = responses[start:end]

            # 这里的指标目前是 Python 循环，可进一步向量化或模型化
            for i, (p, r) in enumerate(zip(batch_prompts, batch_responses)):
                idx = start + i
                for name, metric in self.metric_registry.all().items():
                    scores[name][idx] = metric(p, r)

        return scores
