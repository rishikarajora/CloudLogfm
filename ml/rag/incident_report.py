class IncidentReportGenerator:

    def generate(
        self,
        node,
        cause,
        confidence,
        neighbors
    ):

        report = []

        report.append(
            "INCIDENT REPORT"
        )

        report.append(
            "=" * 40
        )

        report.append(
            f"Node: {node}"
        )

        report.append(
            f"Likely Root Cause: {cause}"
        )

        report.append(
            f"Confidence: {confidence:.2%}"
        )

        report.append("")

        report.append(
            "Similar Historical Incidents:"
        )

        for n in neighbors:

            report.append(
                f"- {n}"
            )

        return "\n".join(report)