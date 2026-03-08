# List Creation Cheatsheet

## Creating lists
```python
empty = []
numbers = [1, 2, 3]
mixed = [1, "two", 3.0]
```

## Common methods
- `append()`, `extend()`, `insert()`
- `remove()`, `pop()`, `clear()`
- `sort()`, `reverse()`

## Accessing elements
```python
lst[0]        # first element
lst[-1]       # last element
lst[1:4]      # slicing
```

## List comprehensions
```python
squares = [x*x for x in range(10)]
even = [x for x in numbers if x % 2 == 0]
```

## Tips
- Slicing returns a new list.
- Use `len()` to get length.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

