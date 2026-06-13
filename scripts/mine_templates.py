import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from ml.data_pipeline.preprocessing.cleaning import parse_bgl_line
from ml.data_pipeline.parsing.template_extractor import LogTemplateExtractor

log_file = Path("data/raw/BGL/BGL.log")

extractor = LogTemplateExtractor()

count = 0

with open(
    log_file,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    for line in f:

        parsed = parse_bgl_line(line)

        template = extractor.extract_template(
            parsed["message"]
        )

        print(template)

        count += 1

        if count == 100:
            break