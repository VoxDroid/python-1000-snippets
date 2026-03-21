# sample1.py
# Compute factorial of numbers using ProcessPoolExecutor.

from concurrent.futures import ProcessPoolExecutor


def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(factorial, range(5, 11)))
    print('Factorials:', results)
