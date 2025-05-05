# List Creation

## Description
This snippet introduces Python lists, which are ordered, mutable collections used to store multiple items. It shows how to create and manipulate a list.

## Code
```python
fruits = ["apple", "banana", "orange"]
print("Initial list:", fruits)
fruits.append("grape")
print("After appending:", fruits)
fruits[1] = "mango"
print("After modification:", fruits)
```

## Output
```
Initial list: ['apple', 'banana', 'orange']
After appending: ['apple', 'banana', 'orange', 'grape']
After modification: ['apple', 'mango', 'orange', 'grape']
```

## Explanation
- **List Creation**: Lists are defined using square brackets `[]`, with items separated by commas. `fruits` is a list of strings.
- **Mutability**: Lists are mutable, meaning their contents can be changed after creation.
- **Methods**:
  - `append()`: Adds an item to the end of the list.
  - Indexing (`fruits[1]`): Accesses or modifies an item at a specific position (0-based indexing).
- **Use Case**: Lists are used for storing collections like to-do items, user data, or results of computations.
- **Flexibility**: Lists can hold items of different types (e.g., `[1, "hello", True]`), though this is less common.
- **Best Practice**: Use meaningful list names and keep items of the same type for clarity.