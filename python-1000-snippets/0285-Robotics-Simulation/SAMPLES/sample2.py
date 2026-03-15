# sample2.py
# Forward kinematics for a simple 2-joint planar robot arm.

import numpy as np


def forward_kinematics(theta1, theta2, l1=1.0, l2=0.5):
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return x, y


if __name__ == '__main__':
    angles = [(0.0, 0.0), (np.pi / 6, np.pi / 6), (np.pi / 4, -np.pi / 6)]
    for theta1, theta2 in angles:
        x, y = forward_kinematics(theta1, theta2)
        print(f"theta1={theta1:.2f}, theta2={theta2:.2f} -> (x, y)=({x:.3f}, {y:.3f})")
