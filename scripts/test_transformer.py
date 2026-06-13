import torch
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.pretraining.models.embeddings import EventEmbedding
from ml.pretraining.models.positional_encoding import PositionalEncoding
from ml.pretraining.models.transformer_encoder import LogTransformerEncoder

with open(
    "ml/tokenizer/vocab.json",
    "r"
) as f:

    vocab = json.load(f)

embedding = EventEmbedding(
    vocab_size=len(vocab)
)

position = PositionalEncoding()

transformer = LogTransformerEncoder()

sample = torch.tensor(
    [
        [5,7,8,10,11,12,13,13,13,13]
    ]
)

x = embedding(sample)

x = position(x)

x = transformer(x)

print("Output Shape:")
print(x.shape)