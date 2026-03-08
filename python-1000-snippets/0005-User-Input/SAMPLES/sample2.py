# sample2.py
# Simple calculator that asks the user for two numbers.

def main():
    try:
        a = float(input("First number: ").strip())
        b = float(input("Second number: ").strip())
    except ValueError:
        print("Both inputs must be numeric.")
        return
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    if b != 0:
        print(f"{a} / {b} = {a/b}")
    else:
        print("Cannot divide by zero")

if __name__ == '__main__':
    main()

