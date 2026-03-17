#!/usr/bin/env python3
"""2D diffusion (heat equation) using finite differences."""

import numpy as np


def diffuse(u, alpha, dt):
    un = u.copy()
    nx, ny = u.shape
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            u[i, j] = un[i, j] + alpha * dt * (
                un[i + 1, j]
                + un[i - 1, j]
                + un[i, j + 1]
                + un[i, j - 1]
                - 4 * un[i, j]
            )
    return u


def main():
    nx, ny = 50, 50
    u = np.zeros((nx, ny), dtype=float)
    # initial hot spot in the center
    u[nx // 2, ny // 2] = 1.0

    alpha = 0.1
    dt = 0.1

    for _ in range(120):
        u = diffuse(u, alpha, dt)

    center = u[nx // 2, ny // 2]
    print(f"Center temp: {center:.2f}")


if __name__ == '__main__':
    main()
