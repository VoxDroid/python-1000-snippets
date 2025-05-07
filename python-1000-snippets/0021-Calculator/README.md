# Calculator

## Description
This snippet implements a simple calculator that performs basic arithmetic operations based on user input, using functions and conditionals.

## Code
```python
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
result = calculator(a, b, op)
print("Result:", result)
```

## Output
```
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): +
Result: 15.0
```
*(If operation is `/` and `b` is `0`):*
```
Enter first number: 10
Enter second number: 0
Enter operation (+, -, *, /): /
Result: Error: Division by zero
```

## Explanation
- **Function**: `calculator(a, b, operation)` performs the requested operation using conditionals.
- **User Input**: Accepts two numbers and an operation symbol.
- **Error Handling**: Checks for division by zero and invalid operations.
- **Use Case**: Demonstrates combining functions, conditionals, and user input for interactive programs.
- **Best Practice**: Add more robust error handling (e.g., for non-numeric inputs) in production code.