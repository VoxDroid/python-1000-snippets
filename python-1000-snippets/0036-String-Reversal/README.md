# String Reversal

## Description
This snippet demonstrates how to reverse a string in Python using slicing, a simple and efficient method.

## Code
```python
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)
```

## Output
```
Enter a string: Python
Reversed string: nohtyP
```

## Explanation
- **String Reversal**: The slice `[::-1]` uses a step of `-1` to reverse the string.
- **Slicing**: Syntax `[start:stop:step]` with `step=-1` iterates backward.
- **Use Case**: String reversal is used in text processing, palindrome checks, or coding challenges.
- **Alternative**: Could use a loop or `reversed()` with `join()`, but slicing is most concise.
- **Best Practice**: Use slicing for simplicity; ensure input validation for empty strings.