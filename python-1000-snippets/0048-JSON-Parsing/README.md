# JSON Parsing

## Description
This snippet demonstrates parsing a JSON string into a Python dictionary using the `json` module, allowing easy access to structured data.

## Code
```python
import json

json_string = '{"name": "Alice", "age": 25, "city": "Boston"}'
data = json.loads(json_string)
print("Parsed data:", data)
print("Name:", data["name"])
```

## Output
```
Parsed data: {'name': 'Alice', 'age': 25, 'city': 'Boston'}
Name: Alice
```

## Explanation
- **json.loads()**: Converts a JSON-formatted string into a Python object (usually a dictionary).
- **JSON**: A lightweight data format using key-value pairs, similar to Python dictionaries.
- **Use Case**: JSON parsing is used for APIs, configuration files, or data exchange.
- **Error Handling**: Invalid JSON raises `json.JSONDecodeError`, which should be caught in production.
- **Best Practice**: Validate JSON input and use `json.load()` for reading JSON from files.