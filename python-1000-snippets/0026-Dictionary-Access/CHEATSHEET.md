# Dictionary Access Cheatsheet

## Access
- `value = d[key]` (KeyError if missing)
- `value = d.get(key)` (None if missing)
- `value = d.get(key, default)`

## Other techniques
```python
if key in d:
    print(d[key])
value = d.setdefault(key, default)
```

## Iteration
```python
for k in d: print(k)
for k,v in d.items(): print(k,v)
```

## Tips
- Use `d.get` to provide default values.
- `d.keys()`, `d.values()`, `d.items()` return views.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

