# 0430-RSA-Key-Pair-Generation Cheatsheet

- Use `cryptography` to generate RSA keys.
- Store private keys securely (never commit to source control).
- Use public keys to verify signatures or encrypt small payloads.

## Generate keys
```py
from cryptography.hazmat.primitives.asymmetric import rsa
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
```

## Serialize to PEM
```py
from cryptography.hazmat.primitives import serialization
pem = key.private_bytes(...)
```

## Load a key
```py
from cryptography.hazmat.primitives import serialization
private_key = serialization.load_pem_private_key(pem, password=None)
```

## Notes
- RSA encryption with OAEP is limited to small plaintexts (key_size/8 - padding).
- For larger data, use hybrid encryption: encrypt with a symmetric key and encrypt that key with RSA.
