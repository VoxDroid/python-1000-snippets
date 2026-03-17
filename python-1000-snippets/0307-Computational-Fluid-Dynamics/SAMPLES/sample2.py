#!/usr/bin/env python3
"""2D Burgers' equation (viscous flow) using finite differences."""

import numpy as np


def step_burgers(u, v, nu, dt, dx, dy):
    un = u.copy()
    vn = v.copy()
    nx, ny = u.shape

    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            u[i, j] = (
                un[i, j]
                - un[i, j] * dt / dx * (un[i, j] - un[i - 1, j])
                - vn[i, j] * dt / dy * (un[i, j] - un[i, j - 1])
                + nu * dt
                * (
                    (un[i + 1, j] - 2 * un[i, j] + un[i - 1, j]) / dx**2
                    + (un[i, j + 1] - 2 * un[i, j] + un[i, j - 1]) / dy**2
                )
            )
            v[i, j] = (
                vn[i, j]
                - un[i, j] * dt / dx * (vn[i, j] - vn[i - 1, j])
                - vn[i, j] * dt / dy * (vn[i, j] - vn[i, j - 1])
                + nu * dt
                * (
                    (vn[i + 1, j] - 2 * vn[i, j] + vn[i - 1, j]) / dx**2
                    + (vn[i, j + 1] - 2 * vn[i, j] + vn[i, j - 1]) / dy**2
                )
            )

    # Boundary conditions: u=v=0 on boundaries (no-slip)
    u[0, :] = u[-1, :] = u[:, 0] = u[:, -1] = 0
    v[0, :] = v[-1, :] = v[:, 0] = v[:, -1] = 0

    return u, v


def main():
    nx, ny = 50, 50
    u = np.zeros((nx, ny), dtype=float)
    v = np.zeros((nx, ny), dtype=float)

    # Initial condition: bump in the middle
    u[nx // 2 - 1 : nx // 2 + 2, ny // 2 - 1 : ny // 2 + 2] = 1.0
    v[nx // 2 - 1 : nx // 2 + 2, ny // 2 - 1 : ny // 2 + 2] = 1.0

    nu = 0.01
    dt = 0.001
    dx = dy = 1.0

    for _ in range(300):
        u, v = step_burgers(u, v, nu, dt, dx, dy)

    center_u = u[nx // 2, ny // 2]
    center_v = v[nx // 2, ny // 2]
    print(f"Center u: {center_u:.2f}, v: {center_v:.2f}")


if __name__ == '__main__':
    main()
