# sample2.py
# Compute a forward pass for a simple network without external libraries.

from __future__ import annotations


def relu(x):
    return [max(0.0, v) for v in x]


def matmul(weights, vec):
    return [sum(w * v for w, v in zip(row, vec)) for row in weights]


def add_bias(vec, bias):
    return [v + b for v, b in zip(vec, bias)]


def forward(x):
    w1 = [[0.1, -0.2, 0.3], [0.4, 0.5, -0.6], [-0.1, 0.2, 0.1], [0.3, -0.3, 0.2], [0.2, 0.1, -0.1]]
    b1 = [0.1, -0.1, 0.05, 0.0, -0.05]
    w2 = [[0.2, -0.4, 0.1, 0.3, -0.2], [-0.3, 0.2, 0.4, -0.1, 0.6]]
    b2 = [0.0, 0.05]

    h1 = relu(add_bias(matmul(w1, x), b1))
    out = add_bias(matmul(w2, h1), b2)
    return out


def main() -> None:
    x = [1.0, 0.5, -0.5]
    y = forward(x)
    print("Input:", x)
    print("Output:", [round(v, 4) for v in y])


if __name__ == '__main__':
    main()
