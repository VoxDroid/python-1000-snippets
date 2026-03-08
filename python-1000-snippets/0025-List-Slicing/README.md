# List Slicing

## Description
This snippet demonstrates list slicing in Python, which extracts a subset of elements from a list using a start, stop, and step.

## Code
```python
numbers = [0, 1, 2, 3, 4, 5]
print("Full list:", numbers)
print("First three:", numbers[:3])
print("Last three:", numbers[-3:])
print("Every second:", numbers[::2])
```

## Output
```
Full list: [0, 1, 2, 3, 4, 5]
First three: [0, 1, 2]
Last three: [3, 4, 5]
Every second: [0, 2, 4]
```

## Explanation
- **Slicing Syntax**: `list[start:stop:step]` extracts elements from `start` to `stop-1` with `step` increments.
- **Defaults**: Omitting `start` defaults to 0, `stop` to the end, and `step` to 1.
- **Negative Indices**: `-3` refers to the third element from the end.
- **Use Case**: Slicing is used for extracting sublists, reversing lists, or sampling data.
- **Best Practice**: Use slicing for readable subset extraction; avoid modifying lists while slicing.

## Additional Files
- `CHEATSHEET.md` explains slice notation, negative steps, and reversing lists.
- `SAMPLES/` includes:
  1. `sample1.py` – reverse a list using slicing.
  2. `sample2.py` – skip elements using step.
  3. `sample3.py` – slice strings as well as lists.

Run samples under a `.venv` to explore different slicing behaviors.