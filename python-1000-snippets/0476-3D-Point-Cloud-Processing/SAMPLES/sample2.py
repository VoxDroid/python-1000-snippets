# sample2.py
# Estimate normals for each point using PCA on local neighbors.

import numpy as np


def estimate_normals(points: np.ndarray, k: int = 10) -> np.ndarray:
    normals = np.zeros_like(points)
    for i, p in enumerate(points):
        # find k nearest neighbors (brute force)
        dists = np.sum((points - p) ** 2, axis=1)
        idx = np.argsort(dists)[1 : k + 1]
        cov = np.cov(points[idx].T)
        eigvals, eigvecs = np.linalg.eigh(cov)
        normals[i] = eigvecs[:, 0]  # smallest eigenvalue eigenvector
    return normals


def main() -> None:
    rng = np.random.RandomState(1)
    points = rng.rand(100, 3) * 10.0

    normals = estimate_normals(points, k=8)
    print("Computed normals for", normals.shape[0], "points")
    print("Sample normals (first 3):")
    for n in normals[:3]:
        print(" ", np.round(n, 3).tolist())


if __name__ == "__main__":
    main()
