# Iterator Pattern

## Description
This snippet implements the Iterator pattern to provide a way to traverse a collection.

## Code
```python
class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value

class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers
    def get_iterator(self):
        return NumberIterator(self.numbers)

collection = NumberCollection([1, 2, 3])
for num in collection.get_iterator():
    print(num, end=" ")
```

## Output
```
1 2 3
```

## Explanation
- **Iterator Pattern**: `NumberIterator` provides sequential access to `NumberCollection`’s elements.
- **Logic**: Implements `__iter__` and `__next__` for iteration.
- **Complexity**: O(n) for n elements.
- **Use Case**: Used for traversing complex data structures like trees or graphs.
- **Best Practice**: Ensure iterator is stateless; support multiple iterators.