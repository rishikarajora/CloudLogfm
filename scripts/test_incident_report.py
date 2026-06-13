import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.rag.incident_report import (
    IncidentReportGenerator
)

reporter = IncidentReportGenerator()

report = reporter.generate(
    node="R36-M1-N5-C:J02-U01",
    cause="Data TLB Failure",
    confidence=0.89,
    neighbors=[
        "R37-M0-N1-C:J03-U01",
        "R37-M0-NA-C:J02-U01",
        "R33-M1-NB-C:J04-U01"
    ]
)

print(report)