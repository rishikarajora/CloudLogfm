import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.sequence_builder import SequenceBuilder

builder = SequenceBuilder()

sequences = builder.build_node_sequences(
    "data/raw/BGL/BGL.log",
    max_logs=50000
)

print("Total Nodes:")
print(len(sequences))

print("\n")

for node, seq in list(sequences.items())[:5]:

    print(node)

    print(seq[:20])

    print("-" * 60)