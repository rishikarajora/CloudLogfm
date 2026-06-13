import torch
import torch.nn as nn


class Trainer:

    def __init__(
        self,
        model,
        optimizer,
        device
    ):

        self.model = model
        self.optimizer = optimizer
        self.device = device

        self.criterion = nn.CrossEntropyLoss()

    def train_epoch(
        self,
        dataloader
    ):

        self.model.train()

        total_loss = 0

        for inputs, targets in dataloader:

            inputs = inputs.to(self.device)

            targets = targets.to(self.device)

            self.optimizer.zero_grad()

            outputs = self.model(inputs)

            loss = self.criterion(
                outputs,
                targets
            )

            loss.backward()

            self.optimizer.step()

            total_loss += loss.item()

        return total_loss / len(dataloader)