# 0096-Knapsack-Problem Cheatsheet

- The 0/1 knapsack problem chooses items with values and weights to maximize total value under a weight limit.
- Standard DP uses table `dp[i][w]` with `i` items and capacity `w`:
  ```python
  for i in range(1,n+1):
      for w in range(cap+1):
          if wt[i-1] <= w:
              dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]]+val[i-1])
          else:
              dp[i][w] = dp[i-1][w]
  ```
- Space-optimized version uses 1D array iterating weights backwards.
- To reconstruct chosen items, backtrack through table starting at `dp[n][cap]`.
- Complexity O(n * capacity); space can be reduced to O(capacity).
- Useful in budgeting, resource allocation, subset selection.
