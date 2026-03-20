# sample2.py
# Classify heightmap into water, land, and mountain regions.

import numpy as np


def classify_terrain(heightmap: np.ndarray):
    water = heightmap < 0.4
    land = (heightmap >= 0.4) & (heightmap < 0.7)
    mountain = heightmap >= 0.7
    return water, land, mountain


def main() -> None:
    heightmap = np.random.rand(50, 50)
    water, land, mountain = classify_terrain(heightmap)

    print("Water coverage:", round(float(np.mean(water)), 3))
    print("Land coverage:", round(float(np.mean(land)), 3))
    print("Mountain coverage:", round(float(np.mean(mountain)), 3))


if __name__ == "__main__":
    main()
