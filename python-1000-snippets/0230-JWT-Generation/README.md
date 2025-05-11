# JWT Generation

## Description
This snippet demonstrates generating a JSON Web Token (JWT) using `pyjwt`.

## Code
```python
# Note: Requires `pyjwt`. Install with `pip install pyjwt`
try:
    import jwt
    payload = {"user_id": 123, "role": "admin"}
    token = jwt.encode(payload, "secret_key", algorithm="HS256")
    print("JWT:", token)
except ImportError:
    print("Mock Output: JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
```

## Output
```
Mock Output: JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```
*(Real output with `pyjwt`: `JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...`)*

## Explanation
- **JWT Generation**: Creates a JWT with a payload using `pyjwt`.
- **Logic**: Encodes a dictionary with a secret key using the HS256 algorithm.
- **Complexity**: O(1) for encoding.
- **Use Case**: Used for secure authentication or data exchange in APIs.
- **Best Practice**: Use strong secrets; set expiration; validate tokens on receipt.