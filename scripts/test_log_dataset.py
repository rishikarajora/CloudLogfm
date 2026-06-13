import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.sequence_builder import SequenceBuilder
from ml.pretraining.datasets.log_dataset import LogDataset

builder = SequenceBuilder()

node_sequences = builder.build_node_sequences(
    "data/raw/BGL/BGL.log",
    max_logs=200000
)

dataset = LogDataset(
    node_sequences,
    window_size=10,
    min_length=20
)

print("Dataset Samples:")
print(len(dataset))

print("\n")

for idx in [0, 100, 500, 1000, 5000]:

    print(f"\nSample {idx}")

    x, y = dataset[idx]

    print("Input:", x)

    print("Target:", y)

    print("-" * 50)