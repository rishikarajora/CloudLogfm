import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.cleaning import parse_bgl_line
from ml.data_pipeline.parsing.template_extractor import LogTemplateExtractor

VOCAB_PATH = Path("ml/tokenizer/vocab.json")
LOG_FILE = Path("data/raw/BGL/BGL.log")

with open(VOCAB_PATH, "r") as f:
    vocab = json.load(f)

extractor = LogTemplateExtractor()

events = []

MAX_LOGS = 10000

with open(
    LOG_FILE,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    for idx, line in enumerate(f):

        parsed = parse_bgl_line(line)

        template = extractor.extract_template(
            parsed["message"]
        )

        if template in vocab:
            events.append(vocab[template])

        if idx >= MAX_LOGS:
            break

print("Total Events:", len(events))
print(events[:100])