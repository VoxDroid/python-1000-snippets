# Symmetric Encryption

## Description
This snippet demonstrates symmetric encryption using `cryptography` with AES.

## Code
```python
# Note: Requires `cryptography`. Install with `pip install cryptography`
try:
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(b"Hello, World!")
    decrypted = cipher.decrypt(encrypted)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted.decode())
except ImportError:
    print("Mock Output: Encrypted: b'gAAAAAB...', Decrypted: Hello, World!")
```

## Output
```
Mock Output: Encrypted: b'gAAAAAB...', Decrypted: Hello, World!
```
*(Real output with `cryptography`: `Encrypted: b'gAAAAAB...`, Decrypted: Hello, World!`)*

## Explanation
- **Symmetric Encryption**: Uses `Fernet` (AES-based) for encryption and decryption.
- **Logic**: Generates a key, encrypts a message, and decrypts it.
- **Complexity**: O(n) for n bytes of data.
- **Use Case**: Used for secure data transmission or storage.
- **Best Practice**: Secure keys; use authenticated encryption; avoid reusing keys.