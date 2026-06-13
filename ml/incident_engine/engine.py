import json
import faiss
import torch
import numpy as np

from ml.rag.root_cause import RootCauseEngine
from ml.anomaly.detector import AnomalyDetector


class IncidentEngine:

    def __init__(
        self,
        model,
        vocab
    ):

        self.model = model

        self.root_cause = (
            RootCauseEngine()
        )

        self.anomaly = (
            AnomalyDetector(model)
        )

        self.index = faiss.read_index(
            "data/embeddings/logbert.index"
        )

        with open(
            "data/embeddings/metadata.json",
            "r"
        ) as f:

            self.metadata = json.load(f)

    def analyze(
        self,
        sequence,
        true_event
    ):

        # --------------------
        # Embedding
        # --------------------

        x = torch.tensor(
            [sequence],
            dtype=torch.long
        )

        with torch.no_grad():

            embedding = (
                self.model
                .get_embeddings(x)
            )

        query_vector = (
            embedding.numpy()
            .astype(np.float32)
        )

        # --------------------
        # Retrieval
        # --------------------

        distances, indices = (
            self.index.search(
                query_vector,
                k=5
            )
        )

        similar = []

        for idx in indices[0]:

            similar.append(
                self.metadata[idx]["node"]
            )

        # --------------------
        # Root Cause
        # --------------------

        cause, confidence = (
            self.root_cause.infer(
                sequence
            )
        )

        # --------------------
        # Anomaly
        # --------------------

        (
            event_conf,
            anomaly_score,
            severity
        ) = self.anomaly.score(
            sequence,
            true_event
        )

        return {

            "severity":
                severity,

            "anomaly_score":
                anomaly_score,

            "root_cause":
                cause,

            "root_confidence":
                confidence,

            "similar_incidents":
                similar
        }