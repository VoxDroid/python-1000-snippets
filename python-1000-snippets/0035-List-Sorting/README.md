# List Sorting

## Description
This snippet shows how to sort a list in Python using the `sort()` method and `sorted()` function, including ascending and descending order.

## Code
```python
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print("Sorted (ascending):", numbers)
numbers.sort(reverse=True)
print("Sorted (descending):", numbers)
sorted_numbers = sorted([5, 2, 8, 1, 9])
print("Sorted with sorted():", sorted_numbers)
```

## Output
```
Sorted (ascending): [1, 2, 5, 8, 9]
Sorted (descending): [9, 8, 5, 2, 1]
Sorted with sorted(): [1, 2, 5, 8, 9]
```

## Explanation
- **sort() Method**: Modifies the list in place. `reverse=True` sorts in descending order.
- **sorted() Function**: Returns a new sorted list, leaving the original unchanged.
- **Use Case**: Sorting is used in data processing, user interfaces, or ranking algorithms.
- **Flexibility**: Both methods support custom sorting with `key` functions (e.g., `key=len` for strings).
- **Best Practice**: Use `sorted()` when preserving the original list is needed.