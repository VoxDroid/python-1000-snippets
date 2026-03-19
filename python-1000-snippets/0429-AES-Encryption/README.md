# AES Encryption

## Description
This snippet demonstrates AES encryption using the `cryptography` library.

## Requirements
- Python 3.8+
- `cryptography` (`pip install cryptography`)

## Samples
- `SAMPLES/sample1.py`: Encrypt and decrypt a message using `Fernet` (AES-128-GCM).
- `SAMPLES/sample2.py`: Encrypt/decrypt using AES-GCM (`AESGCM`) with associated data.
- `SAMPLES/sample3.py`: Encrypt/decrypt using AES-CBC with PKCS7 padding.

## Running
```bash
python python-1000-snippets/0429-AES-Encryption/SAMPLES/sample1.py
python python-1000-snippets/0429-AES-Encryption/SAMPLES/sample2.py
python python-1000-snippets/0429-AES-Encryption/SAMPLES/sample3.py
```

## Notes
- Use authenticated encryption modes (like GCM or Fernet) to prevent tampering.
- Keep encryption keys secret and rotate them as needed.
