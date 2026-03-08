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

## Additional Files
- `CHEATSHEET.md` with map tips and comparison to comprehension.
- `SAMPLES/` contains:
  1. `sample1.py` – basic map with lambda.
  2. `sample2.py` – map with a named function over strings.
  3. `sample3.py` – chaining map and filter.

Test these under a `.venv`.