# While Loop

## Description
This snippet showcases the `while` loop in Python, which repeatedly executes a block of code as long as a condition remains true.

## Code
```python
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
```

## Output
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

## Explanation
- **`while` Loop**: Continues looping as long as the condition (`count <= 5`) evaluates to `True`.
- **Increment**: `count += 1` increases `count` by 1 each iteration to eventually exit the loop. Without this, the loop would run indefinitely (infinite loop).
- **Condition**: Checked before each iteration. If `False`, the loop stops.
- **Use Case**: `while` loops are useful when the number of iterations isn't known in advance, such as waiting for user input or processing until a condition changes.
- **Caution**: Always ensure the loop condition will eventually become `False` to avoid infinite loops.
- **Best Practice**: Use `while` loops for condition-driven tasks and `for` loops for sequence-driven tasks.