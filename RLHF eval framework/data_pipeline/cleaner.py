# data_pipeline/cleaner.py
import pandas as pd

def basic_clean(
    df: pd.DataFrame,
    text_cols=("prompt", "response_a", "response_b"),
    min_len: int = 3
) -> pd.DataFrame:
    # 去重
    df = df.drop_duplicates()

    # 去除空值
    df = df.dropna(subset=list(text_cols))

    # 去除过短文本
    for col in text_cols:
        df = df[df[col].astype(str).str.len() >= min_len]

    # 这里可以扩展更多规则：标注质量过滤、异常标注过滤等
    return df
