# sample3.py
# Create an ASCII heatmap view in the console from generated data.

from __future__ import annotations


def generate_heatmap(rows: int = 10, cols: int = 30):
    # Generate an ASCII-friendly heatmap using sine waves.
    data = []
    for r in range(rows):
        row = []
        for c in range(cols):
            value = 0.5 + 0.5 * __import__("math").sin(r * 0.3) * __import__("math").cos(c * 0.2)
            row.append(value)
        data.append(row)
    return data


def render_ascii(data: list[list[float]]) -> str:
    chars = " .:-=+*#%@"
    min_v = min(v for row in data for v in row)
    max_v = max(v for row in data for v in row)
    span = max_v - min_v if max_v > min_v else 1.0
    lines = []
    for row in data:
        line = "".join(chars[int((v - min_v) / span * (len(chars) - 1))] for v in row)
        lines.append(line)
    return "\n".join(lines)


def main() -> None:
    data = generate_heatmap(12, 50)
    print(render_ascii(data))


if __name__ == "__main__":
    main()
