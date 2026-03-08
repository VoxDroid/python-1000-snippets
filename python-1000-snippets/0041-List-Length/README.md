# List Length

## Description
This snippet shows how to find the length of a list in Python using the `len()` function, which returns the number of items.

## Code
```python
items = ["apple", "banana", "orange"]
length = len(items)
print("List length:", length)
```

## Output
```
List length: 3
```

## Explanation
- **len() Function**: Returns the number of elements in a list (or other sequence).
- **Use Case**: List length is used for iteration, validation, or sizing data structures.
- **Applicability**: `len()` works on lists, tuples, strings, sets, and dictionaries.
- **Best Practice**: Use `len()` directly rather than manual counting for efficiency.

## Additional Files
- `CHEATSHEET.md` covering len() usage on different types.
- `SAMPLES/` includes:
  1. `sample1.py` – length of lists and strings.
  2. `sample2.py` – dynamic list with user input.
  3. `sample3.py` – compare lengths of two lists.

Run in a `.venv` to verify outputs.