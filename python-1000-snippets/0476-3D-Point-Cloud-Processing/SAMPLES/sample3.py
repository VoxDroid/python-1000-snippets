# sample3.py
# Compute axis-aligned bounding box and apply a simple transformation.

import numpy as np


def axis_aligned_bbox(points: np.ndarray):
    min_pt = points.min(axis=0)
    max_pt = points.max(axis=0)
    return min_pt, max_pt


def translate(points: np.ndarray, offset: np.ndarray) -> np.ndarray:
    return points + offset


def main() -> None:
    rng = np.random.RandomState(2)
    points = rng.rand(200, 3) * 5.0

    min_pt, max_pt = axis_aligned_bbox(points)
    translated = translate(points, np.array([1.0, 2.0, -0.5]))

    print("BBox min:", np.round(min_pt, 3).tolist())
    print("BBox max:", np.round(max_pt, 3).tolist())
    print("Translated sample point:", np.round(translated[0], 3).tolist())


if __name__ == "__main__":
    main()
