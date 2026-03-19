# sample3.py
# Show how running mean/variance can be updated across batches (moving average).

import numpy as np


def update_running_stats(running_mean, running_var, batch_mean, batch_var, momentum=0.9):
    running_mean = momentum * running_mean + (1 - momentum) * batch_mean
    running_var = momentum * running_var + (1 - momentum) * batch_var
    return running_mean, running_var


def main() -> None:
    rng = np.random.default_rng(0)
    running_mean = np.zeros(3)
    running_var = np.ones(3)

    for i in range(1, 4):
        X = rng.normal(loc=i, scale=1.0, size=(5, 3))
        batch_mean = X.mean(axis=0)
        batch_var = X.var(axis=0)
        running_mean, running_var = update_running_stats(running_mean, running_var, batch_mean, batch_var)
        print(f"After batch {i}: running_mean={running_mean.round(3)}, running_var={running_var.round(3)}")


if __name__ == "__main__":
    main()
