# Dynamic Configuration Loading

## Description
This snippet demonstrates dynamic loading of a JSON configuration file.

## Code
```python
import json

def load_config(file_path="config.json"):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"default": "value"}

config = load_config()
print("Config:", config)
```

## Output
```
Config: {'default': 'value'}
```
*(Real output with `config.json`: Content of the JSON file)*

## Explanation
- **Dynamic Configuration Loading**: Loads settings from a JSON file.
- **Logic**: Reads and parses a JSON file, returns a default if not found.
- **Complexity**: O(n) for n bytes in file.
- **Use Case**: Used for application settings or environment configurations.
- **Best Practice**: Validate config structure; handle file errors; use environment variables.