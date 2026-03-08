# sample1.py
# Iterative factorial with input validation.

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

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

