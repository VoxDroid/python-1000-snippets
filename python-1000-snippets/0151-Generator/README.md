# Generator

## Description
This snippet demonstrates a Python generator to yield Fibonacci numbers up to a given limit.

## Code
```python
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

fib = fibonacci(10)
print("Fibonacci:", list(fib))
```

## Output
```
Fibonacci: [0, 1, 1, 2, 3, 5, 8]
```

## Explanation
- **Generator**: Uses `yield` to produce values lazily, saving memory compared to storing a full list.
- **Logic**: Yields Fibonacci numbers where each is the sum of the previous two, up to `n`.
- **Complexity**: O(n) time, O(1) space per yield.
- **Use Case**: Used for streaming large datasets or infinite sequences.
- **Best Practice**: Use generators for memory efficiency; avoid reusing exhausted generators.