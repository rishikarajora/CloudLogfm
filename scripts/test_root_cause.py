import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.rag.root_cause import RootCauseEngine


engine = RootCauseEngine()

sequence = [
    4, 4, 4, 31, 34,
    84, 85, 46, 47,
    86, 87
]

cause, confidence = engine.infer(
    sequence
)

print("Cause:")
print(cause)

print()

print("Confidence:")
print(round(confidence, 3))