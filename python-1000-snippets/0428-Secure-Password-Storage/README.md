# Secure Password Storage

## Description
This snippet demonstrates secure password hashing and verification using modern algorithms (bcrypt, Argon2, and scrypt).

## Requirements
- Python 3.8+
- `bcrypt` (`pip install bcrypt`)
- `argon2-cffi` (`pip install argon2-cffi`)

## Samples
- `SAMPLES/sample1.py`: Hash and verify passwords using bcrypt.
- `SAMPLES/sample2.py`: Hash and verify passwords using Argon2.
- `SAMPLES/sample3.py`: Derive a key from a password using scrypt.

## Running
```bash
python python-1000-snippets/0428-Secure-Password-Storage/SAMPLES/sample1.py
python python-1000-snippets/0428-Secure-Password-Storage/SAMPLES/sample2.py
python python-1000-snippets/0428-Secure-Password-Storage/SAMPLES/sample3.py
```

## Notes
- Use a well-tested library (bcrypt, Argon2) for password hashing; avoid custom crypto.
- Store only the hash (and salt if applicable), never plaintext passwords.
