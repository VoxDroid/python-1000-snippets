# RSA Key Pair Generation

## Description
This snippet demonstrates RSA key pair generation using `cryptography`.

## Code
```python
# Note: Requires `cryptography`. Install with `pip install cryptography`
try:
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives import serialization
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    print("Keys generated")
except ImportError:
    print("Mock Output: Keys generated")
```

## Output
```
Mock Output: Keys generated
```
*(Real output with `cryptography`: `Keys generated`)*

## Explanation
- **RSA Key Pair Generation**: Creates an RSA private-public key pair.
- **Logic**: Uses `cryptography` to generate a 2048-bit key pair.
- **Complexity**: O(1) for key generation (computationally intensive).
- **Use Case**: Used for secure communication or signing.
- **Best Practice**: Secure private key; use appropriate key size; test key usage.