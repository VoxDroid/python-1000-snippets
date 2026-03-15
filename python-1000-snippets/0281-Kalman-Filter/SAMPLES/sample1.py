# sample1.py
# 1D Kalman filter: estimate a constant position from noisy measurements.

import numpy as np


def kalman_1d(measurements, process_var=1e-3, meas_var=0.1):
    # State: position; P: uncertainty
    x = 0.0
    P = 1.0

    estimates = []
    for z in measurements:
        # Predict
        P = P + process_var

        # Update
        K = P / (P + meas_var)
        x = x + K * (z - x)
        P = (1 - K) * P

        estimates.append(x)
    return np.array(estimates)


if __name__ == '__main__':
    # Simulate noisy observations of a constant value (true=5.0)
    true_value = 5.0
    rng = np.random.default_rng(0)
    measurements = true_value + rng.normal(scale=0.5, size=20)

    estimates = kalman_1d(measurements)

    print("Measurements:", np.round(measurements[:5], 3))
    print("Estimates:", np.round(estimates[:5], 3))
    print("Final estimate:", estimates[-1])
