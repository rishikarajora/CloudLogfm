import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.cleaning import parse_bgl_line
from ml.data_pipeline.parsing.template_extractor import LogTemplateExtractor

extractor = LogTemplateExtractor()

positions = [
    0,
    100000,
    500000,
    1000000,
    2000000,
    3000000,
    4000000
]

current_target = 0

with open(
    "data/raw/BGL/BGL.log",
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    for idx, line in enumerate(f):

        if current_target >= len(positions):
            break

        if idx == positions[current_target]:

            parsed = parse_bgl_line(line)

            template = extractor.extract_template(
                parsed["message"]
            )

            print(f"\nPosition {idx}")
            print(template)

            current_target += 1