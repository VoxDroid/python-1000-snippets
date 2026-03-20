# sample2.py
# Solve inverse kinematics for a 2-link planar arm using iterative Jacobian transpose.

import numpy as np


def forward_kinematics(theta1: float, theta2: float, l1: float = 1.0, l2: float = 1.0):
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return np.array([x, y])


def jacobian(theta1: float, theta2: float, l1: float = 1.0, l2: float = 1.0):
    j11 = -l1 * np.sin(theta1) - l2 * np.sin(theta1 + theta2)
    j12 = -l2 * np.sin(theta1 + theta2)
    j21 = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    j22 = l2 * np.cos(theta1 + theta2)
    return np.array([[j11, j12], [j21, j22]])


def inverse_kinematics(target: np.ndarray, initial: np.ndarray, steps: int = 100, alpha: float = 0.5):
    theta = initial.copy()
    for _ in range(steps):
        pos = forward_kinematics(theta[0], theta[1])
        error = target - pos
        if np.linalg.norm(error) < 1e-3:
            break
        J = jacobian(theta[0], theta[1])
        theta += alpha * J.T @ error
    return theta


def main() -> None:
    target = np.array([1.0, 1.0])
    initial = np.array([0.1, 0.1])

    angles = inverse_kinematics(target, initial)
    position = forward_kinematics(angles[0], angles[1])

    print("Solved joint angles:", np.round(angles, 3).tolist())
    print("Resulting end effector:", np.round(position, 3).tolist())


if __name__ == "__main__":
    main()
