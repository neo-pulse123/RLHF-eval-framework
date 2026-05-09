# data_pipeline/aligner.py
import pandas as pd

def align_labels(
    df: pd.DataFrame,
    preference_col: str = "preference",  # e.g. "A", "B"
    mapping: dict = None
) -> pd.DataFrame:
    """
    将不同标注体系对齐到统一标准，例如：
    - "A"/"B" -> 0/1
    - "better"/"worse" -> 1/0
    """
    if mapping is None:
        mapping = {"A": 0, "B": 1}
    df["preference_id"] = df[preference_col].map(mapping)
    return df
