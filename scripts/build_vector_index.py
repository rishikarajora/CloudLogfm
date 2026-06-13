import json
import faiss
import torch
import numpy as np
import sys

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.pretraining.models.logbert import LogBERT
from ml.data_pipeline.preprocessing.sequence_builder import SequenceBuilder


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

builder = SequenceBuilder()

node_sequences = builder.build_node_sequences(
    "data/raw/BGL/BGL.log",
    max_logs=200000
)

vectors = []
metadata = []

for node, sequence in node_sequences.items():

    if len(sequence) < 20:
        continue

    sequence = sequence[:20]

    x = torch.tensor(
        [sequence],
        dtype=torch.long
    )

    with torch.no_grad():

        emb = model.get_embeddings(x)

    vectors.append(
        emb.squeeze(0).numpy()
    )

    metadata.append(
        {
            "node": node,
            "sequence": sequence
        }
    )

vectors = np.array(
    vectors,
    dtype=np.float32
)

print("Vectors:")
print(vectors.shape)

index = faiss.IndexFlatL2(
    vectors.shape[1]
)

index.add(vectors)

faiss.write_index(
    index,
    "data/embeddings/logbert.index"
)

with open(
    "data/embeddings/metadata.json",
    "w"
) as f:

    json.dump(
        metadata,
        f,
        indent=4
    )

print("\nSaved FAISS Index")