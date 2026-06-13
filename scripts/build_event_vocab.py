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

            event_vocab[template] = f"E{event_counter}"

            event_counter += 1

        if idx >= MAX_LOGS:
            break

print("Unique Templates:")
print(len(event_vocab))

print("\nFirst 20 Events:\n")

for i, (k, v) in enumerate(event_vocab.items()):

    print(v, "=>", k)

    if i == 20:
        break