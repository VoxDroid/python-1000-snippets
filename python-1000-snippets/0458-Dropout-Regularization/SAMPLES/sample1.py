# sample1.py
# Demonstrate dropout on a vector using a dropout mask.

import numpy as np


def dropout(x, p=0.5, seed=0):
    rng = np.random.default_rng(seed)
    mask = rng.random(x.shape) >= p
    return x * mask / (1 - p), mask


def main() -> None:
    x = np.arange(10, dtype=float)
    out, mask = dropout(x, p=0.3)

    print("Input:", x)
    print("Dropout mask:", mask.astype(int))
    print("Output (scaled):", out)


if __name__ == "__main__":
    main()
