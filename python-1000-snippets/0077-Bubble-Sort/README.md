# Bubble Sort

## Description
This snippet implements the bubble sort algorithm, which repeatedly swaps adjacent elements if they are in the wrong order.

## Code
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22]
print("Sorted:", bubble_sort(numbers))
```

## Output
```
Sorted: [12, 22, 25, 34, 64]
```

## Explanation
- **Bubble Sort**: Compares and swaps adjacent elements, “bubbling” larger values to the end.
- **Complexity**: O(n²) time, O(1) space.
- **Use Case**: Simple sorting for small lists or educational purposes; inefficient for large datasets.
- **Optimization**: Add a flag to exit early if no swaps occur.
- **Best Practice**: Use Python’s `sorted()` or `list.sort()` for production; bubble sort for learning.