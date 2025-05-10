# Insertion Sort

## Description
This snippet implements the insertion sort algorithm, which builds a sorted array by inserting each element into its correct position.

## Code
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

numbers = [64, 34, 25, 12, 22]
print("Sorted:", insertion_sort(numbers))
```

## Output
```
Sorted: [12, 22, 25, 34, 64]
```

## Explanation
- **Insertion Sort**: Takes each element and inserts it into the sorted portion of the list by shifting larger elements.
- **Complexity**: O(n²) time, O(1) space; efficient for small or nearly sorted lists.
- **Use Case**: Sorting small datasets or online sorting where data arrives incrementally.
- **Best Practice**: Use for small lists; Python’s `sorted()` is better for general use.