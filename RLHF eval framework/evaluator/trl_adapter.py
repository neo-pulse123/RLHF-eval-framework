# evaluator/trl_adapter.py
from typing import Any, Dict
from .batch_evaluator import BatchEvaluator

class TRLEvalAdapter:
    def __init__(self, batch_evaluator: BatchEvaluator):
        self.batch_evaluator = batch_evaluator

    def evaluate_outputs(
        self,
        trl_outputs: Dict[str, Any],
        prompt_key: str = "prompts",
        response_key: str = "responses",
    ):
        """
        trl_outputs 示例：
        {
          "prompts": [...],
          "responses": [...],
          ...
        }
        """
        prompts = trl_outputs[prompt_key]
        responses = trl_outputs[response_key]
        scores = self.batch_evaluator.evaluate(prompts, responses)
        return scores
