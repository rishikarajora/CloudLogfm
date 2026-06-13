from pathlib import Path

log_file = Path("data/raw/BGL/BGL.log")

with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
    for i in range(10):
        print(f.readline().strip())