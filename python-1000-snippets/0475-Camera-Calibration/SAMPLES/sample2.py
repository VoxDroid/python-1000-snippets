# sample2.py
# Use known intrinsics to undistort 2D points with a simple radial distortion model.

import numpy as np


def distort_points(pts: np.ndarray, k1: float = -0.2, k2: float = 0.05):
    x = (pts[:, 0] - 320) / 800
    y = (pts[:, 1] - 240) / 800
    r2 = x**2 + y**2
    factor = 1 + k1 * r2 + k2 * r2**2
    xd = x * factor
    yd = y * factor
    return np.stack([xd * 800 + 320, yd * 800 + 240], axis=1)


def undistort_points(pts: np.ndarray, k1: float, k2: float, iterations: int = 5):
    undistorted = pts.copy().astype(float)
    for _ in range(iterations):
        x = (undistorted[:, 0] - 320) / 800
        y = (undistorted[:, 1] - 240) / 800
        r2 = x**2 + y**2
        factor = 1 + k1 * r2 + k2 * r2**2
        undistorted[:, 0] = (pts[:, 0] - 320) / factor * 800 + 320
        undistorted[:, 1] = (pts[:, 1] - 240) / factor * 800 + 240
    return undistorted


def main() -> None:
    pts = np.array([[100.0, 100.0], [200.0, 150.0], [300.0, 200.0]])
    distorted = distort_points(pts)
    undistorted = undistort_points(distorted, k1=-0.2, k2=0.05)

    print("Original points:", pts.tolist())
    print("Distorted points:", np.round(distorted, 2).tolist())
    print("Undistorted points (approx):", np.round(undistorted, 2).tolist())


if __name__ == "__main__":
    main()
