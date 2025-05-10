# Quick Sort

## Description
This snippet implements the quick sort algorithm, a divide-and-conquer method that picks a pivot and partitions the list around it.

## Code
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

numbers = [64, 34, 25, 12, 22]
print("Sorted:", quick_sort(numbers))
```

## Output
```
Sorted: [12, 22, 25, 34, 64]
```

## Explanation
- **Quick Sort**: Selects a pivot (here, middle element), partitions into smaller, equal, and larger elements, and recursively sorts.
- **Complexity**: Average O(n log n) time, O(n) space (due to list creation); in-place versions use O(log n) space.
- **Use Case**: Fast for large datasets; used in many standard library sorts.
- **Best Practice**: Use in-place partitioning for memory efficiency; Python’s `sorted()` is preferred for general use.