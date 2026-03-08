# Loop Break

## Description
This snippet demonstrates the `break` statement in Python, which exits a loop prematurely when a condition is met.

## Code
```python
for i in range(1, 10):
    if i == 5:
        break
    print("Number:", i)
```

## Output
```
Number: 1
Number: 2
Number: 3
Number: 4
```

## Explanation
- **Break Statement**: Exits the nearest enclosing loop when executed, stopping further iterations.
- **Condition**: Here, `break` triggers when `i == 5`, so the loop stops before printing 5.
- **Use Case**: Useful for terminating loops early, like searching for an item or stopping on a condition.
- **Best Practice**: Use `break` sparingly to maintain loop clarity; consider restructuring logic if overused.

## Additional Files
- `CHEATSHEET.md` explains break behavior in `for` and `while` loops.
- `SAMPLES/` includes:
  1. `sample1.py` – search for a value in a list using break.
  2. `sample2.py` – while loop reading input until sentinel using break.
  3. `sample3.py` – nested loops with break to exit inner loop.

Run the samples inside a `.venv` to see break in action.