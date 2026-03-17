"""Solve 0/1 Knapsack using dynamic programming."""

from typing import List, Tuple


def knapsack(values: List[int], weights: List[int], capacity: int) -> Tuple[int, List[int]]:
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # backtrack to find selected items
    result = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], list(reversed(result))


if __name__ == "__main__":
    values = [6, 10, 12]
    weights = [1, 2, 3]
    capacity = 5

    max_value, items = knapsack(values, weights, capacity)
    print("Values:", values)
    print("Weights:", weights)
    print("Capacity:", capacity)
    print("Max value:", max_value)
    print("Selected item indices:", items)
