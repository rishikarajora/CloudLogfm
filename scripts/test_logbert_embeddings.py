import json
import torch
import sys

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.pretraining.models.logbert import LogBERT


with open(
    "ml/tokenizer/vocab.json",
    "r"
) as f:

    vocab = json.load(f)


model = LogBERT(
    vocab_size=len(vocab)
)

model.load_state_dict(
    torch.load(
        "ml/checkpoints/logbert/logbert.pt",
        map_location="cpu"
    )
)

model.eval()

sequence = torch.tensor(
    [[
        5, 7, 8, 10, 11,
        12, 13, 13, 13, 13,
        13, 13, 13, 14, 14,
        14, 14, 14, 14, 14
    ]]
)

with torch.no_grad():

    embedding = model.get_embeddings(
        sequence
    )

print("Embedding Shape:")
print(embedding.shape)

print()

print("First 10 Values:")
print(
    embedding[0][:10]
)