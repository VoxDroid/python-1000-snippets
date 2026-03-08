# List Length Cheatsheet

## Using `len()`
- `len(seq)` returns number of items.
- Works with lists, strings, tuples, sets, dicts (dict returns number of keys).

## Tips
- `len([])` is 0; empty sequences are easy to check.
- For custom objects, define `__len__` to support len().

## Examples
```python
if len(my_list) > 5:
    print('long list')
```

## Running samples
Activate venv and run each script under `SAMPLES/`.
