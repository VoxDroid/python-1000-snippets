# Knapsack Problem

## Description
This snippet solves the 0/1 knapsack problem using dynamic programming to maximize value within a weight constraint.

## Code
```python
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print("Maximum Value:", knapsack(values, weights, capacity))
```

## Output
```
Maximum Value: 220
```

## Explanation
- **Knapsack**: Selects items to maximize total value without exceeding weight capacity; each item is taken (1) or not (0).
- **DP**: Builds a table where `dp[i][w]` is the maximum value for the first `i` items and weight `w`.
- **Complexity**: O(n * capacity) time, O(n * capacity) space.
- **Use Case**: Used in resource allocation, budgeting, or optimization problems.
- **Best Practice**: Optimize space with a 1D array for large inputs.