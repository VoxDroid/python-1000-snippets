# User Input

## Description
This snippet demonstrates how to capture user input in Python using the `input()` function. It allows programs to interact with users by accepting text or numbers.

## Code
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")
```

## Output
```
Enter your name: Alice
Enter your age: 25
Hello, Alice! You are 25 years old.
```

## Explanation
- **`input()` Function**: Prompts the user to enter data via the console. The argument (e.g., `"Enter your name: "`) is displayed as a prompt.
- **Return Type**: `input()` always returns a string, even if the user enters numbers. To use numbers in calculations, convert the input using `int()` or `float()`.
- **Type Conversion**: `int(input(...))` converts the string input to an integer. Be cautious, as invalid input (e.g., letters) will raise a `ValueError`.
- **Use Case**: User input is critical for interactive applications like forms, games, or command-line tools.
- **Error Handling**: In production code, you should add error handling (e.g., `try-except`) to manage invalid inputs gracefully.