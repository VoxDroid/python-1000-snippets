# List Sorting Cheatsheet

## Methods
- `lst.sort()` modifies list in place.
- `sorted(lst)` returns new sorted list.

## Parameters
- `reverse=True` for descending order.
- `key=` specify function to extract comparison key.

## Examples
```python
words.sort(key=len)
```

## Tips
- Sorting is stable: preserves order of equal elements.
- Use `operator.itemgetter` for tuples: `key=itemgetter(1)`.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

