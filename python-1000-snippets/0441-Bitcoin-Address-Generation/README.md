# Bitcoin Address Generation

## Description
This snippet demonstrates generating a Bitcoin address using `ecdsa`.

## Code
```python
# Note: Requires `ecdsa`. Install with `pip install ecdsa`
try:
    import ecdsa
    import hashlib
    import base58
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b"\x04" + vk.to_string()
    address = base58.b58encode(public_key)[:10]
    print("Address:", address.decode())
except ImportError:
    print("Mock Output: Address: 1A2B3C4D5E")
```

## Output
```
Mock Output: Address: 1A2B3C4D5E
```
*(Real output with `ecdsa`: `Address: <base58 prefix>`)*

## Explanation
- **Bitcoin Address Generation**: Creates a simplified Bitcoin address.
- **Logic**: Generates an ECDSA key pair and encodes the public key.
- **Complexity**: O(1) for generation.
- **Use Case**: Used in cryptocurrency wallets.
- **Best Practice**: Follow Bitcoin standards; secure private keys; validate addresses.