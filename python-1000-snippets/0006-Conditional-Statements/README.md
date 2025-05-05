# Conditional Statements

## Description
This snippet introduces conditional statements (`if`, `elif`, `else`) in Python, which allow the program to make decisions based on conditions.

## Code
```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```

## Output
```
Enter your age: 20
You are an adult.
```

## Explanation
- **Conditional Structure**:
  - `if`: Checks the first condition. If true, executes its block.
  - `elif`: Checks additional conditions if the previous `if` or `elif` is false.
  - `else`: Executes if no previous conditions are true.
- **Indentation**: Python uses indentation (typically 4 spaces) to define the scope of code blocks under `if`, `elif`, or `else`.
- **Conditions**: Uses comparison operators like `>=` to evaluate expressions. The result must be a boolean (`True` or `False`).
- **Use Case**: Conditionals are used for decision-making in applications like user authentication, game logic, or data filtering.
- **Best Practice**: Keep conditions clear and avoid deeply nested `if` statements for better readability.