# Digital Signature

## Description
This snippet demonstrates creating and verifying a digital signature using `cryptography`.

## Code
```python
# Note: Requires `cryptography`. Install with `pip install cryptography`
try:
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    message = b"Hello, World!"
    signature = private_key.sign(message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    public_key.verify(signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    print("Signature verified")
except ImportError:
    print("Mock Output: Signature verified")
```

## Output
```
Mock Output: Signature verified
```
*(Real output with `cryptography`: `Signature verified`)*

## Explanation
- **Digital Signature**: Signs a message with a private key and verifies with a public key.
- **Logic**: Uses RSA-PSS to create and verify a signature.
- **Complexity**: O(k^3) for RSA operations (k is key size).
- **Use Case**: Used for data integrity and authenticity in secure communications.
- **Best Practice**: Use secure padding; protect private keys; validate signatures.