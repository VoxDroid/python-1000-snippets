# sample2.py
# Complementary filter fusing gyroscope and accelerometer to estimate roll angle.

import numpy as np


def wrap_angle(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi


if __name__ == '__main__':
    np.random.seed(0)

    dt = 0.02
    total_time = 2.0
    steps = int(total_time / dt)

    # True roll behavior (sinusoidal)
    t = np.linspace(0, total_time, steps)
    true_roll = 0.5 * np.sin(2 * np.pi * 0.5 * t)

    # Complementary filter state
    roll_est = 0.0
    alpha = 0.98  # high-pass on gyro, low-pass on accel

    print('Time  TrueRoll  GyroRoll  AccelRoll  EstRoll')
    for i, tt in enumerate(t):
        # Simulated gyro measures roll rate (derivative) with noise
        gyro_rate = np.gradient(true_roll, dt)[i] + np.random.normal(scale=np.deg2rad(0.5))

        # Simulated accelerometer roll estimate (from gravity) with noise
        accel_roll = true_roll[i] + np.random.normal(scale=np.deg2rad(2.0))

        # Complementary filter update
        roll_est = alpha * (roll_est + gyro_rate * dt) + (1 - alpha) * accel_roll
        roll_est = wrap_angle(roll_est)

        if i % 25 == 0:
            print(f"{tt:.2f}  {true_roll[i]:.3f}  {gyro_rate*dt:.3f}  {accel_roll:.3f}  {roll_est:.3f}")
