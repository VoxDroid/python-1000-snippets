# Dictionary Creation

## Description
This snippet demonstrates how to create and initialize a dictionary in Python. Dictionaries are mutable, unordered collections that store key-value pairs, useful for mapping unique keys to values.

## Code
```python
student = {"name": "Alice", "age": 20, "major": "Computer Science"}
print("Dictionary:", student)
```

## Output
```
Dictionary: {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}
```

## Explanation
- **Dictionary Creation**: Dictionaries are defined using curly braces `{}`, with key-value pairs separated by colons (`:`) and pairs separated by commas.
- **Keys and Values**: Keys (e.g., `"name"`) must be unique and immutable (strings, numbers, tuples). Values (e.g., `"Alice"`, `20`) can be of any type.
- **Use Case**: Dictionaries are ideal for storing structured data, like user profiles, configurations, or lookup tables.
- **Mutability**: Dictionaries can be modified (add, update, or remove key-value pairs) after creation.
- **Best Practice**: Use descriptive keys for clarity and avoid using mutable types (like lists) as keys.