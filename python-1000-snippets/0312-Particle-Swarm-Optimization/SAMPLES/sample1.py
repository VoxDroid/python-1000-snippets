#!/usr/bin/env python3
"""PSO optimizing a 2D sphere function (sum of squares)."""

import numpy as np


def sphere(x):
    return np.sum(x**2)


def pso_optimize(fitness, dim, num_particles=50, iterations=100):
    w = 0.5
    c1 = 1.5
    c2 = 1.5

    positions = np.random.randn(num_particles, dim)
    velocities = np.zeros_like(positions)

    pbest = positions.copy()
    pbest_score = np.apply_along_axis(fitness, 1, positions)

    gbest_idx = np.argmin(pbest_score)
    gbest = pbest[gbest_idx].copy()

    for _ in range(iterations):
        r1 = np.random.rand(num_particles, dim)
        r2 = np.random.rand(num_particles, dim)

        velocities = (
            w * velocities
            + c1 * r1 * (pbest - positions)
            + c2 * r2 * (gbest - positions)
        )
        positions += velocities

        scores = np.apply_along_axis(fitness, 1, positions)
        improved = scores < pbest_score
        pbest[improved] = positions[improved]
        pbest_score[improved] = scores[improved]

        gbest_idx = np.argmin(pbest_score)
        gbest = pbest[gbest_idx].copy()

    return gbest, pbest_score[gbest_idx]


def main():
    best_pos, best_score = pso_optimize(sphere, dim=2)
    print(f"Best position: {np.round(best_pos, 2)}, fitness: {best_score:.4f}")


if __name__ == '__main__':
    main()
