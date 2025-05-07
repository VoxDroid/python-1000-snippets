# Factorial Calculation

## Description
This snippet calculates the factorial of a non-negative integer using a loop, demonstrating iterative computation.

## Code
```python
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Factorial of {n} is {factorial}")
```

## Output
```
Enter a non-negative integer: 5
Factorial of 5 is 120
```
*(If input is `-1`):*
```
Enter a non-negative integer: -1
Factorial is not defined for negative numbers.
```

## Explanation
- **Factorial**: The product of all positive integers up to `n` (e.g., `5! = 5 * 4 * 3 * 2 * 1 = 120`).
- **Loop**: Multiplies `factorial` by each integer from 1 to `n`.
- **Input Validation**: Checks for negative numbers, as factorial is undefined for them.
- **Use Case**: Factorials are used in combinatorics, probability, and algorithm design.
- **Best Practice**: Add error handling for non-integer inputs and consider recursive solutions for advanced use.