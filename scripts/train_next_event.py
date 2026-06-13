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
from ml.pretraining.trainer import Trainer

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

dataset = LogDataset(
    node_sequences
)

loader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True
)

device = torch.device("cpu")

model = NextEventPredictor(
    vocab_size=len(vocab)
)

model.to(device)

optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=1e-3
)

trainer = Trainer(
    model,
    optimizer,
    device
)

for epoch in range(5):

    loss = trainer.train_epoch(
        loader
    )

    print(
        f"Epoch {epoch+1} Loss: {loss:.4f}"
    )

    torch.save(
    model.state_dict(),
    "ml/checkpoints/next_event.pt"
)