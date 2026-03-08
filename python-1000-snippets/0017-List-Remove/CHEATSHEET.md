# List Remove Cheatsheet

## remove() method
```python
lst = [1,2,3]
lst.remove(2)   # removes first occurrence
```

## pop() method
```python
lst.pop(0)       # removes by index, returns value
```

## Safe removal
```python
if item in lst:
    lst.remove(item)
```

## Using comprehension to filter
```python
lst = [x for x in lst if x != unwanted]
```

## Tips
- `remove()` raises `ValueError` if element not found.
- `pop()` with no argument removes and returns last element.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (no input required)
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

