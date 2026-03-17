#!/usr/bin/env python3
"""Soft body impact simulation (apply impulse and measure deformation)."""

import numpy as np


class SoftBody:
    def __init__(self, points, springs, fixed=None):
        self.points = np.array(points, dtype=float)
        self.prev = self.points.copy()
        self.springs = springs
        self.fixed = np.zeros(len(points), dtype=bool)
        if fixed is not None:
            self.fixed[fixed] = True

    def step(self, dt=0.02, gravity=(0.0, -9.8), damping=0.98, constraint_iters=6):
        velocity = (self.points - self.prev) * damping
        self.prev = self.points.copy()
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
        return max(
            abs(np.linalg.norm(self.points[j] - self.points[i]) - rest)
            for i, j, rest in self.springs
        )


def main():
    points = [
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 1.0],
    ]
    springs = [
        (0, 1, 1.0),
        (0, 2, 1.0),
        (1, 3, 1.0),
        (2, 3, 1.0),
        (0, 3, np.sqrt(2)),
        (1, 2, np.sqrt(2)),
    ]
    body = SoftBody(points, springs, fixed=[0])

    # Apply an impulse to point 3
    body.points[3] += np.array([0.5, 0.5])

    for _ in range(120):
        body.step(dt=0.02)

    print(f"Max spring stretch: {body.max_spring_stretch():.3f}")
    print(f"Point 3 position: {body.points[3]}")


if __name__ == '__main__':
    main()
