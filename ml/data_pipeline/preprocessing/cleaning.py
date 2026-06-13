from typing import Dict


def parse_bgl_line(line: str) -> Dict:

    parts = line.strip().split()

    return {
        "label": parts[0],
        "timestamp": parts[1],
        "date": parts[2],
        "node": parts[3],
        "datetime": parts[4],
        "component": parts[6],
        "subsystem": parts[7],
        "level": parts[8],
        "message": " ".join(parts[9:])
    }