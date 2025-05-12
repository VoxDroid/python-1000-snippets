# Nested Dictionary Processing

## Description
This snippet demonstrates processing a nested dictionary to extract values.

## Code
```python
data = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}}
x_values = [inner["x"] for inner in data.values()]
print("X Values:", x_values)
```

## Output
```
X Values: [1, 3]
```

## Explanation
- **Nested Dictionary Processing**: Extracts "x" values from nested dictionaries.
- **Logic**: Uses a list comprehension to access inner dictionary values.
- **Complexity**: O(n) for n top-level keys.
- **Use Case**: Used for parsing structured data like JSON.
- **Best Practice**: Handle missing keys; validate structure; use recursion for deeper nesting.