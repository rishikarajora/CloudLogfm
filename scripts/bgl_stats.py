from pathlib import Path

log_file = Path("data/raw/BGL/BGL.log")

total_logs = 0
normal_logs = 0
anomaly_logs = 0

with open(
    log_file,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    for line in f:

        total_logs += 1

        label = line.split()[0]

        if label == "-":
            normal_logs += 1
        else:
            anomaly_logs += 1

print(f"Total Logs: {total_logs:,}")
print(f"Normal Logs: {normal_logs:,}")
print(f"Anomaly Logs: {anomaly_logs:,}")