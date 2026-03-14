# 0231-JWT-Validation Cheatsheet

## Run
```bash
python python-1000-snippets/0231-JWT-Validation/SAMPLES/sample1.py
python python-1000-snippets/0231-JWT-Validation/SAMPLES/sample2.py
python python-1000-snippets/0231-JWT-Validation/SAMPLES/sample3.py
```

## Notes
* Always validate the `algorithms` you accept (e.g., allow only HS256/RS256/ES256).
* Handle `jwt.ExpiredSignatureError` and `jwt.InvalidTokenError`.
* Keep signing keys/secrets secure and rotate them as needed.
