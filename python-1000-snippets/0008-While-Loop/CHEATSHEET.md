# While Loop Cheatsheet

## Syntax
```python
while condition:
    # code
```

## Loop control
- `break` exits the loop immediately.
- `continue` skips to the next iteration.

## Common patterns
```python
count = 0
while count < 10:
    count += 1

# loop until valid input
while True:
    val = input("...")
    if val == "quit":
        break
```

## Caution
Always modify a variable used in the condition to avoid infinite loops.

## Running samples
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `python SAMPLES/sample1.py`
3. `python SAMPLES/sample2.py` (uses piped input)
4. `python SAMPLES/sample3.py` (uses piped input)

