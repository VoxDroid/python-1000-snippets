# Generator Pipelines

## Description
This snippet demonstrates a generator pipeline to process data lazily.

## Code
```python
def square_gen(numbers):
    for n in numbers:
        yield n**2

def filter_gen(numbers):
    for n in numbers:
        if n > 10:
            yield n

data = [1, 2, 3, 4]
pipeline = filter_gen(square_gen(data))
result = list(pipeline)
print("Result:", result)
```

## Output
```
Result: [16]
```

## Explanation
- **Generator Pipelines**: Chains generators to square and filter numbers.
- **Logic**: Squares numbers, then filters those greater than 10.
- **Complexity**: O(n) for n elements.
- **Use Case**: Used for memory-efficient data processing.
- **Best Practice**: Chain generators; handle large datasets; validate pipeline logic.