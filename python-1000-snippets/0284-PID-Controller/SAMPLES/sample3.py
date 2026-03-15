# sample3.py
# PID controller responding to a changing setpoint.

import numpy as np


class PID:
    def __init__(self, Kp=1.0, Ki=0.0, Kd=0.0, dt=0.1):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, error):
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        return self.Kp * error + self.Ki * self.integral + self.Kd * derivative


def simulate(setpoints, dt=0.1):
    pid = PID(Kp=1.5, Ki=0.4, Kd=0.05, dt=dt)
    x = 0.0
    history = []

    for sp in setpoints:
        error = sp - x
        u = pid.update(error)
        x += dt * (-x + u)
        history.append((sp, x))

    return history


if __name__ == '__main__':
    setpoints = [0.0] * 20 + [1.0] * 40 + [0.5] * 20
    history = simulate(setpoints)

    print('Last 5 (setpoint, output):')
    for sp, out in history[-5:]:
        print(f'  {sp:.2f} -> {out:.3f}')
