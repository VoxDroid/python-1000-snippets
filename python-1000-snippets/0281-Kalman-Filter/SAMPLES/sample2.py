# sample2.py
# 2D Kalman filter: track position and velocity with noisy position measurements.

import numpy as np


def kalman_2d(zs, dt=1.0, process_var=1e-3, meas_var=0.5):
    # State: [position, velocity]
    x = np.array([0.0, 0.0])
    P = np.eye(2)

    # State transition (constant velocity)
    F = np.array([[1, dt], [0, 1]])
    H = np.array([[1, 0]])
    Q = process_var * np.eye(2)
    R = np.array([[meas_var]])

    estimates = []
    for z in zs:
        # Predict
        x = F @ x
        P = F @ P @ F.T + Q

        # Update
        y = np.array([z]) - H @ x
        S = H @ P @ H.T + R
        K = P @ H.T @ np.linalg.inv(S)
        x = x + (K @ y).flatten()
        P = (np.eye(2) - K @ H) @ P

        estimates.append(x.copy())
    return np.array(estimates)


if __name__ == '__main__':
    true_positions = np.linspace(0, 10, 30)
    rng = np.random.default_rng(1)
    measurements = true_positions + rng.normal(scale=0.5, size=true_positions.shape)

    estimates = kalman_2d(measurements)

    print("First 5 measurements:", np.round(measurements[:5], 3))
    print("First 5 estimates (pos, vel):", np.round(estimates[:5], 3))
    print("Final estimated state:", np.round(estimates[-1], 3))
