# 0077-Bubble-Sort Cheatsheet

- Bubble sort repeatedly steps through list, compares adjacent items, and swaps them if out of order.
- Basic implementation:
  ```python
  def bubble_sort(arr):
      n = len(arr)
      for i in range(n):
          for j in range(0, n-i-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
      return arr
  ```
- **Optimization**: track if any swap occurred; if none, break early.
- Complexity: best/average/worst O(n²); space O(1).
- Useful for teaching; avoid in real code – use built‑in sort.
