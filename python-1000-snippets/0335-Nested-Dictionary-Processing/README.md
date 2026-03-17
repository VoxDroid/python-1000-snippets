# Nested Dictionary Processing

## Description
This snippet demonstrates Python techniques for reading, transforming, and merging nested dictionaries (common in JSON-like data structures).

## Files
- `SAMPLES/sample1.py`: Extract specific nested values with safe key access.
- `SAMPLES/sample2.py`: Flatten a nested dictionary into dot-delimited keys.
- `SAMPLES/sample3.py`: Deep-merge two nested dictionaries.

## Quick start
```bash
python SAMPLES/sample1.py
python SAMPLES/sample2.py
python SAMPLES/sample3.py
```

## Output (example)
```
X values: [1, 3]
Flattened: {'a.x': 1, 'a.y': 2, 'b.x': 3, 'b.y': 4}
Merged: {'a': {'x': 1, 'y': 2, 'z': 9}, 'b': {'x': 3, 'y': 4}}
```

## Explanation
- **Nested dictionary processing**: Often needed when consuming APIs or configuration files.
- **Logic**: Use recursion and list/dict comprehensions to navigate nested structures.
- **Best practice**: Validate keys exist; avoid `KeyError`s by using `.get()` or `try/except`.
