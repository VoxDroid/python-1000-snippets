#!/usr/bin/env python3
"""Newton method to find a root of a cubic polynomial."""


def newton_root(f, df, x0, iterations=15):
    x = x0
    for _ in range(iterations):
        x -= f(x) / df(x)
    return x


def main():
    f = lambda x: x**3 - 2 * x - 1
    df = lambda x: 3 * x**2 - 2

    root = newton_root(f, df, x0=1.5, iterations=20)
    print(f"Root (cubic): {root:.4f}")


if __name__ == '__main__':
    main()
