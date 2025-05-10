# Selection Sort

## Description
This snippet implements the selection sort algorithm, which repeatedly selects the smallest element from the unsorted portion and places it at the beginning.

## Code
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

numbers = [64, 34, 25, 12, 22]
print("Sorted:", selection_sort(numbers))
```

## Output
```
Sorted: [12, 22, 25, 34, 64]
```

## Explanation
- **Selection Sort**: Finds the minimum element in the unsorted portion and swaps it with the first unsorted element.
- **Complexity**: O(n²) time, O(1) space.
- **Use Case**: Simple sorting for small lists; useful when swapping is expensive.
- **Best Practice**: Prefer built-in sorting for efficiency; use selection sort for educational purposes.