# Edit Distance

## Description
This snippet computes the edit distance (Levenshtein distance) between two strings, the minimum number of operations (insert, delete, replace) to transform one into the other.

## Code
```python
def edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1] + 1,  # replace
                               dp[i-1][j] + 1,    # delete
                               dp[i][j-1] + 1)    # insert
    
    return dp[m][n]

str1 = "kitten"
str2 = "sitting"
print("Edit Distance:", edit_distance(str1, str2))
```

## Output
```
Edit Distance: 3
```

## Explanation
- **Edit Distance**: Measures the minimum operations to convert `str1` to `str2`.
- **DP**: `dp[i][j]` is the edit distance for prefixes `str1[:i]` and `str2[:j]`.
- **Complexity**: O(m * n) time, O(m * n) space.
- **Use Case**: Used in spell checkers, DNA sequence alignment, or natural language processing.
- **Best Practice**: Optimize space with a 1D array; trace operations for edit sequence.