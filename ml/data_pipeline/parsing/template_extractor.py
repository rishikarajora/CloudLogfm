from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig


class LogTemplateExtractor:

    def __init__(self):

        config = TemplateMinerConfig()

        self.template_miner = TemplateMiner(
            config=config
        )

    def extract_template(self, message: str):

        result = self.template_miner.add_log_message(
            message
        )

        return result["template_mined"]