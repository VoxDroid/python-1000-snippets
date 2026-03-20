# sample1.py
# Simulate a PID controller tracking a setpoint for a second-order plant.

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


def simulate_step_response(dt: float = 0.01, t_end: float = 5.0):
    # Second-order plant: x" + 2*zeta*wn*x' + wn^2*x = K*u
    wn = 2.0
    zeta = 0.7
    K = 1.0

    # State: [x, x_dot]
    state = np.array([0.0, 0.0])
    setpoint = 1.0

    pid = PID(kp=8.0, ki=1.0, kd=0.5, dt=dt)

    t = np.arange(0.0, t_end, dt)
    output = []

    for _ in t:
        u = pid.compute(setpoint, state[0])
        x, x_dot = state
        # dynamics
        x_ddot = K * u - 2 * zeta * wn * x_dot - (wn**2) * x
        state = np.array([x + dt * x_dot, x_dot + dt * x_ddot])
        output.append(state[0])

    return t, np.array(output)


def main() -> None:
    t, y = simulate_step_response()
    print("Final value (approx):", round(float(y[-1]), 3))
    print("First 5 output values:", [round(float(v), 3) for v in y[:5]])


if __name__ == "__main__":
    main()
