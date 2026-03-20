# sample1.py
# Generate a heatmap matrix and save it as a CSV file.

import csv
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/heatmap.csv")


def generate_heatmap_data(rows: int = 10, cols: int = 10):
    # Simple gradient-based heatmap data
    data = []
    for r in range(rows):
        row = []
        for c in range(cols):
            value = (r + 1) * (c + 1)
            row.append(value)
        data.append(row)
    return data


def save_csv(path: str, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def main() -> None:
    data = generate_heatmap_data(16, 16)
    save_csv(OUTPUT_PATH, data)
    print("Saved heatmap data to", OUTPUT_PATH)


if __name__ == "__main__":
    main()
