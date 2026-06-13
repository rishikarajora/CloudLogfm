import json
import sys

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.sequence_builder import SequenceBuilder
from ml.pretraining.datasets.masked_log_dataset import MaskedLogDataset


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

print("Dataset Size:")
print(len(dataset))

print("\n" + "=" * 60)

for idx in [0, 10, 100]:

    if idx >= len(dataset):
        continue

    x, y, pos = dataset[idx]

    print(f"\nSample {idx}")

    print("Sequence:")
    print(x.tolist())

    print()

    print("Target:")
    print(y.item())

    print()

    print("Mask Position:")
    print(pos)

    print("\n" + "-" * 60)