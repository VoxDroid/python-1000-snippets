# sample2.py
# Advection of a scalar field using a simple semi-Lagrangian scheme.

import numpy as np


def bilinear_interp(grid, x, y):
    # grid shape (H, W)
    h, w = grid.shape
    x0 = int(np.floor(x))
    y0 = int(np.floor(y))
    x1 = min(x0 + 1, w - 1)
    y1 = min(y0 + 1, h - 1)

    sx = x - x0
    sy = y - y0

    a = grid[y0, x0]
    b = grid[y0, x1]
    c = grid[y1, x0]
    d = grid[y1, x1]

    return (a * (1 - sx) * (1 - sy)
            + b * sx * (1 - sy)
            + c * (1 - sx) * sy
            + d * sx * sy)


def advect(field, vel_x, vel_y, dt=0.1):
    h, w = field.shape
    out = np.zeros_like(field)
    for j in range(h):
        for i in range(w):
            # Backtrace to find source position
            x = i - vel_x[j, i] * dt
            y = j - vel_y[j, i] * dt
            x = np.clip(x, 0, w - 1)
            y = np.clip(y, 0, h - 1)
            out[j, i] = bilinear_interp(field, x, y)
    return out


if __name__ == '__main__':
    size = 50
    field = np.zeros((size, size), dtype=float)
    field[size // 2, size // 2] = 1.0

    # Circular velocity field around center
    cx, cy = size / 2, size / 2
    y, x = np.mgrid[0:size, 0:size]
    vx = -(y - cy)
    vy = x - cx
    norm = np.sqrt(vx ** 2 + vy ** 2) + 1e-6
    vx /= norm
    vy /= norm

    print('Initial center value:', field[size // 2, size // 2])
    for step in range(1, 6):
        field = advect(field, vx, vy, dt=1.0)
        center_val = field[size // 2, size // 2]
        print(f'Step {step}: center value {center_val:.4f}')

    print('Final total mass:', float(np.sum(field)))
