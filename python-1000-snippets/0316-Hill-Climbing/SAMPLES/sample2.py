#!/usr/bin/env python3
"""Hill climbing optimizing a shifted quadratic function."""

import numpy as np


def shifted_quadratic(x):
    x = np.asarray(x)
    return (x[0] - 1) ** 2 + (x[1] + 2) ** 2


def neighbors(x, step=0.2, num=40):
    return [x + np.random.randn(*x.shape) * step for _ in range(num)]


def hill_climb(f, x0, iterations=300):
    x = np.array(x0, dtype=float)
    best = x.copy()
    best_score = f(x)

    for _ in range(iterations):
        cand = neighbors(x)
        scores = [f(c) for c in cand]
        idx = int(np.argmin(scores))
        if scores[idx] < best_score:
            best = cand[idx].copy()
            best_score = scores[idx]
            x = best
        else:
            break

    return best, best_score


def main():
    best, score = hill_climb(shifted_quadratic, x0=[0.0, 0.0])
    print(f"Best solution: {np.round(best, 2)}, fitness: {score:.4f}")


if __name__ == '__main__':
    main()
