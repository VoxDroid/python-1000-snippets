# 0230-JWT-Generation Cheatsheet

## Run
```bash
python python-1000-snippets/0230-JWT-Generation/SAMPLES/sample1.py
python python-1000-snippets/0230-JWT-Generation/SAMPLES/sample2.py
python python-1000-snippets/0230-JWT-Generation/SAMPLES/sample3.py
```

## Notes
* `pyjwt` supports HS256, RS256, ES256, and more.
* Always verify tokens with the expected algorithm and keys.
* Include standard claims like `exp`, `iat`, and `iss` for security.
