# Binary Search

## Description
This snippet implements binary search to find an element in a sorted list by repeatedly dividing the search interval in half.

## Code
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

numbers = [12, 22, 25, 34, 64]
target = 25
index = binary_search(numbers, target)
print(f"Index of {target}: {index}")
```

## Output
```
Index of 25: 2
```

## Explanation
- **Binary Search**: Efficiently searches a sorted list by checking the middle element and narrowing the search range.
- **Complexity**: O(log n) time, O(1) space.
- **Requirement**: The input list must be sorted.
- **Use Case**: Used in databases, search engines, or any sorted data lookup.
- **Best Practice**: Ensure the list is sorted; use Python’s `bisect` module for production.