# Custom Iterator Design

## Description
This snippet demonstrates a custom iterator for Fibonacci numbers.

## Code
```python
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

fib = Fibonacci(5)
print("Fibonacci:", list(fib))
```

## Output
```
Fibonacci: [0, 1, 1, 2, 3]
```

## Explanation
- **Custom Iterator Design**: Creates an iterator for the first n Fibonacci numbers.
- **Logic**: Implements `__iter__` and `__next__` to generate Fibonacci sequence.
- **Complexity**: O(n) for n numbers.
- **Use Case**: Used for custom sequence generation.
- **Best Practice**: Implement iterator protocol; handle edge cases; ensure termination.