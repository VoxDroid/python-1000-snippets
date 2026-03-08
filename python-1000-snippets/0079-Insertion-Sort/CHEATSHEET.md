# 0079-Insertion-Sort Cheatsheet

- Insertion sort builds the sorted array one element at a time, inserting each new element into the correct position by shifting neighbors.
- Pseudocode:
  ```python
  for i in range(1, len(arr)):
      key = arr[i]
      j = i - 1
      while j >= 0 and arr[j] > key:
          arr[j+1] = arr[j]
          j -= 1
      arr[j+1] = key
  ```
- Stable: equal elements preserve order.
- Best on nearly sorted lists (O(n + d) where d distance elements move).
- Online algorithm: can sort as data arrives.
- To sort descending, invert comparison (`<`).
