# Custom Iteration Pattern

## Description
This snippet demonstrates a custom iterator for even numbers.

## Code
```python
class EvenNumbers:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

evens = EvenNumbers(6)
print(list(evens))
```

## Output
```
[0, 2, 4, 6]
```

## Explanation
- **Custom Iteration Pattern**: Iterates over even numbers up to a limit.
- **Logic**: Implements `__iter__` and `__next__` for even number sequence.
- **Complexity**: O(n) for n numbers.
- **Use Case**: Used for custom sequence generation.
- **Best Practice**: Ensure termination; handle edge cases; test iterator protocol.