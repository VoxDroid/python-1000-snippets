# Variable Declaration Cheatsheet

Quick reference for declaring and using variables in Python.

## Basic Assignment
```python
x = 10           # integer
name = "Bob"    # string
pi = 3.14159      # float
flag = True       # boolean

# No semicolon needed; newline terminates the statement.
```

## Multiple Variables
```python
a, b, c = 1, 2, 3      # parallel assignment
x = y = z = 0           # same value to multiple names
```

## Dynamic Typing
```python
var = 5
var = "now a string"   # allowed, type changes at runtime
```

## Common Tips
- Variable names must start with a letter or underscore and may contain letters, digits, and underscores.
- Avoid using Python reserved keywords (`class`, `for`, `if`, etc.) as variable names.
- Use descriptive names (`user_age` vs `a`) for readability.

## Running Samples
1. Create and activate virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Execute sample files:
   ```bash
   python SAMPLES/sample1.py
   python SAMPLES/sample2.py
   python SAMPLES/sample3.py
   ```

