#!/usr/bin/env python3
"""Gradient descent on a 2D quadratic function with analytic gradient."""

import numpy as np


def quadratic(x):
    return x[0] ** 2 + x[1] ** 2


def grad_quadratic(x):
    return np.array([2 * x[0], 2 * x[1]])


def gradient_descent(grad_fn, x0, lr=0.1, iterations=100):
    x = np.array(x0, dtype=float)
    for _ in range(iterations):
        x -= lr * grad_fn(x)
    return x, quadratic(x)


def main():
    best, loss = gradient_descent(grad_quadratic, x0=[2.0, 2.0])
    print(f"Best solution: {np.round(best, 2)}, loss: {loss:.4f}")


if __name__ == '__main__':
    main()
