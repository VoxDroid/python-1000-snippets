# Conditional Statements Cheatsheet

## Syntax
```python
if condition:
    # code
elif other_condition:
    # code
else:
    # code
```

## Tips
- Conditions should evaluate to a boolean.
- Use `and`, `or`, `not` for compound conditions.
- Avoid deep nesting by using guard clauses or boolean variables.

## Examples
```python
if x > 0 and x < 10:
    print("x is between 0 and 10")

# ternary-like expression
status = "adult" if age >= 18 else "minor"
```

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py` (requires age input)
3. `python SAMPLES/sample2.py` (simulated username/password)
4. `python SAMPLES/sample3.py` (requires grade input)

