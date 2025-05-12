# Complex Lambda Expressions

## Description
This snippet demonstrates a complex lambda expression for conditional mapping.

## Code
```python
data = [1, -2, 3, -4]
transformed = list(map(lambda x: x**2 if x > 0 else -x, data))
print("Transformed:", transformed)
```

## Output
```
Transformed: [1, 2, 9, 4]
```

## Explanation
- **Complex Lambda Expressions**: Applies conditional logic within a lambda function.
- **Logic**: Squares positive numbers, negates negative numbers.
- **Complexity**: O(n) for n elements.
- **Use Case**: Used for concise data transformations.
- **Best Practice**: Ensure readability; avoid overuse; test edge cases.