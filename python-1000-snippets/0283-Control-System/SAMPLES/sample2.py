# sample2.py
# Simulate a PID controller on a first-order plant.

import numpy as np


def simulate_pid(setpoint=1.0, dt=0.1, steps=100, Kp=2.0, Ki=0.5, Kd=0.1):
    # Simple plant: x' = -a*x + b*u
    a, b = 1.0, 1.0
    x = 0.0
    integral = 0.0
    prev_error = 0.0

    history = []

    for _ in range(steps):
        error = setpoint - x
        integral += error * dt
        derivative = (error - prev_error) / dt
        u = Kp * error + Ki * integral + Kd * derivative

        # Plant dynamics (Euler integration)
        x += dt * (-a * x + b * u)

        history.append(x)
        prev_error = error

    return np.array(history)


if __name__ == '__main__':
    response = simulate_pid()
    print("Final output:", response[-1])
    print("First 5 outputs:", np.round(response[:5], 3))
