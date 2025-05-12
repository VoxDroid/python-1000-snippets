# Tuple Manipulation

## Description
This snippet demonstrates tuple manipulation to extract and transform elements.

## Code
```python
data = [(1, "a"), (2, "b")]
numbers = [t[0] for t in data]
print("Numbers:", numbers)
```

## Output
```
Numbers: [1, 2]
```

## Explanation
- **Tuple Manipulation**: Extracts first elements from a list of tuples.
- **Logic**: Uses a list comprehension to access tuple indices.
- **Complexity**: O(n) for n tuples.
- **Use Case**: Used for structured data processing.
- **Best Practice**: Validate tuple structure; handle empty lists; use unpacking.