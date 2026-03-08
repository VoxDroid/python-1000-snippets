# Filter Function Cheatsheet

## Basic syntax
```python
filter(func, iterable)
```
- Returns lazy filter object.
- Can cast to list/tuple.

## Tips
- `func` returning bool decides inclusion.
- To filter out `None` or falsey values: `filter(None, iterable)`.
- Equivalent comprehension: `[x for x in iterable if func(x)]`.

## Examples
```python
result = list(filter(lambda x: x>0, nums))
```

## Running samples
Activate venv and execute samples in `SAMPLES/`.
