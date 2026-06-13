import json
import faiss
import numpy as np


index = faiss.read_index(
    "data/embeddings/logbert.index"
)

with open(
    "data/embeddings/metadata.json",
    "r"
) as f:

    metadata = json.load(f)


query_vector = np.array(
    [index.reconstruct(0)],
    dtype=np.float32
)

distances, indices = index.search(
    query_vector,
    5
)

print("\nTop Similar Incidents\n")

for rank, idx in enumerate(indices[0]):

    item = metadata[idx]

    print(
        f"{rank + 1}. Node: {item['node']}"
    )

    print(
        f"Distance: {distances[0][rank]:.4f}"
    )

    print(
        f"Sequence: {item['sequence']}"
    )

    print("-" * 60)