# sample3.py
# Compute a DTW-based average (centroid) of multiple sequences.

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


def dtw_centroid(series: list[np.ndarray], iterations: int = 3) -> np.ndarray:
    # Start with the first series
    centroid = series[0].copy()
    for _ in range(iterations):
        # Align all series to centroid by finding best matching points
        aligned = []
        for s in series:
            # Simple up/down sampling to same length
            idx = np.linspace(0, len(s) - 1, len(centroid)).astype(int)
            aligned.append(s[idx])
        centroid = np.mean(aligned, axis=0)
    return centroid


def main() -> None:
    rng = np.random.RandomState(2)
    base = np.sin(np.linspace(0, 2 * np.pi, 80))
    series = [base + 0.1 * rng.randn(len(base)) for _ in range(5)]

    centroid = dtw_centroid(series)

    print("Centroid length:", len(centroid))
    print("Centroid sample:", np.round(centroid[:5], 3).tolist())


if __name__ == "__main__":
    main()
