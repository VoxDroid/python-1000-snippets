# Tuple Creation

## Description
This snippet demonstrates Python tuples, which are ordered, immutable collections used to store multiple items. It shows how to create and access tuple elements.

## Code
```python
coordinates = (10, 20)
x, y = coordinates
print("Tuple:", coordinates)
print("X coordinate:", x)
print("Y coordinate:", y)
```

## Output
```
Tuple: (10, 20)
X coordinate: 10
Y coordinate: 20
```

## Explanation
- **Tuple Creation**: Tuples are defined using parentheses `()`, with items separated by commas. `coordinates` is a tuple of integers.
- **Immutability**: Tuples cannot be modified after creation (no appending or changing elements).
- **Unpacking**: `x, y = coordinates` assigns tuple elements to individual variables, a common Python idiom.
- **Accessing Elements**: Tuple elements can be accessed via indexing (e.g., `coordinates[0]`), but this snippet uses unpacking for clarity.
- **Use Case**: Tuples are used for fixed collections, like coordinates, database records, or function return values.
- **Performance**: Tuples are slightly faster than lists and use less memory, making them ideal for immutable data.
- **Best Practice**: Use tuples for data that shouldn't change and lists for data that may need modification.