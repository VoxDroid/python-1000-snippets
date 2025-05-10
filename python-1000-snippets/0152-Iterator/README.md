# Iterator

## Description
This snippet defines a custom iterator class to iterate over a range of numbers with a specified step.

## Code
```python
class StepRange:
    def __init__(self, start, end, step):
        self.current = start
        self.end = end
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

for num in StepRange(0, 10, 2):
    print(num, end=" ")
```

## Output
```
0 2 4 6 8
```

## Explanation
- **Iterator**: Implements `__iter__` and `__next__` to create a custom iterable.
- **Logic**: Iterates from `start` to `end` with `step` increments.
- **Complexity**: O(n) time for n iterations, O(1) space.
- **Use Case**: Used for custom iteration logic or wrapping data structures.
- **Best Practice**: Raise `StopIteration` correctly; ensure `__iter__` returns self.