# 0078-Selection-Sort Cheatsheet

- Selection sort iterates through the list and selects the smallest (or largest) element from the unsorted part, swapping it with the first unsorted element.
- Basic implementation:
  ```python
  def selection_sort(arr):
      n = len(arr)
      for i in range(n):
          min_idx = i
          for j in range(i+1, n):
              if arr[j] < arr[min_idx]:
                  min_idx = j
          arr[i], arr[min_idx] = arr[min_idx], arr[i]
      return arr
  ```
- To sort descending, choose max element instead.
- Selection sort is not stable by default (equal elements may change order).
- Complexity: O(n²) time; few swaps (O(n)).
- Good for small arrays or memory-constrained contexts where writes are expensive.
