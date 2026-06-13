from pathlib import Path

log_file = Path("data/raw/BGL/BGL.log")

with open(
    log_file,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    line = f.readline().strip()

parts = line.split()

for i, part in enumerate(parts):
    print(i, "=>", part)