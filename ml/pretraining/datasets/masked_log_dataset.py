import random
import torch

from torch.utils.data import Dataset


class MaskedLogDataset(Dataset):

    def __init__(
        self,
        node_sequences,
        mask_token=106,
        window_size=20,
        min_length=20
    ):

        self.samples = []

        self.mask_token = mask_token

        for sequence in node_sequences.values():

            if len(sequence) < min_length:
                continue

            if len(set(sequence)) < 5:
                continue

            for i in range(
                len(sequence) - window_size + 1
            ):

                window = sequence[
                    i:i + window_size
                ]

                self.samples.append(
                    window
                )

    def __len__(self):

        return len(self.samples)

    def __getitem__(
        self,
        idx
    ):

        sequence = self.samples[idx].copy()

        mask_position = random.randint(
            0,
            len(sequence) - 1
        )

        target = sequence[
            mask_position
        ]

        sequence[
            mask_position
        ] = self.mask_token

        return (
            torch.tensor(
                sequence,
                dtype=torch.long
            ),
            torch.tensor(
                target,
                dtype=torch.long
            ),
            mask_position
        )