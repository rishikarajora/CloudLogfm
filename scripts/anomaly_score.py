import json
import torch
import torch.nn.functional as F
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


sequence = [
    5, 7, 8, 10, 11,
    12, 13, 13, 13, 13,
    13, 13, 13, 14, 14,
    14, 14, 14, 14, 14
]

mask_position = 8

true_event = sequence[
    mask_position
]

sequence[
    mask_position
] = vocab["[MASK]"]

x = torch.tensor(
    [sequence],
    dtype=torch.long
)

mask_positions = torch.tensor(
    [mask_position]
)

with torch.no_grad():

    logits = model(
        x,
        mask_positions
    )

    probs = F.softmax(
        logits,
        dim=1
    )

    topk = torch.topk(
        probs,
        k=5,
        dim=1
    )

    anomaly_score = (
        1.0
        - probs[
            0,
            true_event
        ].item()
    )

print()

print("True Event:")
print(true_event)

print()

print("Confidence:")
print(
    probs[
        0,
        true_event
    ].item()
)

print()

print("Anomaly Score:")
print(anomaly_score)

print()

print("Top Predictions")

for i in range(5):

    print(
        f"Event: {topk.indices[0][i].item()}",
        f"Probability: {topk.values[0][i].item():.4f}"
    )