# Loop Break Cheatsheet

## Syntax
```python
for x in seq:
    if cond:
        break
```

## Use with while
```python
while True:
    if cond:
        break
```
```

## Nested loops
- `break` breaks only the innermost loop.
- Use flags or functions to exit multiple loops.

## Tips
- Often used in searching or validating input.
- After break, else clause of loop (if present) is skipped.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py` (using piped input)
4. `python SAMPLES/sample3.py`

