# 0080-Merge-Sort Cheatsheet

- Merge sort splits list into halves until single-element lists remain, then merges them back sorted.
- Recursive implementation uses helper `merge(left, right)` function.
- Bottom-up (iterative) version merges sublists of increasing size.
- Stable sort: equal elements maintain input order.
- Time complexity: O(n log n); space O(n).
- Suitable for sorting linked lists or external sorting when data doesn’t fit memory.

## Basic use
```python
sorted_list = merge_sort(my_list)
```

## Bottom-up example
```python
# see sample3.py
```