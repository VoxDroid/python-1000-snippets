# sample1.py
# Given synthetic keypoints, compute joint angles to mimic pose estimation output.

import numpy as np


def angle_between(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> float:
    """Compute the angle at point b formed by points a-b-c."""
    ba = a - b
    bc = c - b
    cos_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-8)
    return np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0)))


def main() -> None:
    # Simulate a simple pose: shoulder->elbow->wrist.
    shoulder = np.array([0.2, 0.5])
    elbow = np.array([0.4, 0.4])
    wrist = np.array([0.6, 0.6])

    elbow_angle = angle_between(shoulder, elbow, wrist)

    print("Shoulder:", shoulder.tolist())
    print("Elbow:", elbow.tolist())
    print("Wrist:", wrist.tolist())
    print(f"Computed elbow angle (degrees): {elbow_angle:.2f}")


if __name__ == "__main__":
    main()
