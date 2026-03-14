# 0233-Symmetric-Encryption Cheatsheet

## Run
```bash
python python-1000-snippets/0233-Symmetric-Encryption/SAMPLES/sample1.py
python python-1000-snippets/0233-Symmetric-Encryption/SAMPLES/sample2.py
python python-1000-snippets/0233-Symmetric-Encryption/SAMPLES/sample3.py
```

## Notes
* Use authenticated encryption (AES-GCM or Fernet) to prevent tampering.
* Keep keys secret and rotate regularly.
* For AES-GCM, never reuse a key+nonce pair.
