# 0429-AES-Encryption Cheatsheet

- Use authenticated encryption modes (GCM, Fernet) to prevent tampering.
- Never reuse a nonce/IV with the same key.

## Fernet (easy, safe)
```py
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
token = cipher.encrypt(b"data")
plain = cipher.decrypt(token)
```

## AES-GCM (manual nonce and associated data)
```py
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
key = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(key)
ct = aesgcm.encrypt(nonce, data, aad)
```

## AES-CBC (requires padding)
```py
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
```

## Notes
- Keep keys secret and rotate them periodically.
- Hardware security modules (HSMs) are recommended for key management.
