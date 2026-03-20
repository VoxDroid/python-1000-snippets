# sample2.py
# Compute basic statistics for heatmap data and print a summary report.

from __future__ import annotations


def generate_heatmap_data(rows: int = 8, cols: int = 8):
    return [[(r + 1) * (c + 1) for c in range(cols)] for r in range(rows)]


def summarize(data: list[list[float]]):
    flat = [v for row in data for v in row]
    return {
        "min": min(flat),
        "max": max(flat),
        "mean": sum(flat) / len(flat),
    }


def main() -> None:
    data = generate_heatmap_data()
    stats = summarize(data)
    print("Heatmap Summary")
    print(f"  min: {stats['min']}")
    print(f"  max: {stats['max']}")
    print(f"  mean: {stats['mean']:.2f}")


if __name__ == "__main__":
    main()
