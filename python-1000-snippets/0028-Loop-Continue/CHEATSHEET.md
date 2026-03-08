# Loop Continue Cheatsheet

## Syntax
```python
for x in seq:
    if cond:
        continue
    # code for non-cond case
```

## Use with while
```python
while condition:
    if skip:
        continue
    # rest
```
```

## Notes
- Skips only current iteration, not entire loop.
- Useful for filtering inside loops.

## Tips
- Pair with `break` for combined control.
- In nested loops, continue affects innermost only.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py` (simulate input)
4. `python SAMPLES/sample3.py`

