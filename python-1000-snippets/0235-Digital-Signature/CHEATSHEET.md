# 0235-Digital-Signature Cheatsheet

## Run
```bash
python python-1000-snippets/0235-Digital-Signature/SAMPLES/sample1.py
python python-1000-snippets/0235-Digital-Signature/SAMPLES/sample2.py
python python-1000-snippets/0235-Digital-Signature/SAMPLES/sample3.py
```

## Notes
* Use RSA-PSS for RSA signatures and Ed25519 for fast, modern signatures.
* Always verify signatures before trusting data.
* Protect private keys and rotate them as needed.
