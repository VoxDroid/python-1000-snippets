# Certificate Generation

## Description
This snippet demonstrates generating a self-signed X.509 certificate using `pyOpenSSL`.

## Code
```python
# Note: Requires `pyOpenSSL`. Install with `pip install pyOpenSSL`
try:
    from OpenSSL import crypto
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)
    cert = crypto.X509()
    cert.get_subject().CN = "example.com"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(86400)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, "sha256")
    print("Certificate generated")
except ImportError:
    print("Mock Output: Certificate generated")
```

## Output
```
Mock Output: Certificate generated
```
*(Real output with `pyOpenSSL`: `Certificate generated`)*

## Explanation
- **Certificate Generation**: Creates a self-signed certificate with RSA key.
- **Logic**: Generates a key pair, sets certificate attributes, and signs it.
- **Complexity**: O(k^3) for RSA key generation (k is key size).
- **Use Case**: Used for testing or internal SSL/TLS setups.
- **Best Practice**: Use CA-signed certificates in production; secure private keys; set appropriate validity.