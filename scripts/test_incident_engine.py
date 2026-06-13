import json
import sys
import torch

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.pretraining.models.logbert import LogBERT
from ml.incident_engine.engine import IncidentEngine


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

engine = IncidentEngine(
    model,
    vocab
)


sequence = [
    5,7,8,10,11,
    12,13,13,13,13,
    13,13,13,14,14,
    14,14,14,14
]

true_event = 14

report = engine.analyze(
    sequence,
    true_event
)

print()
print("=" * 60)
print("INCIDENT ANALYSIS")
print("=" * 60)

for k, v in report.items():

    print(
        f"{k}: {v}"
    )