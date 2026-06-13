import torch
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.pretraining.models.embeddings import EventEmbedding

with open(
    "ml/tokenizer/vocab.json",
    "r"
) as f:

    vocab = json.load(f)

model = EventEmbedding(
    vocab_size=len(vocab),
    embedding_dim=128
)

sample = torch.tensor(
    [
        [5,7,8,10,11,12,13,13,13,13]
    ]
)

output = model(sample)

print("Shape:")
print(output.shape)