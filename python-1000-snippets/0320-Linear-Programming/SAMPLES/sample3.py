#!/usr/bin/env python3
"""Linear programming with both equality and inequality constraints."""

import numpy as np


def simplex(c, A, b):
    m, n = A.shape
    T = np.zeros((m + 1, n + m + 1))
    T[:m, :n] = A
    T[:m, n:n+m] = np.eye(m)
    T[:m, -1] = b
    T[-1, :n] = -c

    basis = list(range(n, n + m))

    while True:
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
    # Maximize x + 2y subject to x + y <= 4, x + 3y <= 6
    c = np.array([1.0, 2.0])
    A = np.array([[1.0, 1.0], [1.0, 3.0]])
    b = np.array([4.0, 6.0])

    x, obj = simplex(c, A, b)
    print(f"Solution: x={x[0]:.2f}, y={x[1]:.2f}, objective={obj:.2f}")


if __name__ == '__main__':
    main()
