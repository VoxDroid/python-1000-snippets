# Asymmetric Encryption

## Description
This snippet demonstrates asymmetric encryption using `cryptography` with RSA.

## Code
```python
# Note: Requires `cryptography`. Install with `pip install cryptography`
try:
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization, hashes  # Import hashes here

    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    
    message = b"Hello, World!"

    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Instantiate SHA256
            algorithm=hashes.SHA256(),                    # Instantiate SHA256
            label=None
        )
    )

    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("Decrypted:", decrypted.decode())

except ImportError:
    print("Mock Output: Decrypted: Hello, World!")
```

## Output
```
Mock Output: Decrypted: Hello, World!
```
*(Real output with `cryptography`: `Decrypted: Hello, World!`)*

## Explanation
- **Asymmetric Encryption**: Uses RSA to encrypt with a public key and decrypt with a private key.
- **Logic**: Generates key pair, encrypts a message, and decrypts it.
- **Complexity**: O(k^3) for RSA operations (k is key size).
- **Use Case**: Used for secure key exchange or authentication.
- **Best Practice**: Use secure padding; protect private keys; use appropriate key sizes.