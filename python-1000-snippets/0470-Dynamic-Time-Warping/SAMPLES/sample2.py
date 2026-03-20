# sample2.py
# Use DTW distance to classify time series against template patterns.

import numpy as np


def dtw_distance(a: np.ndarray, b: np.ndarray) -> float:
    n, m = len(a), len(b)
    dp = np.full((n + 1, m + 1), np.inf)
    dp[0, 0] = 0.0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(a[i - 1] - b[j - 1])
            dp[i, j] = cost + min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1])

    return dp[n, m]


def main() -> None:
    rng = np.random.RandomState(0)
    templates = {
        "sine": np.sin(np.linspace(0, 2 * np.pi, 50)),
        "square": np.sign(np.sin(np.linspace(0, 2 * np.pi, 50))),
    }

    # Create a noisy sine-like series to classify.
    query = np.sin(np.linspace(0, 2 * np.pi, 60)) + 0.1 * rng.randn(60)

    best_label = None
    best_dist = float('inf')
    for label, template in templates.items():
        dist = dtw_distance(query, template)
        print(f"DTW distance to {label}: {dist:.3f}")
        if dist < best_dist:
            best_dist = dist
            best_label = label

    print("Predicted label:", best_label)


if __name__ == "__main__":
    main()
