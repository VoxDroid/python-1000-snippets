#!/usr/bin/env python3
"""Conjugate gradient on a random symmetric positive-definite system."""

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
    np.random.seed(0)
    n = 4
    M = np.random.randn(n, n)
    A = M.T @ M + np.eye(n) * 1e-3
    b = np.random.randn(n)

    x = conjugate_gradient(A, b)
    print(f"Solution: {np.round(x, 2)}")


if __name__ == '__main__':
    main()
