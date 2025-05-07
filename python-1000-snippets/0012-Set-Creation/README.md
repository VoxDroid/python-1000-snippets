# Set Creation

## Description
This snippet shows how to create a set in Python. Sets are unordered, mutable collections of unique elements, useful for removing duplicates or performing mathematical set operations.

## Code
```python
numbers = {1, 2, 2, 3, 4}
print("Set:", numbers)
```

## Output
```
Set: {1, 2, 3, 4}
```

## Explanation
- **Set Creation**: Sets are defined using curly braces `{}`, with elements separated by commas. Duplicates (e.g., `2`) are automatically removed.
- **Uniqueness**: Sets only store unique elements, making them ideal for deduplication.
- **Unordered**: Sets do not maintain insertion order, and elements cannot be accessed by index.
- **Use Case**: Sets are used for tasks like finding unique items, membership testing, or set operations (union, intersection).
- **Best Practice**: Use sets for operations requiring uniqueness or fast membership testing, but avoid if order matters.