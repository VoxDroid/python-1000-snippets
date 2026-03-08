# User Input Cheatsheet

## Basic usage
```python
name = input("Enter your name: ")   # returns string
age_str = input("Age: ")
age = int(age_str)                    # convert to int
```

## Converting types
- `int()`, `float()`, `bool()` can cast input strings.
- Always catch `ValueError` if the user types invalid data.

## Prompting
- The string passed to `input()` is shown as the prompt.
- Use `strip()` to clean whitespace: `input(...).strip()`.

## Example patterns
```python
# loop until valid integer entered
while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid integer")
```

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py`
4. `python SAMPLES/sample3.py`

