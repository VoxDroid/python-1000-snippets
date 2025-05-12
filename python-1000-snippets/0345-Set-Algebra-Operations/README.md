# Set Algebra Operations

## Description
This snippet demonstrates set operations like union and intersection.

## Code
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
union = set1 | set2
intersection = set1 & set2
print("Union:", union, "Intersection:", intersection)
```

## Output
```
Union: {1, 2, 3, 4} Intersection: {2, 3}
```

## Explanation
- **Set Algebra Operations**: Performs union and intersection on two sets.
- **Logic**: Uses Python’s set operators to combine or find common elements.
- **Complexity**: O(n + m) for n, m elements in sets.
- **Use Case**: Used for data filtering or membership testing.
- **Best Practice**: Handle empty sets; use frozensets for immutability; validate inputs.