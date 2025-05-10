# Merge Sort

## Description
This snippet implements the merge sort algorithm, a divide-and-conquer method that splits a list, sorts sublists, and merges them.

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

numbers = [64, 34, 25, 12, 22]
print("Sorted:", merge_sort(numbers))
```

## Output
```
Sorted: [12, 22, 25, 34, 64]
```

## Explanation
- **Merge Sort**: Recursively divides the list into halves, sorts them, and merges sorted halves.
- **Merge**: Combines two sorted lists by comparing elements.
- **Complexity**: O(n log n) time, O(n) space.
- **Use Case**: Efficient for large datasets, especially linked lists or stable sorting.
- **Best Practice**: Use for stable sorting; Python’s `sorted()` uses a hybrid algorithm (Timsort) for general use.