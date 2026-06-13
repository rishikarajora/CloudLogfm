import json
import torch
import torch.nn as nn

from torch.utils.data import DataLoader

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.sequence_builder import SequenceBuilder
from ml.pretraining.datasets.masked_log_dataset import MaskedLogDataset
from ml.pretraining.models.logbert import LogBERT


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

dataset = MaskedLogDataset(
    node_sequences=node_sequences,
    mask_token=vocab["[MASK]"]
)

loader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True
)

model = LogBERT(
    vocab_size=len(vocab)
)

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=1e-4
)

epochs = 20

best_loss = float("inf")

for epoch in range(epochs):

    model.train()

    total_loss = 0

    for x, y, pos in loader:

        optimizer.zero_grad()

        logits = model(
            x,
            pos
        )

        loss = criterion(
            logits,
            y
        )

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(loader)

    print(
        f"Epoch {epoch + 1} Loss: {avg_loss:.4f}"
    )

    if avg_loss < best_loss:

        best_loss = avg_loss

        torch.save(
            model.state_dict(),
            "ml/checkpoints/logbert/logbert.pt"
        )

        print(
            "Saved Best Model"
        )

print("\nTraining Complete")
print(
    f"Best Loss: {best_loss:.4f}"
)