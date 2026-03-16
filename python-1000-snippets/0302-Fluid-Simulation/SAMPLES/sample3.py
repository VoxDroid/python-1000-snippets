# sample3.py
# Combine advection and diffusion for a simple fluid-like scalar field.

import numpy as np


def diffuse(field, rate=0.1):
    out = field.copy()
    h, w = field.shape
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            out[y, x] = field[y, x] + rate * (
                field[y - 1, x]
                + field[y + 1, x]
                + field[y, x - 1]
                + field[y, x + 1]
                - 4 * field[y, x]
            )
    return out


def advect(field, vel_x, vel_y, dt=0.1):
    h, w = field.shape
    out = np.zeros_like(field)
    for y in range(h):
        for x in range(w):
            sx = x - vel_x[y, x] * dt
            sy = y - vel_y[y, x] * dt
            sx = np.clip(sx, 0, w - 1)
            sy = np.clip(sy, 0, h - 1)
            x0, y0 = int(np.floor(sx)), int(np.floor(sy))
            x1, y1 = min(x0 + 1, w - 1), min(y0 + 1, h - 1)
            dx, dy = sx - x0, sy - y0
            a = field[y0, x0]
            b = field[y0, x1]
            c = field[y1, x0]
            d = field[y1, x1]
            out[y, x] = (
                a * (1 - dx) * (1 - dy)
                + b * dx * (1 - dy)
                + c * (1 - dx) * dy
                + d * dx * dy
            )
    return out


if __name__ == '__main__':
    size = 50
    field = np.zeros((size, size), dtype=float)
    field[size // 2, size // 2] = 1.0

    # Constant rotational velocity field
    cx, cy = size / 2, size / 2
    y, x = np.mgrid[0:size, 0:size]
    vx = -(y - cy)
    vy = x - cx
    norm = np.sqrt(vx ** 2 + vy ** 2) + 1e-6
    vx /= norm
    vy /= norm

    print('Initial mass:', float(np.sum(field)))
    for step in range(1, 6):
        field = advect(field, vx, vy, dt=0.5)
        field = diffuse(field, rate=0.1)
        print(f'Step {step}: center={field[size//2, size//2]:.4f} mass={np.sum(field):.4f}')
