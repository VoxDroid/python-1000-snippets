# Filter Function

## Description
This snippet shows the `filter()` function in Python, which selects items from an iterable based on a function that returns `True` or `False`.

## Code
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers:", list(evens))
```

## Output
```
Even numbers: [2, 4, 6]
```

## Explanation
- **Filter Function**: `filter(function, iterable)` keeps items where `function` returns `True`.
- **Lambda**: `lambda x: x % 2 == 0` checks if a number is even.
- **Conversion**: `filter()` returns a filter object, converted to a list for printing.
- **Use Case**: `filter()` is used for selecting subsets, like filtering valid data or specific categories.
- **Best Practice**: Use `filter()` for functional programming; list comprehension may be more readable.