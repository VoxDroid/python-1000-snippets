# sample1.py
# Simulate a simple differential-drive robot in 2D.

import numpy as np


def simulate_diff_drive(left_vel, right_vel, wheel_base=0.5, dt=0.1, steps=50):
    x, y, theta = 0.0, 0.0, 0.0
    path = []
    for _ in range(steps):
        v = (left_vel + right_vel) / 2
        omega = (right_vel - left_vel) / wheel_base
        x += v * np.cos(theta) * dt
        y += v * np.sin(theta) * dt
        theta += omega * dt
        path.append((x, y, theta))
    return np.array(path)


if __name__ == '__main__':
    path = simulate_diff_drive(left_vel=1.0, right_vel=0.5, steps=100)
    print('Final pose (x,y,theta):', np.round(path[-1], 3))
    print('First 3 poses:', np.round(path[:3], 3))
