# Self-Signed Certificate

## Description
This snippet demonstrates creating a self-signed certificate using `cryptography`.

## Code
```python
# Note: Requires `cryptography`. Install with `pip install cryptography`
try:
    from cryptography import x509
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization, hashes
    from cryptography.x509.oid import NameOID
    import datetime
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "example.com")])
    cert = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(datetime.datetime.utcnow()).not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=10)).add_extension(x509.SubjectAlternativeName([x509.DNSName("example.com")]), critical=False).sign(key, hashes.SHA256())
    print("Certificate created")
except ImportError:
    print("Mock Output: Certificate created")
```

## Output
```
Mock Output: Certificate created
```
*(Real output with `cryptography`: `Certificate created`)*

## Explanation
- **Self-Signed Certificate**: Generates a self-signed X.509 certificate.
- **Logic**: Creates a key pair and signs a certificate with basic attributes.
- **Complexity**: O(1) for certificate generation.
- **Use Case**: Used for testing or internal TLS setups.
- **Best Practice**: Use for non-production; secure private key; include necessary extensions.