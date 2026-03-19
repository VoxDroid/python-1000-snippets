# TLS Server Implementation

## Description
This snippet demonstrates building a TLS server using Python's `ssl` module and a self-signed certificate.

## Requirements
- Python 3.8+
- `cryptography` (`pip install cryptography`)
- `requests` (`pip install requests`)

## Samples
- `SAMPLES/sample1.py`: Create a self-signed certificate and start an HTTPS server; connect to it with a trusted client.
- `SAMPLES/sample2.py`: Create an SSL client context that trusts a self-signed certificate and connect to a running TLS server.
- `SAMPLES/sample3.py`: Demonstrate mutual TLS (mTLS) where the server requires a client certificate.

## Running
```bash
python python-1000-snippets/0433-TLS-Server-Implementation/SAMPLES/sample1.py
python python-1000-snippets/0433-TLS-Server-Implementation/SAMPLES/sample2.py
python python-1000-snippets/0433-TLS-Server-Implementation/SAMPLES/sample3.py
```

## Notes
- Self-signed certificates are suitable for testing but not for production.
- Use a CA-signed certificate and proper certificate verification in production.
