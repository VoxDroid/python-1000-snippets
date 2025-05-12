# Secure Password Storage

## Description
This snippet demonstrates secure password hashing using `bcrypt`.

## Code
```python
# Note: Requires `bcrypt`. Install with `pip install bcrypt`
try:
    import bcrypt
    password = "mypassword".encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print("Password hashed:", bcrypt.checkpw(password, hashed))
except ImportError:
    print("Mock Output: Password hashed: True")
```

## Output
```
Mock Output: Password hashed: True
```
*(Real output with `bcrypt`: `Password hashed: True`)*

## Explanation
- **Secure Password Storage**: Hashes and verifies passwords securely.
- **Logic**: Uses `bcrypt` to hash a password and check it.
- **Complexity**: O(1) per hash/check (computationally intensive).
- **Use Case**: Used for user authentication systems.
- **Best Practice**: Use strong salts; adjust work factor; avoid plain text.