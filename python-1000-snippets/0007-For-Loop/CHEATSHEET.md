# For Loop Cheatsheet

## Basic syntax
```python
for item in iterable:
    # code
```

## Common iterables
- `range(start, stop, step)`
- lists, tuples, strings, dictionaries (`for k, v in dict.items():`)

## Useful patterns
- `for i in range(5):` loops 0–4.
- `for idx, val in enumerate(sequence):` gets index and value.
- `for x in reversed(sequence):` iterate backwards.

## Tips
- Avoid modifying a list while iterating over it; iterate over a copy if needed.
- Use list comprehensions for simple loops returning a list.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

