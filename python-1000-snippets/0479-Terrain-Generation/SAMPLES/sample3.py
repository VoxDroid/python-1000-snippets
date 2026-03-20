# sample3.py
# Generate a terrain contour representation based on a heightmap.

import numpy as np


def compute_contours(heightmap: np.ndarray, levels: list[float]):
    contours = {}
    for lv in levels:
        contours[lv] = np.argwhere(np.isclose(heightmap, lv, atol=0.02))
    return contours


def main() -> None:
    heightmap = np.linspace(0, 1, 2500).reshape(50, 50) + 0.1 * np.random.randn(50, 50)
    levels = [0.2, 0.4, 0.6, 0.8]
    contours = compute_contours(heightmap, levels)

    for lv, points in contours.items():
        print(f"Level {lv}: {len(points)} points")


if __name__ == "__main__":
    main()
