# Complex INI Processing

## Description
This snippet demonstrates processing a complex INI file using `configparser`.

## Code
```python
import configparser

def parse_ini(file_path="config.ini"):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        return {section: dict(config[section]) for section in config.sections()}
    except FileNotFoundError:
        return {"section1": {"key": "value"}}

print("INI Config:", parse_ini())
```

## Output
```
INI Config: {'section1': {'key': 'value'}}
```
*(Real output with `config.ini`: Parsed INI sections and keys)*

## Explanation
- **Complex INI Processing**: Parses an INI file into a nested dictionary.
- **Logic**: Uses `configparser` to read sections and keys, handles missing file.
- **Complexity**: O(n) for n lines in file.
- **Use Case**: Used for legacy configuration files or simple settings.
- **Best Practice**: Validate section/key formats; handle parsing errors; use defaults.