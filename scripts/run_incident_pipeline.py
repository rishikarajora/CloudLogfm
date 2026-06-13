import json
import sys
import faiss
import torch

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.pretraining.models.logbert import LogBERT
from ml.rag.root_cause import RootCauseEngine


# =====================================
# Load Vocabulary
# =====================================

with open(
    "ml/tokenizer/vocab.json",
    "r"
) as f:

    vocab = json.load(f)


# =====================================
# Load LogBERT
# =====================================

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


# =====================================
# Load FAISS Index
# =====================================

index = faiss.read_index(
    "data/embeddings/logbert.index"
)


# =====================================
# Load Metadata
# =====================================

with open(
    "data/embeddings/metadata.json",
    "r"
) as f:

    metadata = json.load(f)


# =====================================
# Query Incident
# =====================================

query_sequence = [
    4, 4, 4,
    31,
    34,
    84,
    85,
    46,
    47,
    86,
    87,
    50,
    51,
    55,
    53,
    54,
    55,
    56,
    57,
    58
]


# =====================================
# Generate Embedding
# =====================================

x = torch.tensor(
    [query_sequence],
    dtype=torch.long
)

with torch.no_grad():

    embedding = model.get_embeddings(
        x
    )

query_vector = (
    embedding.cpu()
    .numpy()
    .astype("float32")
)


# =====================================
# Search Similar Incidents
# =====================================

distances, indices = index.search(
    query_vector,
    k=5
)


print()
print("=" * 60)
print("TOP SIMILAR INCIDENTS")
print("=" * 60)

for rank, idx in enumerate(
    indices[0],
    start=1
):

    item = metadata[idx]

    print()
    print(
        f"{rank}. {item['node']}"
    )

    print(
        f"Distance: "
        f"{distances[0][rank - 1]:.4f}"
    )


# =====================================
# Root Cause Analysis
# =====================================

engine = RootCauseEngine()

cause, confidence = engine.infer(
    query_sequence
)

print()
print("=" * 60)
print("ROOT CAUSE ANALYSIS")
print("=" * 60)

print(
    f"Cause: {cause}"
)

print(
    f"Confidence: "
    f"{confidence:.2%}"
)


# =====================================
# Incident Report
# =====================================

print()
print("=" * 60)
print("INCIDENT REPORT")
print("=" * 60)

print(
    f"Likely Root Cause: {cause}"
)

print(
    f"Confidence: "
    f"{confidence:.2%}"
)

print()
print(
    "Related Historical Incidents:"
)

for idx in indices[0][:3]:

    print(
        "-",
        metadata[idx]["node"]
    )

print()
print("=" * 60)
print("PIPELINE COMPLETE")
print("=" * 60)