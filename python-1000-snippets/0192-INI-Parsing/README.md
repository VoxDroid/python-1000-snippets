# INI Parsing

## Description
This snippet demonstrates parsing an INI file with multiple sections using `configparser`.

## Code
```python
import configparser

# Sample INI content (normally in a file)
ini_content = """
[Server]
host=127.0.0.1
port=8080

[Database]
host=localhost
user=admin
"""

config = configparser.ConfigParser()
config.read_string(ini_content)
print("Server Host:", config["Server"]["host"])
print("Database User:", config["Database"]["user"])
```

## Output
```
Server Host: 127.0.0.1
Database User: admin
```

## Explanation
- **INI Parsing**: Uses `configparser.read_string` to parse INI-formatted text.
- **Logic**: Accesses values from different sections (`Server`, `Database`).
- **Complexity**: O(n) for parsing n lines.
- **Use Case**: Used for configuration management in applications.
- **Best Practice**: Handle missing sections/keys; use `read` for files; validate parsed data.