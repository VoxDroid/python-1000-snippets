# Loop Continue

## Description
This snippet shows the `continue` statement in Python, which skips the rest of the current loop iteration and proceeds to the next.

## Code
```python
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print("Odd number:", i)
```

## Output
```
Odd number: 1
Odd number: 3
Odd number: 5
```

## Explanation
- **Continue Statement**: Skips the remaining code in the current iteration and moves to the next iteration.
- **Condition**: Here, `continue` triggers for even numbers (`i % 2 == 0`), skipping their `print`.
- **Use Case**: Useful for filtering iterations, like skipping invalid data or specific cases.
- **Best Practice**: Use `continue` to simplify loop logic, but avoid overuse to keep code readable.

## Additional Files
- `CHEATSHEET.md` describes `continue` usage and common patterns.
- `SAMPLES/` includes:
  1. `sample1.py` – skip negative numbers in a list.
  2. `sample2.py` – while loop prompting for positive values skipping invalid ones.
  3. `sample3.py` – continue in nested loops to skip inner processing.

Run these samples in a `.venv` to see `continue` in action.