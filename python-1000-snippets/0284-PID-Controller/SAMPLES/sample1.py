# sample1.py
# Simple PID controller class and step response simulation for a first-order plant.

import numpy as np


class PID:
    def __init__(self, Kp=1.0, Ki=0.0, Kd=0.0, dt=0.1, integral_limit=None):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        self.integral = 0.0
        self.prev_error = 0.0
        self.integral_limit = integral_limit

    def update(self, error):
        self.integral += error * self.dt
        if self.integral_limit is not None:
            self.integral = np.clip(self.integral, -self.integral_limit, self.integral_limit)

        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error

        return self.Kp * error + self.Ki * self.integral + self.Kd * derivative


def simulate(setpoint=1.0, steps=50):
    pid = PID(Kp=2.0, Ki=0.5, Kd=0.1, dt=0.1, integral_limit=10.0)
    x = 0.0
    dt = 0.1
    history = []

    for _ in range(steps):
        error = setpoint - x
        u = pid.update(error)
        # Plant: x' = -x + u
        x += dt * (-x + u)
        history.append(x)

    return np.array(history)


if __name__ == '__main__':
    response = simulate()
    print('Final output:', response[-1])
    print('First 5 outputs:', np.round(response[:5], 3))
