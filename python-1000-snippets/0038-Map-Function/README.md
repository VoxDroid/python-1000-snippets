# Map Function

## Description
This snippet demonstrates the `map()` function in Python, which applies a function to each item in an iterable, returning a map object.

## Code
```python
numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)
print("Squares:", list(squares))
```

## Output
```
Squares: [1, 4, 9, 16]
```

## Explanation
- **Map Function**: `map(function, iterable)` applies `function` to each item in `iterable`.
- **Lambda**: `lambda x: x ** 2` defines the function to square each number.
- **Conversion**: `map()` returns a map object, converted to a list for printing.
- **Use Case**: `map()` is used for transforming data, like scaling values or formatting strings.
- **Best Practice**: Use `map()` for functional programming; consider list comprehension for readability.