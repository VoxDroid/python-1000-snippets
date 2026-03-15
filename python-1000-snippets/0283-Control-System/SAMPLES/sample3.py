# sample3.py
# Simulate a second-order plant under PD control.

import numpy as np


def simulate_pd(setpoint=1.0, dt=0.01, steps=200, Kp=20.0, Kd=5.0):
    # Discrete second-order plant: x'' + 2*zeta*wn*x' + wn^2*x = wn^2*u
    wn = 2.0
    zeta = 0.7

    x = 0.0
    v = 0.0
    history = []

    prev_error = setpoint - x
    for _ in range(steps):
        error = setpoint - x
        u = Kp * error + Kd * (error - prev_error) / dt

        # Plant update (Euler integration)
        a = wn ** 2 * u - 2 * zeta * wn * v - wn ** 2 * x
        v += a * dt
        x += v * dt

        history.append(x)
        prev_error = error

    return np.array(history)


if __name__ == '__main__':
    response = simulate_pd()
    print("Final output:", response[-1])
    print("First 5 outputs:", np.round(response[:5], 4))
