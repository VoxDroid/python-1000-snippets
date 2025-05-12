# Map Reduce Pipeline

## Description
This snippet demonstrates a map-reduce pipeline to process data.

## Code
```python
from functools import reduce
data = [1, 2, 3, 4]
mapped = map(lambda x: x**2, data)
reduced = reduce(lambda x, y: x + y, mapped)
print("Sum of Squares:", reduced)
```

## Output
```
Sum of Squares: 30
```

## Explanation
- **Map Reduce Pipeline**: Squares numbers and sums the results.
- **Logic**: Maps data to squares, then reduces to a sum.
- **Complexity**: O(n) for n elements.
- **Use Case**: Used for data processing in distributed systems.
- **Best Practice**: Optimize mappers/reducers; handle large datasets; validate inputs.