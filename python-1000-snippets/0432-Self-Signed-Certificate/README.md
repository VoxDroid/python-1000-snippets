# Self-Signed Certificate

## Description
This snippet demonstrates generating a self-signed X.509 certificate using `cryptography` and using it for HTTPS.

## Requirements
- Python 3.8+
- `cryptography` (`pip install cryptography`)
- `requests` (`pip install requests`)

## Samples
- `SAMPLES/sample1.py`: Generate a self-signed RSA certificate and write PEM files to `temp/`.
- `SAMPLES/sample2.py`: Load the certificate and print subject/issuer details.
- `SAMPLES/sample3.py`: Start a local HTTPS server using the self-signed certificate and make a request to it.

## Running
```bash
python python-1000-snippets/0432-Self-Signed-Certificate/SAMPLES/sample1.py
python python-1000-snippets/0432-Self-Signed-Certificate/SAMPLES/sample2.py
python python-1000-snippets/0432-Self-Signed-Certificate/SAMPLES/sample3.py
```

## Notes
- Self-signed certificates are useful for testing, but not trusted by browsers or clients.
- For production, obtain certificates from a trusted CA.
