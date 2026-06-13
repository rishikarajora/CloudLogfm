import torch
import torch.nn as nn


class EventEmbedding(nn.Module):

    def __init__(
        self,
        vocab_size,
        embedding_dim=128
    ):

        super().__init__()

        self.embedding = nn.Embedding(
            num_embeddings=vocab_size + 1,
            embedding_dim=embedding_dim
        )

    def forward(
        self,
        input_ids
    ):

        return self.embedding(
            input_ids
        )