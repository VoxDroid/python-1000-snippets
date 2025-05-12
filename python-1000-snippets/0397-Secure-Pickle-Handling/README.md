# Secure Pickle Handling

## Description
This snippet demonstrates secure handling of Python object serialization with `pickle`.

## Code
```python
import pickle

data = {"key": "value"}
serialized = pickle.dumps(data)
deserialized = pickle.loads(serialized)
print("Deserialized:", deserialized)
```

## Output
```
Deserialized: {'key': 'value'}
```

## Explanation
- **Secure Pickle Handling**: Serializes and deserializes Python objects.
- **Logic**: Uses `pickle` to safely handle trusted data.
- **Complexity**: O(n) for n bytes in object.
- **Use Case**: Used for caching or inter-process communication.
- **Best Practice**: Avoid untrusted data; validate inputs; consider alternatives like JSON.