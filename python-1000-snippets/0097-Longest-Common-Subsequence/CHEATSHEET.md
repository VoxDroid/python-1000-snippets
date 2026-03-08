# 0097-Longest-Common-Subsequence Cheatsheet

- LCS length computed by DP table `dp[i][j]` for prefixes of two strings.
- Recurrence:
  ```python
  if a[i-1]==b[j-1]:
      dp[i][j]=dp[i-1][j-1]+1
  else:
      dp[i][j]=max(dp[i-1][j], dp[i][j-1])
  ```
- To reconstruct sequence, backtrack from `dp[m][n]`:
  ```python
  i,j=m,n; seq=[]
  while i>0 and j>0:
      if a[i-1]==b[j-1]:
          seq.append(a[i-1]); i-=1; j-=1
      elif dp[i-1][j] > dp[i][j-1]: i-=1
      else: j-=1
  seq.reverse()
  ```
- Space can be optimized to O(min(m,n)) for length only by computing row by row.
- Applications: diff utilities, sequence alignment, version control, text analysis.
