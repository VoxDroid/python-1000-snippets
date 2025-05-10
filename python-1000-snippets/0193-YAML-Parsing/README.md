# YAML Parsing

## Description
This snippet demonstrates parsing a YAML file using `pyyaml`.

## Code
```python
# Note: Requires `pyyaml`. Install with `pip install pyyaml`
import yaml

# Sample YAML content (normally in a file)
yaml_content = """
server:
  host: 127.0.0.1
  port: 8080
database:
  host: localhost
  user: admin
"""

try:
    config = yaml.safe_load(yaml_content)
    print("Server Host:", config["server"]["host"])
    print("Database User:", config["database"]["user"])
except ImportError:
    print("Mock Output: Server Host: 127.0.0.1, Database User: admin")
```

## Output
```
Mock Output: Server Host: 127.0.0.1, Database User: admin
```
*(Real output with `pyyaml`: `Server Host: 127.0.0.1, Database User: admin`)*

## Explanation
- **YAML Parsing**: Uses `yaml.safe_load` to parse YAML into a Python dictionary.
- **Logic**: Accesses nested values using dictionary keys.
- **Complexity**: O(n) for parsing n lines.
- **Use Case**: Used for complex configuration files in DevOps or applications.
- **Best Practice**: Use `safe_load` to avoid arbitrary code execution; validate YAML structure.