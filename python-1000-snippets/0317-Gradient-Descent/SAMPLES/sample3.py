#!/usr/bin/env python3
"""Gradient descent with numerical gradient estimation for a multimodal 1D function."""

import numpy as np


def multimodal(x):
    x = float(np.asarray(x).ravel()[0])
    return x * np.sin(x) + 0.1 * x**2


def numerical_gradient(f, x, eps=1e-5):
    x0 = float(np.asarray(x).ravel()[0])
    return (f([x0 + eps]) - f([x0 - eps])) / (2 * eps)


def gradient_descent(f, x0, lr=0.1, iterations=200):
    x = np.array([x0], dtype=float)
    for _ in range(iterations):
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return x, f(x)


def main():
    best, loss = gradient_descent(multimodal, x0=2.0)
    print(f"Best solution: {np.round(best, 2)}, loss: {loss:.2f}")


if __name__ == '__main__':
    main()
