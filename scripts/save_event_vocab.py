import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.cleaning import parse_bgl_line
from ml.data_pipeline.parsing.template_extractor import LogTemplateExtractor

log_file = Path("data/raw/BGL/BGL.log")

extractor = LogTemplateExtractor()

event_vocab = {}

event_counter = 1

MAX_LOGS = 50000

with open(
    log_file,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    for idx, line in enumerate(f):

        parsed = parse_bgl_line(line)

        template = extractor.extract_template(
            parsed["message"]
        )

        if template not in event_vocab:

            event_vocab[template] = event_counter

            event_counter += 1

        if idx >= MAX_LOGS:
            break

output_file = Path(
    "ml/tokenizer/vocab.json"
)

with open(
    output_file,
    "w"
) as f:

    json.dump(
        event_vocab,
        f,
        indent=4
    )

print(
    f"Saved {len(event_vocab)} events"
)