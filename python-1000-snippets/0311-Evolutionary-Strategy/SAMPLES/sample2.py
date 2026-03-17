#!/usr/bin/env python3
"""Evolutionary strategy to minimize a shifted quadratic function."""

import numpy as np


def quadratic(x):
    # Minimum at (1, -2)
    return (x[0] - 1) ** 2 + (x[1] + 2) ** 2


def es_optimize(fitness_fn, dim, mu=20, lam=80, generations=120, sigma=0.2):
    parents = np.random.randn(mu, dim)

    for _ in range(generations):
        offspring = parents[np.random.choice(mu, lam)] + sigma * np.random.randn(lam, dim)
        combined = np.vstack((parents, offspring))
        scores = np.apply_along_axis(fitness_fn, 1, combined)
        best_idx = np.argsort(scores)[:mu]
        parents = combined[best_idx]

    best = parents[0]
    return best, fitness_fn(best)


def main():
    best, value = es_optimize(quadratic, dim=2)
    print(f"Best solution: {np.round(best, 2)}, fitness: {value:.4f}")


if __name__ == '__main__':
    main()
