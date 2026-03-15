# sample1.py
# 1D Kalman filter fusing accelerometer-based prediction and GPS position measurements.

import numpy as np


def kalman_predict(x, P, A, B, u, Q):
    x = A @ x + B @ u
    P = A @ P @ A.T + Q
    return x, P


def kalman_update(x, P, z, H, R):
    y = z - H @ x
    S = H @ P @ H.T + R
    K = P @ H.T @ np.linalg.inv(S)
    x = x + K @ y
    P = (np.eye(len(x)) - K @ H) @ P
    return x, P


if __name__ == '__main__':
    np.random.seed(0)

    dt = 1.0
    A = np.array([[1.0, dt], [0.0, 1.0]])
    B = np.array([[0.5 * dt**2], [dt]])
    H = np.array([[1.0, 0.0]])

    process_noise = np.diag([0.1, 0.1]) ** 2
    acc_noise = 0.2 ** 2
    gps_noise = 0.5 ** 2

    # Initial state: position=0, velocity=1
    x = np.array([0.0, 1.0])
    P = np.eye(2) * 1.0

    # Simulated ground truth motion: constant acceleration
    true_acc = 0.2
    true_state = x.copy()

    print('Time  Pos_est  Vel_est  Pos_true  Vel_true')
    for t in range(1, 11):
        # True motion
        true_state = A @ true_state + B.flatten() * true_acc

        # IMU measures acceleration with noise
        imu_acc = true_acc + np.random.normal(scale=np.sqrt(acc_noise))

        # Predict step using IMU
        Q = process_noise + np.diag([0.0, acc_noise])
        x, P = kalman_predict(x, P, A, B, np.array([imu_acc]), Q)

        # GPS measurement (position) with noise
        z = np.array([true_state[0] + np.random.normal(scale=np.sqrt(gps_noise))])
        x, P = kalman_update(x, P, z, H, np.array([[gps_noise]]))

        print(f"{t:2d}    {x[0]:.2f}    {x[1]:.2f}    {true_state[0]:.2f}    {true_state[1]:.2f}")
