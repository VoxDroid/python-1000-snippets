# sample1.py
# Simulate projectile motion with air drag.

import numpy as np


def simulate(v0, angle_deg, dt=0.01, t_max=5.0, drag_coeff=0.1):
    angle = np.deg2rad(angle_deg)
    v = np.array([v0 * np.cos(angle), v0 * np.sin(angle)])
    pos = np.array([0.0, 0.0])
    g = np.array([0.0, -9.81])

    traj = []
    t = 0.0
    while t < t_max and pos[1] >= 0:
        traj.append((t, pos.copy(), v.copy()))
        # drag ~ -k*v*|v|
        drag = -drag_coeff * v * np.linalg.norm(v)
        a = g + drag
        v = v + a * dt
        pos = pos + v * dt
        t += dt
    return traj


if __name__ == '__main__':
    traj = simulate(v0=20.0, angle_deg=45.0)
    print('Time  X(m)  Y(m)  Vx  Vy')
    for t, pos, v in traj[::int(len(traj)/10) or 1]:
        print(f"{t:.2f}  {pos[0]:.2f}  {pos[1]:.2f}  {v[0]:.2f}  {v[1]:.2f}")
    print('Total steps:', len(traj))
