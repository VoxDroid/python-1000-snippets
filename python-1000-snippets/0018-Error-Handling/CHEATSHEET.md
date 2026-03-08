# Error Handling Cheatsheet

## Structure
```python
try:
    # risky code
except SomeError as e:
    # handle error
else:
    # runs if no exception
finally:
    # always runs
```

## Common exceptions
- `ValueError`, `TypeError`, `ZeroDivisionError`, `FileNotFoundError`

## Tips
- Log or print exception details using `as e`.
- Re-raise with `raise` if you can't handle it.
- Use `finally` for cleanup (closing files, releasing resources).

## Example
```python
try:
    x = int(input())
except ValueError:
    print("Not an int")
```

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (takes input)
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

