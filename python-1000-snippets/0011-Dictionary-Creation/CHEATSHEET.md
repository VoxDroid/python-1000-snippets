# Dictionary Creation Cheatsheet

## Basic syntax
```python
d = {"key": "value", "n": 42}
d2 = dict(a=1, b=2)
```

## Accessing and updating
```python
print(d["key"])
d["new"] = 100
```

## Methods
- `keys()`, `values()`, `items()`
- `get(key, default)`
- `pop(key)`, `update()`

## Iteration
```python
for k, v in d.items():
    print(k, v)
```

## Tips
- Use `in` to check for a key: `if "x" in d:`
- `defaultdict` from `collections` avoids missing keys.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

