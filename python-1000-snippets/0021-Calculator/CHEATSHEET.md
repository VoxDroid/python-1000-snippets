# Calculator Cheatsheet

## Supported operations
- `+`, `-`, `*`, `/` (division handles zero)
- Additional examples show `%` and `**` (modulus and exponent)

## Input validation
- Convert inputs with `float()` and catch `ValueError`.
- Use a loop to re-prompt user on invalid input.

## Sample code patterns
```python
try:
    a = float(input())
except ValueError:
    print("Not a number")
```

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (uses piped input)
3. `python SAMPLES/sample2.py` (piped input)
4. `python SAMPLES/sample3.py` (interactive loop simulated)

