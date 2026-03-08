# sample3.py
# interactive calculator for two numbers

def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if b != 0:
        print(f"{a} / {b} = {a / b}")
        print(f"{a} // {b} = {a // b}")
        print(f"{a} % {b} = {a % b}")
    else:
        print("cannot divide by zero")
    print(f"{a} ** {b} = {a ** b}")

if __name__ == '__main__':
    main()

