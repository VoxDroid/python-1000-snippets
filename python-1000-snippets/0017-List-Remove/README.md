# List Remove

## Description
This snippet shows how to use the `remove()` method to delete a specific element from a Python list by its value.

## Code
```python
fruits = ["apple", "banana", "orange"]
print("Initial list:", fruits)
fruits.remove("banana")
print("After remove:", fruits)
```

## Output
```
Initial list: ['apple', 'banana', 'orange']
After remove: ['apple', 'orange']
```

## Explanation
- **List Remove**: The `remove()` method deletes the first occurrence of a specified value (e.g., `"banana"`).
- **Error Handling**: If the value isn't in the list, `remove()` raises a `ValueError`.
- **Use Case**: Useful for filtering lists, such as removing invalid entries or unwanted items.
- **Alternative**: Use `pop()` for index-based removal or list comprehension for conditional removal.
- **Best Practice**: Check if the element exists (e.g., using `in`) before calling `remove()` to avoid errors.

## Additional Files
- `CHEATSHEET.md` provides examples of `remove()`, `pop()`, and safe removal.
- `SAMPLES/` includes:
  1. `sample1.py` – remove a specific item from a list with validation.
  2. `sample2.py` – use `pop()` to remove by index and show effect.
  3. `sample3.py` – filter items using comprehension instead of remove.

Run samples inside a `.venv` to test removal techniques.