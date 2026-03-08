# String Methods

## Description
This snippet showcases common string methods in Python for manipulating text, such as changing case, stripping whitespace, or replacing substrings.

## Code
```python
text = "  Hello, Python!  "
print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Stripped:", text.strip())
print("Replaced:", text.replace("Python", "World"))
```

## Output
```
Original:   Hello, Python!  
Uppercase:   HELLO, PYTHON!  
Lowercase:   hello, python!  
Stripped: Hello, Python!
Replaced:   Hello, World!  
```

## Explanation
- **String Methods**:
  - `upper()`: Converts to uppercase.
  - `lower()`: Converts to lowercase.
  - `strip()`: Removes leading/trailing whitespace.
  - `replace(old, new)`: Replaces all occurrences of `old` with `new`.
- **Immutability**: Strings are immutable, so methods return new strings without modifying the original.
- **Use Case**: String methods are used for text processing, user input cleaning, or formatting.
- **Best Practice**: Chain methods (e.g., `text.strip().lower()`) for concise operations.
## Additional Files
- `CHEATSHEET.md` lists common string methods (split, join, find, etc.).
- `SAMPLES/` includes:
  1. `sample1.py` – demonstrates various methods on one string.
  2. `sample2.py` – trim and replace whitespace in user input.
  3. `sample3.py` – use `split()` and `join()` to reverse word order.

Run samples inside a `.venv` to try different string operations.