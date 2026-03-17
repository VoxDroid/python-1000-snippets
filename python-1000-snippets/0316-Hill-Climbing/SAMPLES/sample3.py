#!/usr/bin/env python3
"""Hill climbing on a multimodal 1D function."""

import numpy as np


def multimodal(x):
    x = float(np.asarray(x).ravel()[0])
    return x * np.sin(x) + 0.1 * x**2


def neighbors(x, step=0.4, num=40):
    x = float(np.asarray(x).ravel()[0])
    return [np.array([x + np.random.randn() * step]) for _ in range(num)]


def hill_climb(f, x0, iterations=300):
    x = np.array([x0], dtype=float)
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
    best, score = hill_climb(multimodal, x0=2.0)
    print(f"Best solution: {np.round(best, 2)}, fitness: {score:.2f}")


if __name__ == '__main__':
    main()
