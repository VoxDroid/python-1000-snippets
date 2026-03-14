# Certificate Generation

## Description
This snippet demonstrates generating X.509 certificates using `cryptography`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — generate a self-signed certificate.
- `sample2.py` — generate a certificate signing request (CSR).
- `sample3.py` — generate a CA certificate and sign a CSR.

Run any of them with:

```bash
python python-1000-snippets/0236-Certificate-Generation/SAMPLES/sample1.py
```

## Output
Each script prints PEM-encoded private keys, certificates, and/or CSRs.

## Explanation
- **Certificate Generation**: Creates X.509 certificates and CSRs using `cryptography`.
- **Logic**: Generate key pairs, build certificate/CSR objects, and sign them with a private key.
- **Complexity**: RSA key generation is O(k^3) (k is key size); signing is faster.
- **Use Case**: Useful for TLS, code signing, or generating certificates for development.
- **Best Practice**: Use CA-signed certificates in production; protect private keys; set appropriate validity and extensions.