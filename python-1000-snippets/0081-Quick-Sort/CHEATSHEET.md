# 0081-Quick-Sort Cheatsheet

- Quick sort divides list using a pivot and recursively sorts partitions.
- Basic recursive (not in-place) version:
  ```python
  def quick_sort(arr):
      if len(arr) <= 1:
          return arr
      pivot = arr[len(arr)//2]
      left = [x for x in arr if x < pivot]
      middle = [x for x in arr if x == pivot]
      right = [x for x in arr if x > pivot]
      return quick_sort(left) + middle + quick_sort(right)
  ```
- Worst-case O(n²) occurs when pivot choices are poor (e.g. sorted input with first/last pivot). Randomizing pivot helps.
- In-place version uses Lomuto or Hoare partition scheme and swaps elements within array.
- Average time O(n log n); space O(log n) auxiliary for recursion.
- Suitable for large arrays; underlying C `sort` uses hybrid algorithms.
