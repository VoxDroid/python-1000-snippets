# Temperature Conversion Cheatsheet

## Formulas
- Celsius to Fahrenheit: `(C * 9/5) + 32`
- Fahrenheit to Celsius: `(F - 32) * 5/9`

## Example function
```python
def convert(value, unit):
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
```

## Tips
- Convert unit input to upper-case.
- Handle invalid units gracefully.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (requires input)
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py` (interactive loop simulated)

