#!/usr/bin/env python3
"""PSO optimizing a 1D Rastrigin-like multimodal function."""

import numpy as np


def rastrigin(x):
    x = np.asarray(x)
    return 10 * len(x) + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))


def pso_optimize(fitness, dim, num_particles=40, iterations=150):
    w = 0.7
    c1 = 1.4
    c2 = 1.4

    positions = np.random.uniform(-5, 5, (num_particles, dim))
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
    best_pos, best_score = pso_optimize(rastrigin, dim=1)
    print(f"Best position: {np.round(best_pos, 2)}, fitness: {best_score:.2f}")


if __name__ == '__main__':
    main()
