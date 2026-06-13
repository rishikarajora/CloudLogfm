import torch
from torch.utils.data import Dataset


class LogDataset(Dataset):

    def __init__(
        self,
        node_sequences,
        window_size=10,
        min_length=20
    ):

        self.samples = []

        for sequence in node_sequences.values():

            if len(sequence) < min_length:
                continue

            if len(set(sequence)) < 5:
                continue

            for i in range(
                len(sequence) - window_size
            ):

                input_window = sequence[
                    i:i + window_size
                ]

                target = sequence[
                    i + window_size
                ]

                self.samples.append(
                    (
                        input_window,
                        target
                    )
                )

    def __len__(self):

        return len(self.samples)

    def __getitem__(
        self,
        idx
    ):

        x, y = self.samples[idx]

        return (
            torch.tensor(
                x,
                dtype=torch.long
            ),
            torch.tensor(
                y,
                dtype=torch.long
            )
        )