# Dictionary Access

## Description
This snippet shows how to access values in a Python dictionary using keys, including handling missing keys with `get()`.

## Code
```python
person = {"name": "Alice", "age": 30, "city": "New York"}
print("Name:", person["name"])
print("Age:", person.get("age"))
print("Country:", person.get("country", "Unknown"))
```

## Output
```
Name: Alice
Age: 30
Country: Unknown
```

## Explanation
- **Accessing Values**: Use square brackets (`dict[key]`) to retrieve a value. Raises `KeyError` if the key doesn't exist.
- **Get Method**: `dict.get(key, default)` returns the value or a default (e.g., `"Unknown"`) if the key is missing.
- **Use Case**: Dictionary access is used for retrieving structured data, like user profiles or settings.
- **Best Practice**: Use `get()` to avoid `KeyError` for optional keys; check keys with `in` if needed.