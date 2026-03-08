# 0083-Linear-Search Cheatsheet

- Iterate through list and compare each element.
- Simple implementation:
  ```python
  def linear_search(arr, target):
      for i, v in enumerate(arr):
          if v == target:
              return i
      return -1
  ```
- Works on unsorted data and for any iterable.
- Use Python’s `in` operator (`if target in arr:`) for membership tests.
- Time complexity O(n); best when target is near beginning.
