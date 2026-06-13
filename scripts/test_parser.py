import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.cleaning import parse_bgl_line

log_file = Path("data/raw/BGL/BGL.log")

with open(
    log_file,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    line = f.readline()

parsed = parse_bgl_line(line)

for k, v in parsed.items():
    print(f"{k}: {v}")