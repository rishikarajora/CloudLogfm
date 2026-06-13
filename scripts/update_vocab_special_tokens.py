import json

with open(
    "ml/tokenizer/vocab.json",
    "r"
) as f:
    vocab = json.load(f)

max_id = max(vocab.values())

vocab["[MASK]"] = max_id + 1

with open(
    "ml/tokenizer/vocab.json",
    "w"
) as f:
    json.dump(
        vocab,
        f,
        indent=4
    )

print(
    "MASK ID:",
    vocab["[MASK]"]
)