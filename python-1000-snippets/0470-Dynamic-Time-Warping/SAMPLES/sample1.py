# sample1.py
# Compute DTW distance between two time series and demonstrate the warping path.

import numpy as np


def dtw_distance(x: np.ndarray, y: np.ndarray):
    n, m = len(x), len(y)
    dp = np.full((n + 1, m + 1), np.inf)
    dp[0, 0] = 0.0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = abs(x[i - 1] - y[j - 1])
            dp[i, j] = cost + min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1])

    return dp[n, m], dp


def warping_path(dp: np.ndarray):
    i, j = np.array(dp.shape) - 1
    path = []
    while i > 0 or j > 0:
        path.append((i - 1, j - 1))
        moves = [(i - 1, j), (i, j - 1), (i - 1, j - 1)]
        costs = [dp[a, b] for a, b in moves]
        k = int(np.argmin(costs))
        i, j = moves[k]
    return list(reversed(path))


def main() -> None:
    x = np.array([1, 2, 2, 3, 2, 1], dtype=float)
    y = np.array([0, 1, 2, 2, 3, 2, 1], dtype=float)

    distance, dp = dtw_distance(x, y)
    path = warping_path(dp)

    print("DTW distance:", distance)
    print("Warping path (first 10):", path[:10])
    print("Aligned pairs (first 5):")
    for i, j in path[:5]:
        print(f"  x[{i}]={x[i]} vs y[{j}]={y[j]}")


if __name__ == "__main__":
    main()
