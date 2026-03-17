#!/usr/bin/env python3
"""Soft body grid that shows deformation under gravity."""

import numpy as np


class SoftBodyGrid:
    def __init__(self, width, height, spacing=1.0):
        self.width = width
        self.height = height
        self.spacing = float(spacing)
        self.points = np.zeros((width * height, 2), dtype=float)
        self.prev = np.zeros_like(self.points)
        self.fixed = np.zeros(width * height, dtype=bool)
        self.springs = []

        for y in range(height):
            for x in range(width):
                idx = y * width + x
                self.points[idx] = np.array([x * spacing, y * spacing])
        self.prev[:] = self.points

        # fix top row
        for x in range(width):
            self.fixed[x] = True

        # structural springs
        for y in range(height):
            for x in range(width):
                idx = y * width + x
                if x + 1 < width:
                    self._add_spring(idx, idx + 1)
                if y + 1 < height:
                    self._add_spring(idx, idx + width)

    def _add_spring(self, i, j):
        rest = np.linalg.norm(self.points[j] - self.points[i])
        self.springs.append((i, j, rest))

    def step(self, dt=0.02, gravity=(0.0, -9.8), damping=0.98, constraint_iters=6):
        velocity = (self.points - self.prev) * damping
        self.prev[:] = self.points
        self.points += velocity
        self.points += np.array(gravity) * (dt * dt)

        for _ in range(constraint_iters):
            for i, j, rest in self.springs:
                p1 = self.points[i]
                p2 = self.points[j]
                delta = p2 - p1
                dist = np.linalg.norm(delta)
                if dist == 0:
                    continue
                diff = (dist - rest) / dist
                correction = delta * 0.5 * diff
                if not self.fixed[i]:
                    self.points[i] += correction
                if not self.fixed[j]:
                    self.points[j] -= correction
            self.points[self.fixed] = self.prev[self.fixed]

    def max_spring_stretch(self):
        max_stretch = 0.0
        for i, j, rest in self.springs:
            dist = np.linalg.norm(self.points[j] - self.points[i])
            max_stretch = max(max_stretch, abs(dist - rest))
        return max_stretch


def main():
    body = SoftBodyGrid(width=5, height=5, spacing=1.0)
    initial_center_y = (body.height // 2) * body.spacing

    for _ in range(240):
        body.step(dt=0.05)

    center_idx = (body.height // 2) * body.width + (body.width // 2)
    center = body.points[center_idx]
    print(f"Center displacement: {center[1] - initial_center_y:.2f}")
    print(f"Max spring stretch: {body.max_spring_stretch():.2f}")


if __name__ == '__main__':
    main()
