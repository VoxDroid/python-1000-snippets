# List Comprehension

## Description
This snippet demonstrates list comprehension in Python, a concise way to create lists by applying an expression to each item in an iterable, optionally with a condition.

## Code
```python
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print("All squares:", squares)
print("Even squares:", even_squares)
```

## Output
```
All squares: [1, 4, 9, 16, 25]
Even squares: [4, 16]
```

## Explanation
- **List Comprehension**: Syntax `[expression for item in iterable if condition]` creates a new list.
- **Examples**:
  - `squares`: Computes the square of each number in `numbers`.
  - `even_squares`: Computes squares only for even numbers (using `if x % 2 == 0`).
- **Use Case**: List comprehensions are used for concise data transformations, like filtering or mapping.
- **Best Practice**: Use list comprehensions for readability, but avoid overly complex expressions.