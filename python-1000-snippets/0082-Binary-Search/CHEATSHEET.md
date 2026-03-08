# 0082-Binary-Search Cheatsheet

- Binary search operates on a sorted sequence.
- Iterative version:
  ```python
  def binary_search(arr, target):
      left, right = 0, len(arr)-1
      while left <= right:
          mid = (left+right)//2
          if arr[mid] == target: return mid
          elif arr[mid] < target: left = mid+1
          else: right = mid-1
      return -1
  ```
- Recursive version similar but uses function calls.
- Use `bisect` module for insertion points:
  ```python
  import bisect
  idx = bisect.bisect_left(arr, x)
  ```
- O(log n) time, constant space.
- Useful for lookups in sorted lists, arrays, or index structures.
