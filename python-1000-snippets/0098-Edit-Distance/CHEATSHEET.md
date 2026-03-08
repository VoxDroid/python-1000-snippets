# 0098-Edit-Distance Cheatsheet

- The Levenshtein distance counts minimum insert/delete/replace operations.
- DP relation:
  ```python
  if a[i-1]==b[j-1]: dp[i][j]=dp[i-1][j-1]
  else: dp[i][j]=1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
  ```
- Initialization: `dp[i][0]=i`, `dp[0][j]=j`.
- Space can be reduced to two rows or one row by iterating backwards.
- To get the sequence of edits, backtrack from `dp[m][n]` recording operations.
- Applications: fuzzy string matching, diff tools, bioinformatics.
