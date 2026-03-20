# sample1.py
# Estimate a pinhole camera intrinsic matrix using DLT from synthetic correspondences.

import numpy as np


def create_chessboard_points(nx: int, ny: int, square_size: float = 1.0):
    xs = np.arange(nx) * square_size
    ys = np.arange(ny) * square_size
    grid = np.stack(np.meshgrid(xs, ys), -1)
    return grid.reshape(-1, 2)


def project_points(pts_3d: np.ndarray, K: np.ndarray, R: np.ndarray, t: np.ndarray):
    pts_cam = (R @ pts_3d.T) + t[:, None]
    pts_proj = K @ pts_cam
    pts_proj /= pts_proj[2:3, :]
    return pts_proj[:2, :].T


def calibrate_dlt(pts_3d: np.ndarray, pts_2d: np.ndarray):
    n = pts_3d.shape[0]
    A = []
    for i in range(n):
        X, Y, Z = pts_3d[i]
        u, v = pts_2d[i]
        A.append([X, Y, Z, 1, 0, 0, 0, 0, -u * X, -u * Y, -u * Z, -u])
        A.append([0, 0, 0, 0, X, Y, Z, 1, -v * X, -v * Y, -v * Z, -v])
    A = np.array(A)
    _, _, Vt = np.linalg.svd(A)
    P = Vt[-1].reshape(3, 4)
    return P


def main() -> None:
    # Create synthetic 3D points within a small volume for calibration.
    rng = np.random.RandomState(0)
    pts_3d = rng.rand(30, 3) * 2.0  # 30 random points in a 2x2x2 cube

    # Ground truth camera intrinsics
    fx, fy, cx, cy = 800.0, 800.0, 320.0, 240.0
    K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

    # Ground truth pose
    angle = np.deg2rad(15)
    R = np.array([[np.cos(angle), 0, np.sin(angle)], [0, 1, 0], [-np.sin(angle), 0, np.cos(angle)]])
    t = np.array([0.0, 0.0, 10.0])

    # Project points
    pts_2d = project_points(pts_3d, K, R, t)

    # Calibrate using DLT
    P = calibrate_dlt(pts_3d, pts_2d)

    print("Estimated projection matrix (first 3 cols are K*R):")
    print(np.round(P, 3))


if __name__ == "__main__":
    main()
