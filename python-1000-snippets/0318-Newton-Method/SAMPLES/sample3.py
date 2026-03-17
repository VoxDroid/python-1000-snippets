#!/usr/bin/env python3
"""Use Newton's method to find a stationary point of a 1D function (optimization)."""

import numpy as np


def f(x):
    x = float(np.asarray(x).ravel()[0])
    return x**4 - 3 * x**3 + 2


def grad_f(x):
    x = float(np.asarray(x).ravel()[0])
    return 4 * x**3 - 9 * x**2


def hess_f(x):
    x = float(np.asarray(x).ravel()[0])
    return 12 * x**2 - 18 * x


def newton_optimize(grad, hess, x0, iterations=20):
    x = float(x0)
    for _ in range(iterations):
        g = grad(x)
        h = hess(x)
        if h == 0:
            break
        x -= g / h
    return x


def main():
    x_opt = newton_optimize(grad_f, hess_f, x0=2.0)
    print(f"Optimum x: {x_opt:.2f}, f(x)={f(x_opt):.2f}")


if __name__ == '__main__':
    main()
