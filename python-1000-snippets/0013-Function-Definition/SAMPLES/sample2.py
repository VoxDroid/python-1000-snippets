# sample2.py
# Recursive factorial function example.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    print("5! =", factorial(5))

