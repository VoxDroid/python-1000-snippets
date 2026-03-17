#!/usr/bin/env python3
"""Tabu Search for a multimodal 1D objective function."""

import numpy as np


def multimodal(x):
    x = float(np.asarray(x).ravel()[0])
    return x * np.sin(x) + 0.1 * x**2


def neighbors(x, step=0.5, num=30):
    x = np.asarray(x).ravel()[0]
    return [np.array([x + np.random.randn() * step]) for _ in range(num)]


def tabu_search(f, x0, iterations=300, tabu_size=60):
    x = np.array([x0], dtype=float)
    best = x.copy()
    best_score = f(x)

    tabu = set()
    tabu.add(float(np.round(x.item(), 4)))

    for _ in range(iterations):
        cand = neighbors(x)
        cand = [c for c in cand if float(np.round(c.item(), 4)) not in tabu]
        if not cand:
            break
        scores = [f(c) for c in cand]
        idx = int(np.argmin(scores))
        x = cand[idx]
        score = scores[idx]

        tabu.add(float(np.round(x.item(), 4)))
        if len(tabu) > tabu_size:
            tabu.pop()

        if score < best_score:
            best = x.copy()
            best_score = score

    return best, best_score


def main():
    best, score = tabu_search(multimodal, x0=2.0)
    print(f"Best solution: {np.round(best, 2)}, fitness: {score:.2f}")


if __name__ == '__main__':
    main()
