# sample2.py
# Recursive generator yielding Fibonacci numbers.

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    n = int(input("Enter number of terms: "))
    print(list(fib(n)))

