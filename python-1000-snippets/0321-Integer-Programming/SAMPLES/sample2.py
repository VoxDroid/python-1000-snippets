#!/usr/bin/env python3
"""Branch-and-bound for a small integer linear program."""

import numpy as np


def is_feasible(x, A, b):
    return np.all(A @ x <= b) and np.all(x >= 0)


def objective(x, c):
    return c @ x


def branch_and_bound(c, A, b, bounds, best=None, best_val=-np.inf):
    # Recursive branch-and-bound for small integer LP.
    if best is None:
        best = np.zeros_like(c, dtype=int)

    # Choose a variable to branch on
    for i in range(len(c)):
        if not np.isclose(bounds[i][0], bounds[i][1]):
            break
    else:
        x = np.array([int(lb) for lb, ub in bounds])
        if is_feasible(x, A, b):
            val = objective(x, c)
            if val > best_val:
                return x, val
        return best, best_val

    lb, ub = bounds[i]
    for val in range(int(lb), int(ub) + 1):
        new_bounds = list(bounds)
        new_bounds[i] = (val, val)
        x, best_val = branch_and_bound(c, A, b, new_bounds, best, best_val)
        best = x
    return best, best_val


def main():
    c = np.array([3.0, 2.0, 4.0])
    A = np.array([[2.0, 1.0, 0.0], [0.0, 2.0, 3.0]])
    b = np.array([4.0, 6.0])
    bounds = [(0, 3), (0, 3), (0, 3)]

    best, best_val = branch_and_bound(c, A, b, bounds)
    print(f"Best solution: {best}, value: {best_val}")


if __name__ == '__main__':
    main()
