# sample1.py
# Compute the step response of a second-order critically damped system analytically.

import numpy as np


def step_response_critically_damped(t, omega_n=1.0):
    # For transfer function 1/(s+omega_n)^2, step response is:
    # y(t) = 1 - (1 + omega_n*t) * exp(-omega_n*t)
    return 1 - (1 + omega_n * t) * np.exp(-omega_n * t)


if __name__ == '__main__':
    t = np.linspace(0, 5, 101)
    y = step_response_critically_damped(t, omega_n=1.0)

    print("Final output (t=5):", y[-1])
    print("First 5 outputs:", np.round(y[:5], 4))
