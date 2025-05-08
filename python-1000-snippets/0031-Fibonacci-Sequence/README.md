# Fibonacci Sequence

## Description
This snippet generates the Fibonacci sequence up to a specified number of terms using a loop. The Fibonacci sequence starts with 0 and 1, where each subsequent number is the sum of the two preceding ones.

## Code
```python
def fibonacci(n):
    sequence = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

n = int(input("Enter number of terms: "))
result = fibonacci(n)
print("Fibonacci sequence:", result)
```

## Output
```
Enter number of terms: 6
Fibonacci sequence: [0, 1, 1, 2, 3, 5]
```

## Explanation
- **Fibonacci Logic**: Starts with `[0, 1]`, then each term is the sum of the previous two (e.g., `0+1=1`, `1+1=2`, `1+2=3`).
- **Function**: `fibonacci(n)` generates `n` terms, handling edge cases (e.g., `n <= 0` or `n == 1`).
- **Loop**: Appends new terms by summing the last two elements of the list.
- **Use Case**: Fibonacci sequences appear in algorithms, mathematics, and nature-inspired computations.
- **Best Practice**: For large `n`, consider recursive or generator-based solutions to optimize memory.