# Dictionary Length

## Description
This snippet demonstrates how to find the number of key-value pairs in a dictionary using the `len()` function.

## Code
```python
person = {"name": "Alice", "age": 25, "city": "Boston"}
length = len(person)
print("Dictionary length:", length)
```

## Output
```
Dictionary length: 3
```

## Explanation
- **len() Function**: Returns the number of key-value pairs in a dictionary.
- **Use Case**: Dictionary length is used for validation, iteration, or checking data completeness.
- **Applicability**: `len()` works on any collection type, including dictionaries.
- **Best Practice**: Use `len()` to check dictionary size before operations like iteration.