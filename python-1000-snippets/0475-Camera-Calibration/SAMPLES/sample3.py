# sample3.py
# Demonstrate using calibration data to project 3D points and recover their image coordinates.

import numpy as np


def project_points(pts_3d: np.ndarray, K: np.ndarray, R: np.ndarray, t: np.ndarray):
    pts_cam = (R @ pts_3d.T) + t[:, None]
    pts_proj = K @ pts_cam
    pts_proj /= pts_proj[2:3, :]
    return pts_proj[:2, :].T


def main() -> None:
    # Assume known intrinsic matrix
    K = np.array([[800, 0, 320], [0, 800, 240], [0, 0, 1]])
    # Identity pose
    R = np.eye(3)
    t = np.array([[0.0], [0.0], [5.0]])

    pts_3d = np.array([[0.5, 0.5, 0.0], [-0.5, 0.5, 0.0], [0.0, -0.5, 0.0]])
    projected = project_points(pts_3d, K, R, t)

    print("Projected image points:")
    for p in projected:
        print(" ", np.round(p, 2).tolist())


if __name__ == "__main__":
    main()
