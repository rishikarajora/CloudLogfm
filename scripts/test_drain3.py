from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig

config = TemplateMinerConfig()

template_miner = TemplateMiner(config=config)

messages = [
    "instruction cache parity error corrected",
    "instruction cache parity error corrected",
    "memory module 17 failed",
    "memory module 25 failed",
    "memory module 89 failed",
]

for msg in messages:

    result = template_miner.add_log_message(msg)

    print("Message:")
    print(msg)

    print("Template:")
    print(result["template_mined"])

    print("-" * 50)