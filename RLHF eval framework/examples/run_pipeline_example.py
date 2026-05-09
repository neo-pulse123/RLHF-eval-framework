# examples/run_pipeline_example.py
from data_pipeline.loader import load_annotated_data
from data_pipeline.cleaner import basic_clean
from data_pipeline.aligner import align_labels
from data_pipeline.formatter import to_reward_model_format
from data_pipeline.dataset import RewardModelDataset
from transformers import AutoTokenizer

def main():
    df = load_annotated_data("../data/human_prefs.jsonl")
    df = basic_clean(df)
    df = align_labels(df, preference_col="preference")

    formatted = to_reward_model_format(df)

    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    dataset = RewardModelDataset(formatted, tokenizer)

    print("Dataset size:", len(dataset))
    print("Example item:", dataset[0])

if __name__ == "__main__":
    main()
