# List Append

## Description
This snippet demonstrates the `append()` method to add elements to a Python list, showcasing how to dynamically grow a list.

## Code
```python
colors = ["red", "blue"]
print("Initial list:", colors)
colors.append("green")
print("After append:", colors)
```

## Output
```
Initial list: ['red', 'blue']
After append: ['red', 'blue', 'green']
```

## Explanation
- **List Append**: The `append()` method adds a single element to the end of a list.
- **Mutability**: Lists are mutable, so `append()` modifies the list in place.
- **Use Case**: Appending is used to build lists dynamically, such as collecting user inputs or accumulating results.
- **Performance**: `append()` is efficient (O(1) time complexity) for adding elements to the end.
- **Best Practice**: Use `append()` for single elements; for multiple elements, consider `extend()` or list concatenation.

## Additional Files
- `CHEATSHEET.md` covers `append()` vs `extend()`, and when to use list comprehensions.
- `SAMPLES/` includes:
  1. `sample1.py` – accumulate user-entered numbers.
  2. `sample2.py` – build a list conditionally in a loop.
  3. `sample3.py` – show difference between append and extend.

Test samples under a `.venv` to verify behavior.