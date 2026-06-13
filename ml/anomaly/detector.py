import torch


class AnomalyDetector:

    def __init__(
        self,
        model
    ):

        self.model = model

    def score(
        self,
        sequence,
        true_event
    ):

        x = torch.tensor(
            [sequence],
            dtype=torch.long
        )

        with torch.no_grad():

            mask_positions = torch.tensor(
                [len(sequence) - 1]
            )

            logits = self.model(
                x,
                mask_positions
            )

            probs = torch.softmax(
                logits,
                dim=-1
            )

        confidence = probs[
            0,
            true_event
        ].item()

        anomaly_score = (
            1 - confidence
        )

        if anomaly_score < 0.30:

            level = "NORMAL"

        elif anomaly_score < 0.70:

            level = "WARNING"

        else:

            level = "CRITICAL"

        return (
            confidence,
            anomaly_score,
            level
        )