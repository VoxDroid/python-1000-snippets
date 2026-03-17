# 0323-Dynamic-Programming Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Fibonacci with memoization
python SAMPLES/sample2.py  # Longest increasing subsequence
python SAMPLES/sample3.py  # 0/1 Knapsack problem
```

## Tips
- Use a table (list/dict) to store results of subproblems.
- Choose between memoization (recursive with cache) and tabulation (iterative table building).
- Identify overlapping subproblems and optimal substructure.

## Example patterns
- Fibonacci: `dp[n] = dp[n-1] + dp[n-2]`
- Knapsack: `dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])`
- LIS: `dp[i] = 1 + max(dp[j] for j < i and arr[j] < arr[i])`
