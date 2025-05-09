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