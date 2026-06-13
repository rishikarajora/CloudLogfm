from pathlib import Path

from config.config import BGL_DIR


class BGLLoader:

    def __init__(self):
        self.log_file = BGL_DIR / "BGL.log"

    def exists(self):
        return self.log_file.exists()

    def read_head(self, n=10):

        logs = []

        with open(
            self.log_file,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            for _ in range(n):
                logs.append(f.readline().strip())

        return logs


if __name__ == "__main__":

    loader = BGLLoader()

    print(loader.exists())

    for log in loader.read_head():
        print(log)