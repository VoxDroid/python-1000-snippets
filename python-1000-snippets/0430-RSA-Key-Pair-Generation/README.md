# RSA Key Pair Generation

## Description
This snippet shows how to generate an RSA key pair, serialize it to PEM files, and use it for signing and encryption.

## Requirements
- Python 3.8+
- `cryptography` (`pip install cryptography`)

## Samples
- `SAMPLES/sample1.py`: Generate an RSA key pair and write PEM files to `temp/`.
- `SAMPLES/sample2.py`: Sign a message with the private key and verify with the public key.
- `SAMPLES/sample3.py`: Encrypt/decrypt a message using RSA OAEP.

## Running
```bash
python python-1000-snippets/0430-RSA-Key-Pair-Generation/SAMPLES/sample1.py
python python-1000-snippets/0430-RSA-Key-Pair-Generation/SAMPLES/sample2.py
python python-1000-snippets/0430-RSA-Key-Pair-Generation/SAMPLES/sample3.py
```

## Notes
- RSA keys should be stored securely (e.g., in a vault or HSM) in production.
- Use appropriate key sizes (2048 bits or higher) for security.
