import torch
import json
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

x = torch.randint(
    0,
    len(vocab),
    (2,20)
)

mask_positions = torch.tensor(
    [5,10]
)

out = model(
    x,
    mask_positions
)

print(out.shape)