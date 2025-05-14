# Hardware Security Module

## Description
This snippet demonstrates a Hardware Security Module (HSM) for an e-commerce platform, simulating secure key storage and encryption.

## Code
```python
# Hardware Security Module for secure key storage
# Note: Requires `cryptography`. Install with `pip install cryptography`
try:
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import rsa, padding

    # HSM model
    class SecureHSM:
        def __init__(self):
            # Initialize simulated HSM with key
            self.key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

        def encrypt(self, data: str) -> bytes:
            # Encrypt data (simulated)
            return self.key.public_key().encrypt(
                data.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

    # Simulate HSM encryption
    def encrypt_data(data_list: list) -> list:
        # Encrypt data with HSM
        hsm = SecureHSM()
        return [hsm.encrypt(d) for d in data_list]

    # Example usage
    data_list = ["payment_info"]
    results = encrypt_data(data_list)
    print("HSM result:", [len(r) for r in results])  # Output length of encrypted data

except ImportError:
    print("Mock Output: HSM result: [256]")
```

## Output
```
Mock Output: HSM result: [256]
```
*(Real output with `cryptography`: `HSM result: [<variable lengths>]`)*

## Explanation
- **Purpose**: A Hardware Security Module securely stores keys and performs cryptographic operations, ensuring data protection.
- **Real-World Use Case**: In an e-commerce platform, it encrypts payment details, securing transactions.
- **Code Breakdown**:
  - The `SecureHSM` class simulates an HSM with RSA.
  - The `encrypt` method encrypts data.
  - The `encrypt_data` function simulates encryption.
- **Challenges**: Hardware integration, key management, and performance.
- **Integration**: Works with Trusted Execution Environment (Snippet 849) and Secure Code Signing (Snippet 848) for security tasks.
- **Complexity**: O(n) for n data bytes.
- **Best Practices**: Use real HSMs, validate encryption, and secure keys.
- **Extensions**: Support HSM APIs or integrate with payment systems.