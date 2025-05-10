# Longest Common Subsequence

## Description
This snippet finds the length of the longest common subsequence (LCS) between two strings using dynamic programming.

## Code
```python
def lcs(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

str1 = "ABCDGH"
str2 = "AEDFHR"
print("LCS Length:", lcs(str1, str2))
```

## Output
```
LCS Length: 3
```

## Explanation
- **LCS**: Finds the longest sequence of characters common to both strings (not necessarily contiguous).
- **DP**: `dp[i][j]` stores the LCS length for prefixes of `str1[:i]` and `str2[:j]`.
- **Complexity**: O(m * n) time, O(m * n) space.
- **Use Case**: Used in diff tools, bioinformatics, or text comparison.
- **Best Practice**: Reconstruct the actual subsequence if needed; optimize space with a 1D array.