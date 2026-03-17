#!/usr/bin/env python3
"""Evolutionary strategy on a multimodal 1D objective function."""

import numpy as np
import random


def multimodal(x):
    x = float(np.asarray(x).ravel()[0])
    return x * np.sin(x) + 0.1 * x**2


def es_optimize(fitness_fn, dim, mu=30, lam=120, generations=150, sigma=0.5):
    dim = int(dim)
    parents = [np.random.randn(dim) for _ in range(mu)]

    for _ in range(generations):
        offspring = []
        for _ in range(lam):
            parent = random.choice(parents)
            child = parent + np.random.randn(dim) * sigma
            offspring.append(child)

        combined = parents + offspring
        combined.sort(key=fitness_fn)
        parents = combined[:mu]

    best = parents[0]
    return best, fitness_fn(best)


def main():
    best, value = es_optimize(multimodal, dim=1)
    print(f"Best solution: {np.round(best, 2)}, fitness: {value:.2f}")


if __name__ == '__main__':
    main()
