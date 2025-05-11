# JWT Validation

## Description
This snippet demonstrates validating a JSON Web Token (JWT) using `pyjwt`.

## Code
```python
# Note: Requires `pyjwt`. Install with `pip install pyjwt`
try:
    import jwt
    token = jwt.encode({"user_id": 123}, "secret_key", algorithm="HS256")
    decoded = jwt.decode(token, "secret_key", algorithms=["HS256"])
    print("Decoded:", decoded)
except ImportError:
    print("Mock Output: Decoded: {'user_id': 123}")
```

## Output
```
Mock Output: Decoded: {'user_id': 123}
```
*(Real output with `pyjwt`: `Decoded: {'user_id': 123}`)*

## Explanation
- **JWT Validation**: Uses `jwt.decode` to verify and decode a JWT with a secret key.
- **Logic**: Encodes a payload, then decodes it to retrieve the original data.
- **Complexity**: O(1) for decoding.
- **Use Case**: Used for secure authentication in APIs or microservices.
- **Best Practice**: Validate algorithms; handle exceptions (e.g., `InvalidTokenError`); use expiration.