import json
import faiss
import torch
import numpy as np
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


index = faiss.read_index(
    "data/embeddings/logbert.index"
)

with open(
    "data/embeddings/metadata.json",
    "r"
) as f:

    metadata = json.load(f)


query_sequence = [
    4,4,4,
    31,34,84,85,
    46,47,86,87,
    50,51,55,53,
    54,55,56,57
]

x = torch.tensor(
    [query_sequence],
    dtype=torch.long
)

with torch.no_grad():

    query_embedding = (
        model.get_embeddings(x)
        .numpy()
        .astype(np.float32)
    )

distances, indices = index.search(
    query_embedding,
    5
)

print("\nTop Similar Incidents\n")

for rank, idx in enumerate(indices[0]):

    item = metadata[idx]

    print(
        f"{rank+1}. {item['node']}"
    )

    print(
        f"Distance: {distances[0][rank]:.4f}"
    )

    print(
        f"Sequence: {item['sequence']}"
    )

    print("-"*60)