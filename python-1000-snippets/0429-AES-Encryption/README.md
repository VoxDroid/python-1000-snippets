# AES Encryption

## Description
This snippet demonstrates AES encryption using `cryptography`.

## Code
```python
# Note: Requires `cryptography`. Install with `pip install cryptography`
try:
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(b"Secret")
    print("Encrypted:", encrypted[:10])
except ImportError:
    print("Mock Output: Encrypted: b'gAAAAAB...'")
```

## Output
```
Mock Output: Encrypted: b'gAAAAAB...'
```
*(Real output with `cryptography`: `Encrypted: <binary data>`)*

## Explanation
- **AES Encryption**: Encrypts data using AES via `Fernet`.
- **Logic**: Generates a key and encrypts a message.
- **Complexity**: O(n) for n bytes in data.
- **Use Case**: Used for secure data storage or transmission.
- **Best Practice**: Secure key storage; use authenticated encryption; test decryption.