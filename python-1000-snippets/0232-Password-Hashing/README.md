# Password Hashing

## Description
This snippet demonstrates hashing and verifying passwords using `bcrypt`.

## Code
```python
# Note: Requires `bcrypt`. Install with `pip install bcrypt`
try:
    import bcrypt
    password = "mypassword".encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    print("Hashed:", hashed)
    print("Verified:", bcrypt.checkpw(password, hashed))
except ImportError:
    print("Mock Output: Hashed: b'$2b$12$...', Verified: True")
```

## Output
```
Mock Output: Hashed: b'$2b$12$...', Verified: True
```
*(Real output with `bcrypt`: `Hashed: b'$2b$12$...`, Verified: True`)*

## Explanation
- **Password Hashing**: Uses `bcrypt.hashpw` to hash a password and `checkpw` to verify it.
- **Logic**: Generates a salted hash and checks if the password matches.
- **Complexity**: O(1) for hashing/verification (cost factor affects runtime).
- **Use Case**: Used for secure password storage in authentication systems.
- **Best Practice**: Use strong salts; adjust work factor; store hashes securely.