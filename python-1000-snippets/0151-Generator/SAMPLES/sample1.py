# sample1.py
# fibonacci generator example (matching README)

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    print('Fibonacci up to 15:', list(fibonacci(15)))
