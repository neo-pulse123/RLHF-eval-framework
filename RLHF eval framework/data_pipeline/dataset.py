# data_pipeline/dataset.py
from torch.utils.data import Dataset

class RewardModelDataset(Dataset):
    def __init__(self, data: list[dict], tokenizer, max_length: int = 1024):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        prompt = item["prompt"]
        chosen = item["chosen"]
        rejected = item["rejected"]

        # 这里以简单拼接为例，实际可按模型需求定制
        chosen_enc = self.tokenizer(
            prompt + chosen,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )
        rejected_enc = self.tokenizer(
            prompt + rejected,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )

        return {
            "prompt": prompt,
            "chosen": chosen,
            "rejected": rejected,
            "chosen_input_ids": chosen_enc["input_ids"].squeeze(0),
            "chosen_attention_mask": chosen_enc["attention_mask"].squeeze(0),
            "rejected_input_ids": rejected_enc["input_ids"].squeeze(0),
            "rejected_attention_mask": rejected_enc["attention_mask"].squeeze(0),
        }
