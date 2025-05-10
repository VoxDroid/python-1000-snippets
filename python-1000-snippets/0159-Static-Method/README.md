# Static Method

## Description
This snippet defines a static method in a class that doesn’t require instance or class access.

## Code
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print("Sum:", MathUtils.add(5, 3))
```

## Output
```
Sum: 8
```

## Explanation
- **Static Method**: Uses `@staticmethod` to define `add`, which doesn’t access `self` or `cls`.
- **Logic**: Simply returns the sum of two numbers.
- **Complexity**: O(1) for the operation.
- **Use Case**: Used for utility functions related to a class but independent of its state.
- **Best Practice**: Use for methods that logically belong to a class but don’t need instance data.