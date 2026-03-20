# sample1.py
# Generate a simple scatter plot data file (CSV) for offline plotting.

import csv
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/interactive_plot_data.csv")


def generate_data(num_points: int = 20):
    # Create a simple 2D spiral dataset
    data = []
    for i in range(num_points):
        theta = i * 0.3
        r = 0.5 + i * 0.1
        x = r * (1.0 + 0.1 * i) * (1 + 0.1 * i) * __import__("math").cos(theta)
        y = r * (1.0 + 0.1 * i) * (1 + 0.1 * i) * __import__("math").sin(theta)
        data.append({"x": x, "y": y, "label": "A" if i % 2 == 0 else "B"})
    return data


def save_csv(path: str, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["x", "y", "label"])
        writer.writeheader()
        writer.writerows(data)


def main() -> None:
    data = generate_data(30)
    save_csv(OUTPUT_PATH, data)
    print("Saved plot data to", OUTPUT_PATH)
    print("You can load it in a plotting tool or library for interactive plotting.")


if __name__ == "__main__":
    main()
