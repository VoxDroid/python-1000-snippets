# List Slicing Cheatsheet

## Syntax
```python
lst[start:stop:step]
```
- `start` inclusive, `stop` exclusive.
- `step` default 1; negative for reverse.

## Examples
```python
lst = [0,1,2,3,4]
print(lst[::-1])     # reverse
print(lst[1:4])      # [1,2,3]
print(lst[:3])       # first three
print(lst[::2])      # every other element
```

## Tips
- Omitting `start` or `stop` defaults to beginning or end.
- Use slicing on strings too: `s = "hello"; s[1:4]`.
- Be cautious with large step values; empty list may result.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

