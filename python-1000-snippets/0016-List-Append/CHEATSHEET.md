# List Append Cheatsheet

## append() method
```python
lst = []
lst.append(1)
```

## extend() vs append()
```python
lst.extend([2,3])   # adds elements individually
lst.append([4,5])   # adds list as single element
```

## Use with loops
```python
for i in range(5):
    lst.append(i)
```

## Tips
- `append()` returns `None` (modifies in place).
- For performance building large lists, appending is efficient.
- Use list comprehensions when building from existing iterables.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (simulated input)
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

