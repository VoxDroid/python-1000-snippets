#!/usr/bin/env python3
"""Cloth simulation sample (prints corner positions)."""

import numpy as np


class Cloth:
    def __init__(self, width, height, spacing=1.0, fixed_indices=None):
        self.w = width
        self.h = height
        self.spacing = float(spacing)
        self.positions = np.zeros((height, width, 2), dtype=float)
        self.prev_positions = np.zeros_like(self.positions)

        for y in range(height):
            for x in range(width):
                self.positions[y, x] = np.array([x * self.spacing, y * self.spacing])
        self.prev_positions[:] = self.positions

        self.fixed = np.zeros((height, width), dtype=bool)
        if fixed_indices is None:
            self.fixed[0, :] = True
        else:
            for (y, x) in fixed_indices:
                self.fixed[y, x] = True

        self.rest_length = self.spacing

    def step(self, dt=0.02, gravity=(0.0, 9.8), damping=0.99, constraint_iters=5):
        # Verlet integration
        current = self.positions
        previous = self.prev_positions
        velocity = (current - previous) * damping
        acceleration = np.array(gravity, dtype=float)

        next_pos = current + velocity + acceleration * (dt * dt)
        self.prev_positions = current.copy()
        self.positions = next_pos

        # Constraint relaxation (simple structural + shear springs)
        for _ in range(constraint_iters):
            self._satisfy_constraints()
            self.positions[self.fixed] = self.prev_positions[self.fixed]

    def _satisfy_constraints(self):
        for y in range(self.h):
            for x in range(self.w):
                if x + 1 < self.w:
                    self._satisfy_spring(y, x, y, x + 1)
                if y + 1 < self.h:
                    self._satisfy_spring(y, x, y + 1, x)
                if x + 1 < self.w and y + 1 < self.h:
                    self._satisfy_spring(y, x, y + 1, x + 1)
                if x > 0 and y + 1 < self.h:
                    self._satisfy_spring(y, x, y + 1, x - 1)

    def _satisfy_spring(self, y1, x1, y2, x2):
        p1 = self.positions[y1, x1]
        p2 = self.positions[y2, x2]
        delta = p2 - p1
        dist = np.linalg.norm(delta)
        if dist == 0:
            return
        diff = (dist - self.rest_length) / dist
        correction = delta * 0.5 * diff

        if not self.fixed[y1, x1]:
            self.positions[y1, x1] += correction
        if not self.fixed[y2, x2]:
            self.positions[y2, x2] -= correction


def main():
    cloth = Cloth(width=5, height=5, spacing=1.0)

    # Run a few steps to let the cloth sag under gravity
    for _ in range(120):
        cloth.step(dt=0.02)

    tl = cloth.positions[0, 0]
    tr = cloth.positions[0, -1]
    bl = cloth.positions[-1, 0]
    br = cloth.positions[-1, -1]

    print(f"Top-left: {tl}")
    print(f"Top-right: {tr}")
    print(f"Bottom-left: {bl}")
    print(f"Bottom-right: {br}")


if __name__ == '__main__':
    main()
