# sample2.py
# Compute summary statistics for a small dataset and print a dashboard report.

from __future__ import annotations


def build_dataset() -> list[dict[str, float]]:
    return [
        {"item": "A", "value": 10.0, "score": 0.75},
        {"item": "B", "value": 22.5, "score": 0.52},
        {"item": "C", "value": 15.1, "score": 0.95},
        {"item": "D", "value": 7.3, "score": 0.33},
    ]


def summarize(data: list[dict[str, float]]) -> dict[str, dict[str, float]]:
    summary = {}
    numeric_keys = [k for k in data[0].keys() if k != "item"]
    for k in numeric_keys:
        values = [row[k] for row in data]
        summary[k] = {
            "min": min(values),
            "max": max(values),
            "mean": sum(values) / len(values),
        }
    return summary


def print_summary(summary: dict[str, dict[str, float]]) -> None:
    print("Dashboard Summary")
    for key, stats in summary.items():
        print(f"{key}: min={stats['min']:.2f}, max={stats['max']:.2f}, mean={stats['mean']:.2f}")


def main() -> None:
    data = build_dataset()
    summary = summarize(data)
    print_summary(summary)


if __name__ == "__main__":
    main()
