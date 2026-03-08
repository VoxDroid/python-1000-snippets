# sample1.py
# Basic calculator using user input and operation symbol.

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

if __name__ == '__main__':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    print("Result:", calculator(a, b, op))

