import json
import sys
import torch

from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.pretraining.models.logbert import LogBERT
from ml.incident_engine.engine import IncidentEngine


# -------------------------
# Load vocab
# -------------------------

with open(
    "ml/tokenizer/vocab.json",
    "r"
) as f:
    vocab = json.load(f)


# -------------------------
# Load model
# -------------------------

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


# -------------------------
# Engine
# -------------------------

engine = IncidentEngine(
    model,
    vocab
)


# -------------------------
# FastAPI app
# -------------------------

app = FastAPI(
    title="CloudLogFM API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# Request schema
# -------------------------

class IncidentRequest(BaseModel):
    sequence: list
    true_event: int


# -------------------------
# Endpoint
# -------------------------

@app.post("/analyze")
def analyze(req: IncidentRequest):

    report = engine.analyze(
        req.sequence,
        req.true_event
    )

    return report


@app.get("/")
def home():

    return {
        "message": "CloudLogFM API is running"
    }
