# Digital Signature Verification

## Description
This snippet demonstrates digital signature creation and verification using `cryptography`.

## Code
```python
# Note: Requires `cryptography`. Install with `pip install cryptography`
try:
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    message = b"Message"
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
- **Digital Signature Verification**: Signs and verifies a message using RSA.
- **Logic**: Generates a key pair, signs a message, and verifies the signature.
- **Complexity**: O(1) for signing/verification (computationally intensive).
- **Use Case**: Used for message authenticity in secure communications.
- **Best Practice**: Use secure padding; protect private key; validate inputs.