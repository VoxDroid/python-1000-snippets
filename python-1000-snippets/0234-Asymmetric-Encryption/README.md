# Asymmetric Encryption

## Description
This snippet demonstrates asymmetric encryption using `cryptography` with RSA.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — RSA-OAEP encrypt/decrypt.
- `sample2.py` — hybrid encryption (RSA-OAEP + AES-GCM).
- `sample3.py` — ECDH-derived key (ECIES-like) + AES-GCM.

Run any of them with:

```bash
python python-1000-snippets/0234-Asymmetric-Encryption/SAMPLES/sample1.py
```

## Output
Each script prints the decrypted plaintext after asymmetric encryption.

## Explanation
- **Asymmetric Encryption**: Uses public/private key pairs to encrypt data or derive shared secrets.
- **Logic**: Generate key pairs, encrypt a symmetric key or message, and decrypt it to recover plaintext.
- **Complexity**: O(k^3) for RSA operations (k is key size).
- **Use Case**: Securely exchange keys or send data when parties do not share a secret.
- **Best Practice**: Use secure padding (OAEP), protect private keys, and use strong key sizes (e.g., 2048+ bits for RSA, P-256/P-384 for EC).