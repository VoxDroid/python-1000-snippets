# sample1.py
# Voxel grid downsampling of a random point cloud using NumPy.

import numpy as np


def voxel_downsample(points: np.ndarray, voxel_size: float) -> np.ndarray:
    # Compute voxel indices for each point
    voxel_indices = np.floor(points / voxel_size).astype(int)
    # Use a dict to average points within each voxel
    voxel_dict = {}
    for idx, p in zip(map(tuple, voxel_indices), points):
        if idx not in voxel_dict:
            voxel_dict[idx] = []
        voxel_dict[idx].append(p)
    downsampled = np.array([np.mean(voxel_dict[k], axis=0) for k in voxel_dict])
    return downsampled


def main() -> None:
    rng = np.random.RandomState(0)
    points = rng.rand(500, 3) * 10.0

    downsampled = voxel_downsample(points, voxel_size=0.5)
    print("Original point count:", points.shape[0])
    print("Downsampled point count:", downsampled.shape[0])
    print("Sample downsampled points (first 3):")
    for p in downsampled[:3]:
        print(" ", np.round(p, 3).tolist())


if __name__ == "__main__":
    main()
