# 0107-Statistics-Calculation Cheatsheet

- Basic summary statistics: mean, median, variance, standard deviation.
- Python’s built-in `statistics` module provides `mean`, `median`, `variance`, `stdev`.
- For median, sort data; for large data use `heapq.nsmallest` to reduce overhead.
- Variance population vs sample: divide by `n` or `n-1` respectively.
- Use NumPy (`np.mean`, `np.median`, `np.var`) for vectorized computation.
- Handle empty data by raising `ValueError` or returning `None`.
