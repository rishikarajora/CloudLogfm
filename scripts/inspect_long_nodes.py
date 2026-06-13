import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.sequence_builder import SequenceBuilder

builder = SequenceBuilder()

seqs = builder.build_node_sequences(
    "data/raw/BGL/BGL.log",
    max_logs=200000
)

items = sorted(
    seqs.items(),
    key=lambda x: len(x[1]),
    reverse=True
)

for node, seq in items[:10]:

    unique_events = len(set(seq))

    print(
        node,
        "Length =", len(seq),
        "Unique =", unique_events
    )