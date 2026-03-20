# sample2.py
# Print a simple interactive plot description to the console.

from __future__ import annotations


def build_plot_data():
    return [(x, x**2) for x in range(-10, 11)]


def main() -> None:
    data = build_plot_data()
    print("Interactive Plot Data (x, y=x^2)")
    for x, y in data:
        print(f"({x}, {y})")
    print("\nTip: Use this data with a plotting library to create an interactive chart.")


if __name__ == "__main__":
    main()
