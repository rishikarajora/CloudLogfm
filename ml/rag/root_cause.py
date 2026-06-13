import json


class RootCauseEngine:

    def __init__(self):

        with open(
            "data/root_causes.json",
            "r"
        ) as f:

            self.causes = json.load(f)

    def infer(
        self,
        sequence
    ):

        votes = {}

        for event in sequence:

            event = str(event)

            if event in self.causes:

                cause = self.causes[event]

                votes[cause] = (
                    votes.get(cause, 0)
                    + 1
                )

        if not votes:

            return (
                "Unknown",
                0
            )

        best = max(
            votes,
            key=votes.get
        )

        confidence = (
            votes[best]
            / len(sequence)
        )

        return (
            best,
            confidence
        )