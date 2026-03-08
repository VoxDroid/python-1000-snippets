# Set Creation Cheatsheet

## Creating sets
```python
s = {1, 2, 3}
s2 = set([1,2,3])
```

## Properties
- Unordered, unique elements.
- Not indexable.

## Common methods
- `add()`, `remove()`, `discard()`
- `union()`, `intersection()`, `difference()`

## Membership testing
```
if x in s:
    print("present")
```

## Tip
Convert a list to a set to remove duplicates: `set(list)`

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

