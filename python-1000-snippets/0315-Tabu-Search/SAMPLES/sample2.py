#!/usr/bin/env python3
"""Tabu Search optimizing a shifted quadratic function."""

import numpy as np


def shifted_quadratic(x):
    x = np.asarray(x)
    return (x[0] - 1) ** 2 + (x[1] + 2) ** 2


def neighbors(x, step=0.4, num=25):
    return [x + np.random.randn(*x.shape) * step for _ in range(num)]


def tabu_search(f, x0, iterations=250, tabu_size=80):
    x = np.array(x0, dtype=float)
    best = x.copy()
    best_score = f(x)

    tabu = set()
    tabu.add(tuple(np.round(x, 4)))

    for _ in range(iterations):
        cand = neighbors(x)
        cand = [c for c in cand if tuple(np.round(c, 4)) not in tabu]
        if not cand:
            break
        scores = [f(c) for c in cand]
        idx = int(np.argmin(scores))
        x = cand[idx]
        score = scores[idx]

        tabu.add(tuple(np.round(x, 4)))
        if len(tabu) > tabu_size:
            tabu.pop()

        if score < best_score:
            best = x.copy()
            best_score = score

    return best, best_score


def main():
    best, score = tabu_search(shifted_quadratic, x0=[0.0, 0.0])
    print(f"Best solution: {np.round(best, 2)}, fitness: {score:.4f}")


if __name__ == '__main__':
    main()
