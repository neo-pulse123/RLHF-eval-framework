# data_pipeline/loader.py
import pandas as pd
from typing import Union
from pathlib import Path

def load_annotated_data(path: Union[str, Path]) -> pd.DataFrame:
    path = Path(path)
    suffix = path.suffix.lower()

    # JSON Lines 格式 (.jsonl)
    if suffix == ".jsonl":
        df = pd.read_json(path, lines=True)

    # 标准 JSON 数组格式
    elif suffix == ".json":
        df = pd.read_json(path)

    # CSV 格式
    elif suffix == ".csv":
        df = pd.read_csv(path)

    else:
        raise ValueError(f"Unsupported file type: {suffix}")

    return df
