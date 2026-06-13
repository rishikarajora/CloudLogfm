from pathlib import Path
import random

log_file = Path("data/raw/BGL/BGL.log")

total_lines = 4747963

positions = random.sample(
    range(total_lines),
    20
)

positions.sort()

current = 0

with open(
    log_file,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    for idx, line in enumerate(f):

        if current >= len(positions):
            break

        if idx == positions[current]:

            print("\n")
            print(line[:300])

            current += 1