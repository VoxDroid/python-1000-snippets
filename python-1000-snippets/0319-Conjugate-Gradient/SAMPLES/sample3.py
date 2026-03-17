#!/usr/bin/env python3
"""Minimize a quadratic function via conjugate gradient (equivalent to solving Ax=b)."""

import numpy as np


def conjugate_gradient(A, b, x0=None, tol=1e-8, max_iter=None):
    n = len(b)
    if x0 is None:
        x = np.zeros_like(b)
    else:
        x = x0.copy()

    r = b - A @ x
    p = r.copy()
    rs_old = np.dot(r, r)

    if max_iter is None:
        max_iter = n

    for _ in range(max_iter):
        Ap = A @ p
        alpha = rs_old / np.dot(p, Ap)
        x += alpha * p
        r -= alpha * Ap
        rs_new = np.dot(r, r)
        if np.sqrt(rs_new) < tol:
            break
        p = r + (rs_new / rs_old) * p
        rs_old = rs_new

    return x


def main():
    A = np.array([[3.0, 1.0], [1.0, 2.0]])
    b = np.array([1.0, 1.0])
    x = conjugate_gradient(A, b)
    f = 0.5 * x @ (A @ x) - x @ b
    print(f"Minimum x: {np.round(x, 2)}, f(x)={f:.2f}")


if __name__ == '__main__':
    main()
