# sample2.py
# Classify a simple pose (standing vs crouching) based on keypoint heights.

import numpy as np


def classify_pose(keypoints: np.ndarray) -> str:
    """Return a simple pose label based on knee and hip y-coordinates."""
    # keypoints: array of shape (N, 2) with (x, y) normalized in [0, 1].
    hip = keypoints[0]
    knee = keypoints[1]
    ankle = keypoints[2]

    # If knees are close to hips, assume crouching.
    if knee[1] - hip[1] < 0.1:
        return "crouching"
    # If ankles are much lower than knees, assume standing.
    if ankle[1] - knee[1] > 0.1:
        return "standing"
    return "unknown"


def main() -> None:
    # Example pose where knee is close to hip (crouch)
    crouch = np.array([[0.5, 0.4], [0.52, 0.45], [0.54, 0.47]])
    stand = np.array([[0.5, 0.4], [0.52, 0.6], [0.54, 0.9]])

    print("Crouch pose classification:", classify_pose(crouch))
    print("Standing pose classification:", classify_pose(stand))


if __name__ == "__main__":
    main()
