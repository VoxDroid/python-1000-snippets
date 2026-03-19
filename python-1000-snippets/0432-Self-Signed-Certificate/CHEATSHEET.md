# 0432-Self-Signed-Certificate Cheatsheet

- Use `cryptography` to generate self-signed X.509 certificates for testing.
- Self-signed certificates are not trusted by default (browsers/clients will warn).

## Generate a self-signed cert
```py
from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa

key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(subject)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.datetime.utcnow())
    .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    .sign(key, hashes.SHA256())
)
```

## Load a certificate
```py
from cryptography import x509
cert = x509.load_pem_x509_certificate(pem_data)
```

## Notes
- For production, obtain certificates from trusted CAs.
- For local testing, configure clients to trust the self-signed certificate.
