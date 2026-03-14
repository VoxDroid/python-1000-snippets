# 0234-Asymmetric-Encryption Cheatsheet

## Run
```bash
python python-1000-snippets/0234-Asymmetric-Encryption/SAMPLES/sample1.py
python python-1000-snippets/0234-Asymmetric-Encryption/SAMPLES/sample2.py
python python-1000-snippets/0234-Asymmetric-Encryption/SAMPLES/sample3.py
```

## Notes
* Use RSA-OAEP for encryption and key wrapping.
* Hybrid encryption (encrypt symmetric key with RSA or EC) is common for large payloads.
* Protect private keys and use secure storage (e.g., HSM, key vaults).
