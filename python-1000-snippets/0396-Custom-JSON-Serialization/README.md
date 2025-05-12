# Custom JSON Serialization

## Description
This snippet demonstrates custom JSON serialization for a class.

## Code
```python
import json

class CustomObject:
    def __init__(self, name):
        self.name = name
    
    def to_json(self):
        return {"name": self.name}

obj = CustomObject("Test")
print(json.dumps(obj.to_json()))
```

## Output
```
{"name": "Test"}
```

## Explanation
- **Custom JSON Serialization**: Converts a custom object to JSON.
- **Logic**: Defines `to_json` to return a serializable dictionary.
- **Complexity**: O(n) for n attributes.
- **Use Case**: Used for API responses or data storage.
- **Best Practice**: Handle complex objects; use `default` in `json.dumps`; validate output.