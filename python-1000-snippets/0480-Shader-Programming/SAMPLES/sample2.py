# sample2.py
# Evaluate a simple fragment-shader-like function and print a few sample values.

import math


def shader(x: float, y: float) -> tuple[int, int, int]:
    # Simulate a fragment shader using math operations.
    r = int(255 * abs(math.sin(3.0 * x)))
    g = int(255 * abs(math.sin(3.0 * y)))
    b = int(255 * abs(math.sin(3.0 * (x + y))))
    return (r, g, b)


def main() -> None:
    samples = [(0.1, 0.2), (0.5, 0.5), (0.9, 0.1)]
    for x, y in samples:
        print(f"shader({x:.2f},{y:.2f}) ->", shader(x, y))


if __name__ == "__main__":
    main()
