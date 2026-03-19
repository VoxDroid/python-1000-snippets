# sample3.py
# Simulate dropout during training and inference (inference uses no dropout).

import numpy as np


def dropout(x, p=0.5, seed=0, training=True):
    if not training:
        return x
    rng = np.random.default_rng(seed)
    mask = rng.random(x.shape) >= p
    return x * mask / (1 - p)


def main() -> None:
    x = np.arange(1, 6, dtype=float)

    print("Training output:", dropout(x, p=0.4, seed=0, training=True))
    print("Inference output:", dropout(x, p=0.4, seed=0, training=False))


if __name__ == "__main__":
    main()
