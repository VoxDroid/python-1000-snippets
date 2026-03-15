# sample2.py
# Demonstrate integral windup and anti-windup in a PID controller.

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

    def update(self, error, anti_windup=False):
        self.integral += error * self.dt
        if anti_windup and self.integral_limit is not None:
            self.integral = np.clip(self.integral, -self.integral_limit, self.integral_limit)

        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        return self.Kp * error + self.Ki * self.integral + self.Kd * derivative


def simulate(anti_windup=False):
    pid = PID(Kp=0.8, Ki=1.0, Kd=0.1, dt=0.1, integral_limit=10.0)
    x = 0.0
    dt = 0.1
    setpoint = 1.0

    history = []
    for _ in range(60):
        error = setpoint - x
        u = pid.update(error, anti_windup=anti_windup)
        # Saturate actuator to [-1, 1]
        u = np.clip(u, -1, 1)
        x += dt * (-x + u)
        history.append(x)

    return np.array(history)


if __name__ == '__main__':
    no_aw = simulate(anti_windup=False)
    with_aw = simulate(anti_windup=True)

    print('Final output without anti-windup:', np.round(no_aw[-1], 3))
    print('Final output with anti-windup:', np.round(with_aw[-1], 3))
