# Static Method Patterns

## Description
This snippet demonstrates static methods for utility functions.

## Code
```python
class MathUtils:
    @staticmethod
    def square(n):
        return n * n

print(MathUtils.square(5))
```

## Output
```
25
```

## Explanation
- **Static Method Patterns**: Defines utility methods without instance dependency.
- **Logic**: Uses `@staticmethod` to create a squaring function.
- **Complexity**: O(1) per call.
- **Use Case**: Used for utility functions related to a class.
- **Best Practice**: Use for stateless methods; avoid instance access; ensure relevance to class.