# JWT Role-Based Authorization

## Description
This snippet demonstrates JWT role-based authorization using `pyjwt`.

## Code
```python
# Note: Requires `pyjwt`. Install with `pip install pyjwt`
try:
    import jwt
    token = jwt.encode({"role": "admin"}, "secret", algorithm="HS256")
    decoded = jwt.decode(token, "secret", algorithms=["HS256"])
    print("Role:", decoded["role"])
except ImportError:
    print("Mock Output: Role: admin")
```

## Output
```
Mock Output: Role: admin
```
*(Real output with `pyjwt`: `Role: admin`)*

## Explanation
- **JWT Role-Based Authorization**: Encodes and decodes a JWT with role info.
- **Logic**: Creates a JWT with a role and verifies it.
- **Complexity**: O(1) per encode/decode.
- **Use Case**: Used for secure API authorization.
- **Best Practice**: Use strong secrets; validate claims; handle expiration.