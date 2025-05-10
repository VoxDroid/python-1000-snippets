# Linear Search

## Description
This snippet implements linear search to find an element in a list by checking each element sequentially.

## Code
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [64, 34, 25, 12, 22]
target = 25
index = linear_search(numbers, target)
print(f"Index of {target}: {index}")
```

## Output
```
Index of 25: 2
```

## Explanation
- **Linear Search**: Checks each element until the target is found or the list ends.
- **Complexity**: O(n) time, O(1) space.
- **Use Case**: Suitable for unsorted or small lists; simple to implement.
- **Best Practice**: Use binary search for sorted lists; Python’s `in` operator for simple checks.