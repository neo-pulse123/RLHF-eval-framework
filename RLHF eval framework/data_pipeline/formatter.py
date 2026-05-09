# data_pipeline/formatter.py
import pandas as pd

def to_reward_model_format(df: pd.DataFrame) -> list[dict]:
    """
    输出示例格式：
    [
      {
        "prompt": "...",
        "chosen": "...",   # 人类偏好更高的响应
        "rejected": "..."
      },
      ...
    ]
    """
    formatted = []
    for _, row in df.iterrows():
        if row["preference_id"] == 0:
            chosen = row["response_a"]
            rejected = row["response_b"]
        else:
            chosen = row["response_b"]
            rejected = row["response_a"]

        formatted.append(
            {
                "prompt": row["prompt"],
                "chosen": chosen,
                "rejected": rejected,
            }
        )
    return formatted
