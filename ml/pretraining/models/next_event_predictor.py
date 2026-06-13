import torch
import torch.nn as nn

from ml.pretraining.models.embeddings import EventEmbedding
from ml.pretraining.models.positional_encoding import PositionalEncoding
from ml.pretraining.models.transformer_encoder import LogTransformerEncoder


class NextEventPredictor(nn.Module):

    def __init__(
        self,
        vocab_size,
        embedding_dim=128
    ):

        super().__init__()

        self.embedding = EventEmbedding(
            vocab_size=vocab_size,
            embedding_dim=embedding_dim
        )

        self.position = PositionalEncoding(
            embedding_dim=embedding_dim
        )

        self.transformer = LogTransformerEncoder(
            embedding_dim=embedding_dim
        )

        self.classifier = nn.Linear(
            embedding_dim,
            vocab_size + 1
        )

    def forward(
        self,
        input_ids
    ):

        x = self.embedding(input_ids)

        x = self.position(x)

        x = self.transformer(x)

        x = x[:, -1, :]

        logits = self.classifier(x)

        return logits