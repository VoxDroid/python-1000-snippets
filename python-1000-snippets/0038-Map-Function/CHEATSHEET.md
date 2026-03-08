# Map Function Cheatsheet

## Basic usage
```python
map(func, iterable)
```
- Returns lazy map object.
- Convert to list, tuple, etc. to consume.

## Tips
- `map(str, numbers)` converts numbers to strings.
- Can pass multiple iterables: `map(func, it1, it2)` stops at shortest.
- Equivalent list comprehension: `[func(x) for x in iterable]`.

## Examples
```python
results = list(map(lambda x: x+1, [1,2,3]))
```

## Running samples
Activate venv and run each file in `SAMPLES/`.
