#!/usr/bin/env python3
"""Evolutionary strategy minimizing a 2D sphere function (sum of squares)."""

import numpy as np


def sphere(x):
    return np.sum(x**2)


def es_optimize(fitness_fn, dim, mu=20, lam=100, generations=100, sigma=0.1):
    # Initialize mu parents
    parents = np.random.randn(mu, dim)

    for _ in range(generations):
        # Generate lambda offspring with Gaussian mutation
        offspring = parents[np.random.choice(mu, lam)] + sigma * np.random.randn(lam, dim)
        combined = np.vstack((parents, offspring))
        scores = np.apply_along_axis(fitness_fn, 1, combined)
        # lower is better
        best_idx = np.argsort(scores)[:mu]
        parents = combined[best_idx]

    best = parents[0]
    return best, fitness_fn(best)


def main():
    best, value = es_optimize(sphere, dim=2)
    print(f"Best solution: {np.round(best, 2)}, fitness: {value:.4f}")


if __name__ == '__main__':
    main()
