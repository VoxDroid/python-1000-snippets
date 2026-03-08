# Counter Cheatsheet

## Manual counting
```python
count = 0
for x in seq:
    if x == target:
        count += 1
```

## Using collections.Counter
```python
from collections import Counter
c = Counter(seq)
print(c[target])
```

## Tips
- `Counter` returns dictionary-like object with frequencies.
- Useful for word frequency, histogram, etc.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

