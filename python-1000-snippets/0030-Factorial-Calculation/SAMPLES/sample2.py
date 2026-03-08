# sample2.py
# Recursive factorial function.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    try:
        n = int(input("Enter non-negative integer: "))
    except ValueError:
        print("Not an integer")
    else:
        if n < 0:
            print("Invalid, negative")
        else:
            print(factorial(n))

