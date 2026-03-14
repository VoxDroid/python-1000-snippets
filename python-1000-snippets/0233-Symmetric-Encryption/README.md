# Symmetric Encryption

## Description
This snippet demonstrates symmetric encryption using `cryptography` with AES.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — symmetric encryption with `Fernet` (AES-128-GCM).
- `sample2.py` — AES-GCM encryption/decryption using low-level primitives.
- `sample3.py` — AES-CBC encryption/decryption with PKCS7 padding.

Run any of them with:

```bash
python python-1000-snippets/0233-Symmetric-Encryption/SAMPLES/sample1.py
```

## Output
Each script prints the cipher text and the decrypted plaintext.

## Explanation
- **Symmetric Encryption**: Encrypts and decrypts data using a shared secret key.
- **Logic**: Derive or generate a symmetric key, encrypt plaintext, then decrypt ciphertext.
- **Complexity**: O(n) for n bytes of data.
- **Use Case**: Encrypt sensitive data at rest or in transit when both parties share a key.
- **Best Practice**: Use authenticated encryption (AES-GCM/Fernet), protect keys, and never reuse nonces/IVs.