# Divide and Conquer

## Description
This snippet demonstrates divide and conquer with merge sort.

## Code
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("Sorted:", merge_sort([3, 1, 4, 1, 5]))
```

## Output
```
Sorted: [1, 1, 3, 4, 5]
```

## Explanation
- **Divide and Conquer**: Sorts an array by dividing and merging.
- **Logic**: Recursively splits array, merges sorted halves.
- **Complexity**: O(n log n) for n elements.
- **Use Case**: Used for sorting, FFT, or matrix multiplication.
- **Best Practice**: Optimize merge; handle large arrays; validate inputs.