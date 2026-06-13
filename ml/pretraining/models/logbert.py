import torch
import torch.nn as nn

from ml.pretraining.models.embeddings import EventEmbedding
from ml.pretraining.models.positional_encoding import PositionalEncoding
from ml.pretraining.models.transformer_encoder import LogTransformerEncoder


class LogBERT(nn.Module):

    def __init__(
        self,
        vocab_size,
        embed_dim=128
    ):

        super().__init__()

        self.embedding = EventEmbedding(
            vocab_size=vocab_size,
            embedding_dim=embed_dim
        )

        self.position = PositionalEncoding(
            embedding_dim=embed_dim
        )

        self.encoder = LogTransformerEncoder(
            embedding_dim=embed_dim
        )

        self.classifier = nn.Linear(
            embed_dim,
            vocab_size + 1
        )

    def forward(
        self,
        x,
        mask_positions
    ):

        x = self.embedding(x)

        x = self.position(x)

        x = self.encoder(x)

        batch_size = x.size(0)

        hidden = x[
            torch.arange(batch_size),
            mask_positions
        ]

        logits = self.classifier(
            hidden
        )

        return logits

    def get_embeddings(
        self,
        x
    ):

        x = self.embedding(x)

        x = self.position(x)

        x = self.encoder(x)

        return x.mean(dim=1)