# Hash Table

## Description
This snippet implements a simple hash table using a list with chaining (linked lists) to handle collisions.

## Code
```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

ht = HashTable()
ht.insert("apple", 5)
ht.insert("banana", 8)
print("Value for 'apple':", ht.get("apple"))
print("Value for 'banana':", ht.get("banana"))
```

## Output
```
Value for 'apple': 5
Value for 'banana': 8
```

## Explanation
- **Hash Table**: Maps keys to values using a hash function; handles collisions with chaining (lists).
- **Methods**:
  - `_hash`: Computes the index for a key.
  - `insert`: Adds or updates a key-value pair.
  - `get`: Retrieves the value for a key.
- **Complexity**: Average O(1) for insert/get; worst-case O(n) with many collisions.
- **Use Case**: Used in dictionaries, caches, or lookup tables.
- **Best Practice**: Use Python’s `dict` for production; implement resizing for scalability.