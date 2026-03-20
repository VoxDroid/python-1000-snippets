# sample3.py
# Simulate disturbance rejection by applying a step disturbance mid-run.

import numpy as np


class PID:
    def __init__(self, kp: float, ki: float, kd: float, dt: float):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, setpoint: float, measurement: float) -> float:
        error = setpoint - measurement
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative


def plant_step(state: np.ndarray, u: float, dt: float, disturbance: float = 0.0) -> np.ndarray:
    wn = 2.0
    zeta = 0.7
    x, x_dot = state
    x_ddot = u + disturbance - 2 * zeta * wn * x_dot - wn**2 * x
    x_next = x + dt * x_dot
    x_dot_next = x_dot + dt * x_ddot
    return np.array([x_next, x_dot_next])


def main() -> None:
    dt = 0.01
    steps = 600
    setpoint = 1.0
    pid = PID(kp=8.0, ki=1.0, kd=0.5, dt=dt)

    state = np.array([0.0, 0.0])
    output = []

    for i in range(steps):
        disturbance = 0.0
        # Apply a step disturbance at t=3 seconds
        if i == 300:
            disturbance = 1.0
        u = pid.compute(setpoint, state[0])
        state = plant_step(state, u, dt, disturbance)
        output.append(state[0])

    print("Value at disturbance:", round(float(output[300]), 3))
    print("Final value:", round(float(output[-1]), 3))


if __name__ == "__main__":
    main()
