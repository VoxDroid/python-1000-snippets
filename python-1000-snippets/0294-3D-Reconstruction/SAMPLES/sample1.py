# sample1.py
# Basic stereo triangulation: reconstruct a 3D point from two image observations.

import cv2
import numpy as np


if __name__ == '__main__':
    # Define a 3D point in world coordinates (homogeneous)
    X = np.array([1.0, 2.0, 5.0, 1.0])

    # Camera intrinsics (simple pinhole, focal length 800, principal point at (320,240))
    K = np.array([[800.0, 0.0, 320.0], [0.0, 800.0, 240.0], [0.0, 0.0, 1.0]])

    # Camera poses: first at origin, second translated along X
    R1 = np.eye(3)
    t1 = np.zeros((3, 1))
    R2 = np.eye(3)
    t2 = np.array([[0.2], [0.0], [0.0]])

    P1 = K @ np.hstack((R1, t1))
    P2 = K @ np.hstack((R2, t2))

    # Project the point into each image
    x1_h = P1 @ X
    x2_h = P2 @ X
    x1 = (x1_h[:2] / x1_h[2]).reshape(2, 1)
    x2 = (x2_h[:2] / x2_h[2]).reshape(2, 1)

    # Triangulate the point
    X_est_h = cv2.triangulatePoints(P1, P2, x1, x2)
    X_est = (X_est_h[:3] / X_est_h[3]).flatten()

    error = np.linalg.norm(X_est - X[:3])
    print(f"Reconstructed 3D point: {X_est}")
    print(f"Ground truth 3D point: {X[:3]}")
    print(f"Reconstruction error: {error:.6f}")
