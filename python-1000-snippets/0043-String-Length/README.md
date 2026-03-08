# String Length

## Description
This snippet shows how to find the length of a string in Python using the `len()` function, which counts characters (including spaces).

## Code
```python
text = "Hello, World!"
length = len(text)
print("String length:", length)
```

## Output
```
String length: 13
```

## Explanation
- **len() Function**: Returns the number of characters in a string, including spaces and punctuation.
- **Use Case**: String length is used in text processing, validation, or formatting.
- **Unicode**: `len()` counts code points, which may differ from visual characters in some Unicode strings.
- **Best Practice**: Use `len()` for simple length checks; consider encoding for complex text.

## Additional Files
- `CHEATSHEET.md` describes string length nuances and Unicode.
- `SAMPLES/` includes:
  1. `sample1.py` – measure a fixed string.
  2. `sample2.py` – read user input and print length.
  3. `sample3.py` – compare lengths of two input strings.

Run samples inside a `.venv` to observe behavior.