# sample2.py
# Simulate a spring-mass-damper system using Euler integration.

import numpy as np


def simulate(k=10.0, b=1.0, m=1.0, x0=1.0, v0=0.0, dt=0.01, t_max=5.0):
    x = x0
    v = v0
    history = []
    t = 0.0
    while t < t_max:
        # F = -kx - bv
        a = (-k * x - b * v) / m
        v = v + a * dt
        x = x + v * dt
        history.append((t, x, v))
        t += dt
    return history


if __name__ == '__main__':
    hist = simulate()
    print('Time  Position  Velocity')
    for t, x, v in hist[::int(len(hist)/10) or 1]:
        print(f"{t:.2f}  {x:.3f}  {v:.3f}")
    print('Total steps:', len(hist))
