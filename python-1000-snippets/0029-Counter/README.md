# Counter

## Description
This snippet implements a simple counter using a loop to count occurrences of a specific character in a string.

## Code
```python
text = "banana"
char = "a"
count = 0
for c in text:
    if c == char:
        count += 1
print(f"Character '{char}' appears {count} times.")
```

## Output
```
Character 'a' appears 3 times.
```

## Explanation
- **Counter Logic**: Iterates through each character in `text`, incrementing `count` when `char` is found.
- **Loop**: A `for` loop processes each character in the string.
- **Use Case**: Counting is used in text analysis, data validation, or frequency calculations.
- **Alternative**: Use `text.count(char)` for a built-in solution, but this shows manual counting logic.
- **Best Practice**: Validate input (e.g., non-empty string) for robustness.