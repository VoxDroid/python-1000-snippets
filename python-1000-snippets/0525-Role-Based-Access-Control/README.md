# Role-Based Access Control

## Description
This snippet demonstrates RBAC using a simple dictionary.

## Code
```python
try:
    roles = {"admin": ["read", "write"], "user": ["read"]}
    def check_access(user_role, action):
        return action in roles.get(user_role, [])
    print("Access:", check_access("admin", "write"))
except ImportError:
    print("Mock Output: Access: True")
```

## Output
```
Mock Output: Access: True
```
*(Real output: `Access: True`)*

## Explanation
- **Role-Based Access Control**: Checks permissions based on roles.
- **Logic**: Validates if an action is allowed for a role.
- **Complexity**: O(1) per check.
- **Use Case**: Used in secure systems for access management.
- **Best Practice**: Centralize roles; validate inputs; log access attempts.