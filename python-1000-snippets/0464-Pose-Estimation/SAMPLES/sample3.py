# sample3.py
# Normalize and visualize pose keypoints by centering them at the mid-hip.

import numpy as np


def normalize_keypoints(keypoints: np.ndarray) -> np.ndarray:
    """Center keypoints around the mid-hip and scale to unit distance."""
    mid_hip = np.mean(keypoints[[0, 1]], axis=0)
    centered = keypoints - mid_hip
    scale = np.linalg.norm(centered, axis=1).max() or 1.0
    return centered / scale


def main() -> None:
    # Keypoints: [left_hip, right_hip, left_shoulder, right_shoulder]
    keypoints = np.array([
        [0.45, 0.65],
        [0.55, 0.65],
        [0.45, 0.35],
        [0.55, 0.35],
    ])

    normalized = normalize_keypoints(keypoints)
    print("Original keypoints:")
    print(keypoints)
    print("Normalized keypoints (centered and scaled):")
    print(np.round(normalized, 3))


if __name__ == "__main__":
    main()
