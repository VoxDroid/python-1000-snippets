# sample3.py
# Kalman filter with occasional missing measurements (prediction-only steps).

import numpy as np


def kalman_1d_missing(measurements, process_var=1e-3, meas_var=0.1):
    x = 0.0
    P = 1.0

    estimates = []
    for z in measurements:
        # Predict
        P = P + process_var

        if z is not None:
            # Update
            K = P / (P + meas_var)
            x = x + K * (z - x)
            P = (1 - K) * P

        estimates.append(x)
    return np.array(estimates)


if __name__ == '__main__':
    true_value = 10.0
    rng = np.random.default_rng(2)
    measurements = [true_value + rng.normal(scale=0.2) if i % 5 != 0 else None for i in range(25)]

    estimates = kalman_1d_missing(measurements)

    print("Measurements (None=missing):", measurements[:10])
    print("Estimates:", np.round(estimates[:10], 3))
    print("Final estimate:", estimates[-1])
