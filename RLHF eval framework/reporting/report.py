# reporting/report.py
from typing import Dict, Any, List
import torch
import numpy as np
import pandas as pd

def compute_summary(scores: Dict[str, torch.Tensor]) -> Dict[str, Any]:
    summary = {}
    for name, tensor in scores.items():
        arr = tensor.detach().cpu().numpy()
        summary[name] = {
            "mean": float(np.mean(arr)),
            "std": float(np.std(arr)),
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
        }
    return summary

def find_anomalies(
    scores: Dict[str, torch.Tensor],
    threshold_low: float = 0.2,
) -> pd.DataFrame:
    """
    返回一个 DataFrame，标出在任一指标上低于阈值的样本索引及对应分数
    """
    records: List[Dict[str, Any]] = []
    n = len(next(iter(scores.values())))
    for i in range(n):
        row = {"index": i}
        is_anomaly = False
        for name, tensor in scores.items():
            v = float(tensor[i].item())
            row[name] = v
            if v < threshold_low:
                is_anomaly = True
        if is_anomaly:
            records.append(row)
    return pd.DataFrame(records)

def generate_report(
    scores: Dict[str, torch.Tensor],
    prompts: List[str],
    responses: List[str],
    threshold_low: float = 0.2,
) -> Dict[str, Any]:
    summary = compute_summary(scores)
    anomalies_df = find_anomalies(scores, threshold_low=threshold_low)

    # 将异常样本附上原始文本
    anomaly_details = []
    for _, row in anomalies_df.iterrows():
        idx = int(row["index"])
        detail = {
            "index": idx,
            "prompt": prompts[idx],
            "response": responses[idx],
        }
        for name in scores.keys():
            detail[name] = float(row[name])
        anomaly_details.append(detail)

    return {
        "summary": summary,
        "num_samples": len(prompts),
        "num_anomalies": len(anomaly_details),
        "anomalies": anomaly_details,
    }
