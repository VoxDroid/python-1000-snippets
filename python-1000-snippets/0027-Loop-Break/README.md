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