# 0335-Nested-Dictionary-Processing Cheatsheet

## Quick commands
```bash
python SAMPLES/sample1.py  # Safe extraction of nested values
python SAMPLES/sample2.py  # Flatten a nested dict
python SAMPLES/sample3.py  # Deep merge nested dictionaries
```

## Tips
- Use `.get()` when walking nested dictionaries to avoid `KeyError`.
- For deep operations, consider recursion with explicit depth tracking.
- Use comprehensions to transform nested dicts into lists or new dicts.

## Example outline (safe access)
```python
x_values = [d.get('x') for d in data.values() if isinstance(d, dict)]
```

## Example outline (flatten)
```python
def flatten(d, parent=''):
    for k, v in d.items():
        key = f"{parent}.{k}" if parent else k
        if isinstance(v, dict):
            yield from flatten(v, key)
        else:
            yield key, v
```
