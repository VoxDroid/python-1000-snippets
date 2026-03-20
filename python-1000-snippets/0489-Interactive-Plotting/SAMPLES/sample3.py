# sample3.py
# Create a simple interactive plot configuration output (e.g., JSON) that can be used by plotting tools.

import json
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../../temp/interactive_plot_config.json")


def build_plot_config():
    return {
        "title": "Sample Interactive Plot",
        "x_label": "X",
        "y_label": "Y",
        "series": [
            {"name": "sin", "data": [[x, __import__("math").sin(x / 2)] for x in range(0, 21)]},
            {"name": "cos", "data": [[x, __import__("math").cos(x / 2)] for x in range(0, 21)]},
        ],
    }


def main() -> None:
    config = build_plot_config()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(config, f, indent=2)
    print("Saved plot configuration to", OUTPUT_PATH)
    print("Load it into a plotting library to render an interactive plot.")


if __name__ == "__main__":
    main()
