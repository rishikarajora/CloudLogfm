import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.sequence_builder import SequenceBuilder

builder = SequenceBuilder()

sequences = builder.build_node_sequences(
    "data/raw/BGL/BGL.log",
    max_logs=200000
)

lengths = [len(v) for v in sequences.values()]

print("Nodes:", len(lengths))

print("Max Length:", max(lengths))
print("Min Length:", min(lengths))

print(
    "Average Length:",
    round(sum(lengths)/len(lengths),2)
)

lengths.sort(reverse=True)

print("\nTop 20 Longest Sequences\n")

for x in lengths[:20]:
    print(x)