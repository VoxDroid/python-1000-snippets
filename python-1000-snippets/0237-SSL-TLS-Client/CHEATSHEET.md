# 0237-SSL-TLS-Client Cheatsheet

## Run
```bash
python python-1000-snippets/0237-SSL-TLS-Client/SAMPLES/sample1.py
python python-1000-snippets/0237-SSL-TLS-Client/SAMPLES/sample2.py
python python-1000-snippets/0237-SSL-TLS-Client/SAMPLES/sample3.py
```

## Notes
* Use `ssl.create_default_context()` for client connections.
* For self-signed servers, load the CA certificate into the context (or disable verification only for testing).
* For mutual TLS, configure both client and server certificates.
