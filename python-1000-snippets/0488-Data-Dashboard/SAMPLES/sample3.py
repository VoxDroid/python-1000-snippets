# sample3.py
# Write a simple dashboard report to a file, refreshing it in a loop.

import os
import time

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/dashboard.txt")


def build_metrics(frame: int) -> dict[str, float]:
    # Simulate some changing metrics.
    base = 100.0 + frame * 0.5
    return {
        "metric_a": base % 100,
        "metric_b": (base * 1.5) % 50,
        "metric_c": (base ** 0.5) * 2,
    }


def format_dashboard(frame: int, metrics: dict[str, float]) -> str:
    lines = [f"Frame: {frame}", "Dashboard Metrics:"]
    for k, v in metrics.items():
        lines.append(f"  {k}: {v:.2f}")
    return "\n".join(lines) + "\n"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    for frame in range(5):
        metrics = build_metrics(frame)
        dashboard_text = format_dashboard(frame, metrics)
        with open(OUTPUT_PATH, "w") as f:
            f.write(dashboard_text)
        print(f"Wrote dashboard frame {frame} to {OUTPUT_PATH}")
        time.sleep(0.1)


if __name__ == "__main__":
    main()
