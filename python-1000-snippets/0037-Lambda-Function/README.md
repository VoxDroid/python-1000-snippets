# Lambda Function

## Description
This snippet introduces lambda functions in Python, which are small, anonymous functions defined with the `lambda` keyword for concise operations.

## Code
```python
square = lambda x: x ** 2
add = lambda x, y: x + y
print("Square of 5:", square(5))
print("Sum of 3 and 4:", add(3, 4))
```

## Output
```
Square of 5: 25
Sum of 3 and 4: 7
```

## Explanation
- **Lambda Syntax**: `lambda arguments: expression` creates a function without a name.
- **Examples**:
  - `square`: Takes one argument and returns its square.
  - `add`: Takes two arguments and returns their sum.
- **Use Case**: Lambda functions are used in functional programming, sorting, or as arguments to higher-order functions.
- **Best Practice**: Use lambda for simple operations; define named functions for complex logic.