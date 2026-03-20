# sample1.py
# Compute forward kinematics for a 2-link planar arm and compute its Jacobian.

import numpy as np


def forward_kinematics(theta1: float, theta2: float, l1: float = 1.0, l2: float = 1.0):
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return np.array([x, y])


def jacobian(theta1: float, theta2: float, l1: float = 1.0, l2: float = 1.0):
    # Partial derivatives of the end effector position w.r.t. joint angles.
    j11 = -l1 * np.sin(theta1) - l2 * np.sin(theta1 + theta2)
    j12 = -l2 * np.sin(theta1 + theta2)
    j21 = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    j22 = l2 * np.cos(theta1 + theta2)
    return np.array([[j11, j12], [j21, j22]])


def main() -> None:
    theta1 = np.pi / 4
    theta2 = np.pi / 6
    pos = forward_kinematics(theta1, theta2)
    J = jacobian(theta1, theta2)

    print("End effector position:", np.round(pos, 3).tolist())
    print("Jacobian:\n", np.round(J, 3))


if __name__ == "__main__":
    main()
