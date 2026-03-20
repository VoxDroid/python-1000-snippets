# sample3.py
# Generate a joint-space trajectory and compute corresponding end-effector positions.

import numpy as np


def forward_kinematics(theta1: float, theta2: float, l1: float = 1.0, l2: float = 1.0):
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return np.array([x, y])


def main() -> None:
    # Sweep joint 1 from 0 to 90 degrees and joint 2 from -45 to 45 degrees.
    theta1_values = np.linspace(0, np.pi / 2, 10)
    theta2_values = np.linspace(-np.pi / 4, np.pi / 4, 10)

    positions = []
    for t1, t2 in zip(theta1_values, theta2_values):
        positions.append(forward_kinematics(t1, t2))

    positions = np.array(positions)
    print("Trajectory points:", positions.shape[0])
    print("First 3 points:")
    for p in positions[:3]:
        print(" ", np.round(p, 3).tolist())


if __name__ == "__main__":
    main()
