# Attribute-Based Access Control

## Description
This snippet demonstrates ABAC using user attributes.

## Code
```python
try:
    user = {"department": "IT", "clearance": "high"}
    def check_access(user, resource):
        return user["department"] == "IT" and user["clearance"] == "high"
    print("Access:", check_access(user, "server"))
except ImportError:
    print("Mock Output: Access: True")
```

## Output
```
Mock Output: Access: True
```
*(Real output: `Access: True`)*

## Explanation
- **Attribute-Based Access Control**: Grants access based on user attributes.
- **Logic**: Checks department and clearance for access.
- **Complexity**: O(1) per check.
- **Use Case**: Used in fine-grained access control systems.
- **Best Practice**: Define clear policies; validate attributes; log decisions.