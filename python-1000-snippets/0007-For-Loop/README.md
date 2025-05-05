# For Loop

## Description
This snippet demonstrates the `for` loop in Python, which iterates over a sequence (e.g., a list, range, or string) to perform repetitive tasks.

## Code
```python
for i in range(1, 6):
    print(f"Number: {i}")
```

## Output
```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

## Explanation
- **`for` Loop**: Iterates over each item in a sequence. Here, `range(1, 6)` generates numbers from 1 to 5 (6 is excluded).
- **`range()` Function**: Creates a sequence of numbers. Syntax: `range(start, stop, step)` (step is optional, defaults to 1).
- **Variable `i`**: Takes on each value in the sequence during iteration.
- **Use Case**: `for` loops are ideal for tasks like processing lists, generating sequences, or repeating actions a fixed number of times.
- **Flexibility**: `for` loops can iterate over any iterable, such as lists (`[1, 2, 3]`), strings (`"hello"`), or tuples.
- **Best Practice**: Use descriptive loop variable names (e.g., `number` instead of `i`) when the context isn't obvious.