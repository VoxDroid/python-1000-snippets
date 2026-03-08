# sample2.py
# Extended calculator with power and modulus operations.

def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Error: Division by zero"
    elif operation == "%":
        return a % b
    elif operation == "**":
        return a ** b
    else:
        return "Invalid operation"

if __name__ == '__main__':
    a = float(input("a: "))
    b = float(input("b: "))
    op = input("op: ")
    print(calculator(a, b, op))

