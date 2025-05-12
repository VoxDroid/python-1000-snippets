# Dynamic Programming

## Description
This snippet demonstrates dynamic programming for the Fibonacci sequence.

## Code
```python
def fibonacci(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print("Fibonacci(10):", fibonacci(10))
```

## Output
```
Fibonacci(10): 55
```

## Explanation
- **Dynamic Programming**: Computes Fibonacci numbers efficiently.
- **Logic**: Uses a table to store intermediate results.
- **Complexity**: O(n) for n terms.
- **Use Case**: Used for problems like knapsack or shortest paths.
- **Best Practice**: Optimize space; handle edge cases; validate inputs.