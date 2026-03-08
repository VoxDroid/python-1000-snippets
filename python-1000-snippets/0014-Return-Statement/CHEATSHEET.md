# Return Statement Cheatsheet

## Basic usage
```python
def add(a, b):
    return a + b
```

## Returning multiple values
```python
def stats(lst):
    return (min(lst), max(lst), sum(lst))
```

## Early return
```python
def f(x):
    if x < 0:
        return None
    # rest of code
```

## Notes
- A function without `return` returns `None`.
- Use `return` to exit function and send value to caller.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

