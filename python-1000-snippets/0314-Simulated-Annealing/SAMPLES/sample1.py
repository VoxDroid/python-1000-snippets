#!/usr/bin/env python3
"""Simulated annealing minimizing a 2D sphere function."""

import numpy as np


def sphere(x):
    return np.sum(np.asarray(x) ** 2)


def simulated_annealing(f, x0, t0=1.0, cooling=0.99, steps=1000, step_size=0.5):
    x = np.array(x0, dtype=float)
    best = x.copy()
    best_score = f(x)
    t = t0

    for _ in range(steps):
        # Propose a neighbor
        x_new = x + np.random.randn(*x.shape) * step_size
        score_new = f(x_new)
        delta = score_new - f(x)

        if delta < 0 or np.random.rand() < np.exp(-delta / t):
            x = x_new

        if score_new < best_score:
            best = x_new
            best_score = score_new

        t *= cooling

    return best, best_score


def main():
    best, score = simulated_annealing(sphere, x0=[2.0, 2.0])
    print(f"Best solution: {np.round(best, 2)}, fitness: {score:.4f}")


if __name__ == '__main__':
    main()
