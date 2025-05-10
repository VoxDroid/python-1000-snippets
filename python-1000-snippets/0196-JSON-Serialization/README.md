# JSON Serialization

## Description
This snippet demonstrates serializing and deserializing Python objects to/from JSON using `json`.

## Code
```python
import json

data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print("JSON:", json_string)
parsed_data = json.loads(json_string)
print("Parsed:", parsed_data)
```

## Output
```
JSON: {"name": "Alice", "age": 30}
Parsed: {'name': 'Alice', 'age': 30}
```

## Explanation
- **JSON Serialization**: Uses `json.dumps` to convert a dictionary to JSON and `json.loads` to parse it back.
- **Logic**: Demonstrates round-trip serialization/deserialization.
- **Complexity**: O(n) for n bytes in the data.
- **Use Case**: Used for API communication or data storage.
- **Best Practice**: Handle invalid JSON; use `ensure_ascii=False` for non-ASCII data; validate parsed data.