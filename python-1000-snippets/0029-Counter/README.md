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

## Additional Files
- `CHEATSHEET.md` covers manual counting versus `collections.Counter` usage.
- `SAMPLES/` includes:
  1. `sample1.py` – count characters in a string manually.
  2. `sample2.py` – use `collections.Counter` to count word frequency.
  3. `sample3.py` – count occurrences of items in a list.

Run samples under a `.venv` to compare manual and built-in counters.
- **Best Practice**: Validate input (e.g., non-empty string) for robustness.