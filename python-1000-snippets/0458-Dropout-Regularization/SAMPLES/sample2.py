# sample2.py
# Show that expected value is preserved by scaling during dropout.

import numpy as np


def dropout(x, p=0.5, seed=0):
    rng = np.random.default_rng(seed)
    mask = rng.random(x.shape) >= p
    return x * mask / (1 - p)


def main() -> None:
    x = np.ones((1000,))
    out = dropout(x, p=0.3)

    print("Mean before dropout:", x.mean())
    print("Mean after dropout:", out.mean())
    print("Fraction of nonzero after dropout:", (out != 0).mean())


if __name__ == "__main__":
    main()
