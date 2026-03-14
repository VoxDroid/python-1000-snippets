# SSL/TLS Client

## Description
This snippet demonstrates an SSL/TLS client using `ssl` and `socket`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — connect to a local TLS server and fetch an HTTP response.
- `sample2.py` — validate a server certificate using a custom CA.
- `sample3.py` — demonstrate mutual TLS (mTLS) where client and server authenticate each other.

Run any of them with:

```bash
python python-1000-snippets/0237-SSL-TLS-Client/SAMPLES/sample1.py
```

## Output
Each script starts a local TLS server and prints the HTTP response received from it.

## Explanation
- **SSL/TLS Client**: Uses Python's `ssl` module to establish a secure connection and validate certificates.
- **Logic**: Wrap a socket with an `SSLContext`, perform the TLS handshake, then read/write data.
- **Complexity**: O(1) for connection (network latency varies).
- **Use Case**: Used for secure communication with web servers.
- **Best Practice**: Verify certificates, handle SSL errors, and use strong cipher suites; for production, prefer higher-level libraries like `requests` or `httpx` with certificate pinning.