# String Concatenation Cheatsheet

How to combine strings in Python efficiently.

## Using `+`
```python
first = "Hello"
second = "world"
result = first + ", " + second + "!"
```

## f-strings
```python
name = "Alice"
greeting = f"Hi, {name}!"
```

## `join()` for lists
```python
words = ["one", "two", "three"]
print(" ".join(words))  # "one two three"
```

## Tips
- Avoid concatenating many strings with `+` in loops; use `str.join` or f-strings.
- f-strings allow expressions: `f"{2+2}"` produces "4".
- Use raw strings (`r""`) to prevent escape processing when concatenating path fragments.

## Running samples
1. Activate virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Run each sample:
   ```bash
   python SAMPLES/sample1.py
   python SAMPLES/sample2.py
   python SAMPLES/sample3.py
   ```

