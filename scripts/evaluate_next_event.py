import json
import torch
import sys
from pathlib import Path

from torch.utils.data import DataLoader

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.sequence_builder import SequenceBuilder
from ml.pretraining.datasets.log_dataset import LogDataset
from ml.pretraining.models.next_event_predictor import NextEventPredictor

with open(
    "ml/tokenizer/vocab.json",
    "r"
) as f:

    vocab = json.load(f)

builder = SequenceBuilder()

node_sequences = builder.build_node_sequences(
    "data/raw/BGL/BGL.log",
    max_logs=200000
)

dataset = LogDataset(node_sequences)

loader = DataLoader(
    dataset,
    batch_size=128,
    shuffle=False
)

model = NextEventPredictor(
    vocab_size=len(vocab)
)

checkpoint = torch.load(
    "ml/checkpoints/next_event.pt"
)

model.load_state_dict(
    checkpoint
)

model.eval()

correct = 0
total = 0

with torch.no_grad():

    for x, y in loader:

        outputs = model(x)

        preds = outputs.argmax(dim=1)

        correct += (preds == y).sum().item()

        total += y.size(0)

accuracy = correct / total

print(
    f"Accuracy: {accuracy:.4f}"
)