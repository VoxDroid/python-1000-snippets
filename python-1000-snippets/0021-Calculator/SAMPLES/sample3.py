# sample3.py
# Looping calculator that runs until user types 'quit'.

def calculator(a, b, op):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Invalid numbers"
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else "Error"
    return "Invalid op"

if __name__ == '__main__':
    while True:
        line = input("Enter a op b (or quit): ")
        if line.strip().lower() == "quit":
            break
        parts = line.split()
        if len(parts) != 3:
            print("Format: a op b")
            continue
        a, op, b = parts
        print(calculator(a, b, op))

