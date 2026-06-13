import json
from collections import defaultdict
from pathlib import Path

from ml.data_pipeline.preprocessing.cleaning import parse_bgl_line
from ml.data_pipeline.parsing.template_extractor import LogTemplateExtractor


class SequenceBuilder:

    def __init__(self):

        self.extractor = LogTemplateExtractor()

        with open(
            "ml/tokenizer/vocab.json",
            "r"
        ) as f:

            self.vocab = json.load(f)

    def build_node_sequences(
        self,
        log_file,
        max_logs=100000
    ):

        node_sequences = defaultdict(list)

        with open(
            log_file,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            for idx, line in enumerate(f):

                parsed = parse_bgl_line(line)

                node = parsed["node"]

                template = self.extractor.extract_template(
                    parsed["message"]
                )

                if template in self.vocab:

                    event_id = self.vocab[template]

                    node_sequences[node].append(
                        event_id
                    )

                if idx >= max_logs:
                    break

        return node_sequences