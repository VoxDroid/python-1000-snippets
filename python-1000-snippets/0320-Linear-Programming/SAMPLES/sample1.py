#!/usr/bin/env python3
"""Simple simplex solver for a small LP problem."""

import numpy as np


def simplex(c, A, b):
    # Simple implementation for small problems (maximize c^T x, Ax <= b, x >= 0)
    m, n = A.shape
    # Build initial tableau
    T = np.zeros((m + 1, n + m + 1))
    T[:m, :n] = A
    T[:m, n : n + m] = np.eye(m)
    T[:m, -1] = b
    T[-1, :n] = -c

    basis = list(range(n, n + m))

    while True:
        # entering variable (most negative in objective row)
        col = np.argmin(T[-1, :-1])
        if T[-1, col] >= 0:
            break

        ratios = []
        for i in range(m):
            if T[i, col] > 1e-9:
                ratios.append(T[i, -1] / T[i, col])
            else:
                ratios.append(np.inf)

        row = int(np.argmin(ratios))
        if ratios[row] == np.inf:
            raise ValueError("Unbounded")

        pivot = T[row, col]
        T[row, :] /= pivot
        for i in range(m + 1):
            if i != row:
                T[i, :] -= T[i, col] * T[row, :]

        basis[row] = col

    x = np.zeros(n)
    for i, bi in enumerate(basis):
        if bi < n:
            x[bi] = T[i, -1]

    return x, T[-1, -1]


def main():
    c = np.array([1.0, 1.0])
    A = np.array([[1.0, 2.0], [2.0, 1.0]])
    b = np.array([4.0, 4.0])

    x, obj = simplex(c, A, b)
    print(f"Solution: x={x[0]:.2f}, y={x[1]:.2f}, objective={obj:.2f}")


if __name__ == '__main__':
    main()
