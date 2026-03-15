# sample2.py
# Triangulate multiple points from two views and compute average reconstruction error.

import cv2
import numpy as np


def project_points(P, points_3d):
    pts_h = np.vstack((points_3d.T, np.ones((1, points_3d.shape[0]))))
    proj = P @ pts_h
    proj = proj[:2] / proj[2:3]
    return proj.T


if __name__ == '__main__':
    # Create a grid of 3D points in front of the cameras
    points = np.array([[x, y, 5.0] for x in (-1, 0, 1) for y in (-1, 0, 1)], dtype=np.float32)

    K = np.array([[800.0, 0, 320.0], [0, 800.0, 240.0], [0, 0, 1.0]])
    R1 = np.eye(3)
    t1 = np.zeros((3, 1))
    R2 = np.eye(3)
    t2 = np.array([[0.2], [0.0], [0.0]])

    P1 = K @ np.hstack((R1, t1))
    P2 = K @ np.hstack((R2, t2))

    pts1 = project_points(P1, points)
    pts2 = project_points(P2, points)

    # Triangulate all points at once
    pts1_t = pts1.T.reshape(2, -1)
    pts2_t = pts2.T.reshape(2, -1)
    X_est_h = cv2.triangulatePoints(P1, P2, pts1_t, pts2_t)
    X_est = (X_est_h[:3] / X_est_h[3]).T

    errors = np.linalg.norm(X_est - points, axis=1)
    print(f"Mean reconstruction error: {float(np.mean(errors)):.6f}")
    print(f"Max reconstruction error: {float(np.max(errors)):.6f}")
