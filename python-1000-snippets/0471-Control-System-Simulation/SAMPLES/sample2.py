# sample2.py
# Explore PID tuning by varying gains and observing settling time.

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


def simulate(plant_fn, pid: PID, setpoint: float, dt: float, steps: int):
    state = np.array([0.0, 0.0])
    history = []
    for _ in range(steps):
        u = pid.compute(setpoint, state[0])
        state = plant_fn(state, u, dt)
        history.append(state[0])
    return np.array(history)


def plant(state: np.ndarray, u: float, dt: float):
    wn = 2.0
    zeta = 0.7
    x, x_dot = state
    x_ddot = u - 2 * zeta * wn * x_dot - wn**2 * x
    x_next = x + dt * x_dot
    x_dot_next = x_dot + dt * x_ddot
    return np.array([x_next, x_dot_next])


def main() -> None:
    dt = 0.01
    steps = 500
    setpoint = 1.0

    gains = [
        (4.0, 0.0, 0.2),
        (8.0, 1.0, 0.5),
        (12.0, 2.0, 1.0),
    ]

    for kp, ki, kd in gains:
        pid = PID(kp, ki, kd, dt)
        output = simulate(plant, pid, setpoint, dt, steps)
        print(f"Kp={kp}, Ki={ki}, Kd={kd}, final={round(float(output[-1]), 3)}")


if __name__ == "__main__":
    main()
