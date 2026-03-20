# sample2.py
# Estimate a rigid transform between two sets of 2D points (feature matching).

import numpy as np


def estimate_rigid_transform(src: np.ndarray, dst: np.ndarray):
    # Compute centroids
    c_src = src.mean(axis=0)
    c_dst = dst.mean(axis=0)

    src_centered = src - c_src
    dst_centered = dst - c_dst
    H = src_centered.T @ dst_centered
    U, S, Vt = np.linalg.svd(H)
    R = Vt.T @ U.T
    if np.linalg.det(R) < 0:
        Vt[-1, :] *= -1
        R = Vt.T @ U.T
    t = c_dst - R @ c_src
    return R, t


def main() -> None:
    rng = np.random.RandomState(0)
    src = rng.rand(10, 2) * 5.0
    angle = np.deg2rad(15)
    R_true = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    t_true = np.array([1.5, -0.5])
    dst = (src @ R_true.T) + t_true

    R_est, t_est = estimate_rigid_transform(src, dst)

    print("True translation:", t_true)
    print("Estimated translation:", np.round(t_est, 3).tolist())
    print("True rotation angle (deg):", 15)
    estimated_angle = np.degrees(np.arctan2(R_est[1, 0], R_est[0, 0]))
    print("Estimated rotation angle (deg):", round(estimated_angle, 2))


if __name__ == "__main__":
    main()
