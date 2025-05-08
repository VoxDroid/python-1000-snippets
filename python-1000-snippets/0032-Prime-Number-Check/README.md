# Prime Number Check

## Description
This snippet checks if a given number is prime. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

## Code
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(f"{num} is {'prime' if is_prime(num) else 'not prime'}.")
```

## Output
```
Enter a number: 17
17 is prime.
```
*(If input is `4`):*
```
Enter a number: 4
4 is not prime.
```

## Explanation
- **Prime Logic**: A number is prime if it’s only divisible by 1 and itself. The function checks divisibility up to the square root of `n` for efficiency.
- **Function**: `is_prime(n)` returns `True` if `n` is prime, `False` otherwise.
- **Optimization**: Only checks divisors up to `sqrt(n)`, as larger divisors would have a smaller counterpart already checked.
- **Use Case**: Prime checks are used in cryptography, number theory, and algorithm design.
- **Best Practice**: Handle invalid inputs (e.g., non-integers) with error handling in production.