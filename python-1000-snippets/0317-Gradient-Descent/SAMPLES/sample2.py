#!/usr/bin/env python3
"""Gradient descent on a shifted quadratic function."""

import numpy as np


def shifted_quadratic(x):
    return (x[0] - 1) ** 2 + (x[1] + 2) ** 2


def grad_shifted_quadratic(x):
    return np.array([2 * (x[0] - 1), 2 * (x[1] + 2)])


def gradient_descent(grad_fn, x0, lr=0.1, iterations=120):
    x = np.array(x0, dtype=float)
    for _ in range(iterations):
        x -= lr * grad_fn(x)
    return x, shifted_quadratic(x)


def main():
    best, loss = gradient_descent(grad_shifted_quadratic, x0=[0.0, 0.0])
    print(f"Best solution: {np.round(best, 2)}, loss: {loss:.4f}")


if __name__ == '__main__':
    main()
