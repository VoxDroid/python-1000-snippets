#!/usr/bin/env python3
"""Newton method to find sqrt(2) by solving x^2 - 2 = 0."""


def newton_root(f, df, x0, iterations=10):
    x = x0
    for _ in range(iterations):
        x -= f(x) / df(x)
    return x


def main():
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x

    root = newton_root(f, df, x0=2.0, iterations=10)
    print(f"Root (sqrt2): {root:.11f}")


if __name__ == '__main__':
    main()
