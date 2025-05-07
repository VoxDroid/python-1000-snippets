# Function Definition

## Description
This snippet illustrates how to define a function in Python. Functions are reusable blocks of code that perform a specific task, improving code modularity and readability.

## Code
```python
def greet(name):
    message = f"Hello, {name}!"
    print(message)

greet("Bob")
```

## Output
```
Hello, Bob!
```

## Explanation
- **Function Definition**: Use the `def` keyword, followed by the function name (`greet`), parameters in parentheses (`name`), and a colon (`:`).
- **Body**: The indented code block under the function defines its behavior. Here, it creates and prints a greeting.
- **Calling**: Invoke the function with `greet("Bob")`, passing `"Bob"` as the argument.
- **Use Case**: Functions are used to encapsulate logic, reduce repetition, and organize code (e.g., for calculations, user interactions).
- **Best Practice**: Use descriptive function names and include docstrings for complex functions to explain their purpose.