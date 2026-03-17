#!/usr/bin/env python3
"""Simple incompressible flow step with pressure Poisson solver."""

import numpy as np


def build_up_b(rho, dt, u, v, dx, dy):
    b = np.zeros_like(u)
    b[1:-1, 1:-1] = (
        rho
        * (
            1
            / dt
            * (
                (u[1:-1, 2:] - u[1:-1, :-2]) / (2 * dx)
                + (v[2:, 1:-1] - v[:-2, 1:-1]) / (2 * dy)
            )
            - ((u[1:-1, 2:] - u[1:-1, :-2]) / (2 * dx)) ** 2
            - 2
            * ((u[2:, 1:-1] - u[:-2, 1:-1]) / (2 * dy))
            * ((v[1:-1, 2:] - v[1:-1, :-2]) / (2 * dx))
            - ((v[2:, 1:-1] - v[:-2, 1:-1]) / (2 * dy)) ** 2
        )
    )
    return b


def pressure_poisson(p, dx, dy, b, nit=50):
    pn = np.empty_like(p)
    for _ in range(nit):
        pn[:] = p
        p[1:-1, 1:-1] = (
            (
                pn[1:-1, 2:]
                + pn[1:-1, :-2]
            )
            * dy**2
            + (
                pn[2:, 1:-1]
                + pn[:-2, 1:-1]
            )
            * dx**2
            - b[1:-1, 1:-1] * dx**2 * dy**2
        ) / (2 * (dx**2 + dy**2))

        # boundary conditions: dp/dn = 0 at walls
        p[:, -1] = p[:, -2]
        p[0, :] = p[1, :]
        p[:, 0] = p[:, 1]
        p[-1, :] = 0

    return p


def main():
    nx, ny = 50, 50
    rho = 1.0
    nu = 0.1
    dt = 0.001
    dx = dy = 1.0

    u = np.zeros((ny, nx), dtype=float)
    v = np.zeros((ny, nx), dtype=float)
    p = np.zeros((ny, nx), dtype=float)

    # simple lid-driven cavity: top boundary moves right
    for _ in range(100):
        b = build_up_b(rho, dt, u, v, dx, dy)
        p = pressure_poisson(p, dx, dy, b, nit=50)

        un = u.copy()
        vn = v.copy()

        u[1:-1, 1:-1] = (
            un[1:-1, 1:-1]
            - un[1:-1, 1:-1] * dt / dx * (un[1:-1, 1:-1] - un[1:-1, :-2])
            - vn[1:-1, 1:-1] * dt / dy * (un[1:-1, 1:-1] - un[:-2, 1:-1])
            - dt / (2 * rho * dx) * (p[1:-1, 2:] - p[1:-1, :-2])
            + nu
            * (
                dt
                / dx**2
                * (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, :-2])
                + dt
                / dy**2
                * (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[:-2, 1:-1])
            )
        )

        v[1:-1, 1:-1] = (
            vn[1:-1, 1:-1]
            - un[1:-1, 1:-1] * dt / dx * (vn[1:-1, 1:-1] - vn[1:-1, :-2])
            - vn[1:-1, 1:-1] * dt / dy * (vn[1:-1, 1:-1] - vn[:-2, 1:-1])
            - dt / (2 * rho * dy) * (p[2:, 1:-1] - p[:-2, 1:-1])
            + nu
            * (
                dt
                / dx**2
                * (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, :-2])
                + dt
                / dy**2
                * (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[:-2, 1:-1])
            )
        )

        # Boundary conditions
        u[0, :] = 0
        u[:, 0] = 0
        u[:, -1] = 0
        u[-1, :] = 1  # lid velocity

        v[0, :] = 0
        v[-1, :] = 0
        v[:, 0] = 0
        v[:, -1] = 0

    vel = np.sqrt(u**2 + v**2)
    print(f"Max velocity magnitude: {vel.max():.2f}")


if __name__ == '__main__':
    main()
