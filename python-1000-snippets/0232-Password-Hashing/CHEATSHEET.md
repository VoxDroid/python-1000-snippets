# 0232-Password-Hashing Cheatsheet

## Run
```bash
python python-1000-snippets/0232-Password-Hashing/SAMPLES/sample1.py
python python-1000-snippets/0232-Password-Hashing/SAMPLES/sample2.py
python python-1000-snippets/0232-Password-Hashing/SAMPLES/sample3.py
```

## Notes
* Use strong, unique salts and tune work factor for security/performance tradeoffs.
* `bcrypt` uses a built-in salt and work factor; `scrypt` and `pbkdf2_hmac` allow explicit salt control.
* Never store passwords in plaintext; store only hashes.
