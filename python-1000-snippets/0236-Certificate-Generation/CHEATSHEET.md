# 0236-Certificate-Generation Cheatsheet

## Run
```bash
python python-1000-snippets/0236-Certificate-Generation/SAMPLES/sample1.py
python python-1000-snippets/0236-Certificate-Generation/SAMPLES/sample2.py
python python-1000-snippets/0236-Certificate-Generation/SAMPLES/sample3.py
```

## Notes
* Use strong key sizes (2048+ bits for RSA, at least 256-bit for EC).
* Protect private keys and store certificates securely.
* CA-signed certs are required for public-facing HTTPS; self-signed are fine for local testing.
