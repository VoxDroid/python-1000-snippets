# Nested YAML Handling

## Description
This snippet demonstrates handling nested YAML data using `pyyaml`.

## Code
```python
# Note: Requires `pyyaml`. Install with `pip install pyyaml`
try:
    import yaml
    yaml_data = """
    parent:
      child1: value1
      child2: value2
    """
    data = yaml.safe_load(yaml_data)
    print("YAML Data:", data)
except ImportError:
    print("Mock Output: YAML Data: {'parent': {'child1': 'value1', 'child2': 'value2'}}")
```

## Output
```
Mock Output: YAML Data: {'parent': {'child1': 'value1', 'child2': 'value2'}}
```
*(Real output with `pyyaml`: `YAML Data: {'parent': {'child1': 'value1', 'child2': 'value2'}}`)*

## Explanation
- **Nested YAML Handling**: Parses nested YAML into a Python dictionary.
- **Logic**: Uses `yaml.safe_load` to safely parse YAML string.
- **Complexity**: O(n) for n characters in YAML.
- **Use Case**: Used for configuration files or data exchange.
- **Best Practice**: Use safe loading; validate structure; handle parsing errors.