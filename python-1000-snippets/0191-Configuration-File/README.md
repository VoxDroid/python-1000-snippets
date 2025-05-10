# Configuration File

## Description
This snippet demonstrates reading a simple configuration file using Python’s `configparser`.

## Directory Structure
```
config/
└── settings.ini
```

## Code
```python
# config/settings.ini
[Database]
host=localhost
port=5432

# main.py
import configparser

config = configparser.ConfigParser()
config.read("config/settings.ini")
print("Database Host:", config["Database"]["host"])
print("Database Port:", config["Database"]["port"])
```

## Output
```
Database Host: localhost
Database Port: 5432
```

## Explanation
- **Configuration File**: Uses `configparser` to read key-value pairs from `settings.ini`.
- **Logic**: Parses the INI file and accesses values using section and key names.
- **Complexity**: O(n) for parsing n lines in the file.
- **Use Case**: Used for storing application settings like database credentials.
- **Best Practice**: Validate config values; use environment variables for sensitive data; handle missing files.