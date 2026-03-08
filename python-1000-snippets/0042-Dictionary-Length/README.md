# Dictionary Length

## Description
This snippet demonstrates how to find the number of key-value pairs in a dictionary using the `len()` function.

## Code
```python
person = {"name": "Alice", "age": 25, "city": "Boston"}
length = len(person)
print("Dictionary length:", length)
```

## Output
```
Dictionary length: 3
```

## Explanation
- **len() Function**: Returns the number of key-value pairs in a dictionary.
- **Use Case**: Dictionary length is used for validation, iteration, or checking data completeness.
- **Applicability**: `len()` works on any collection type, including dictionaries.
- **Best Practice**: Use `len()` to check dictionary size before operations like iteration.

## Additional Files
- `CHEATSHEET.md` describing len() on dicts with examples.
- `SAMPLES/` contains:
  1. `sample1.py` – measure length of a fixed dict.
  2. `sample2.py` – build a dict from input and show length.
  3. `sample3.py` – compare lengths of two dictionaries.

Run the samples under a `.venv` environment.