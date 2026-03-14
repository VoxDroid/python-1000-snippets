# Digital Signature

## Description
This snippet demonstrates creating and verifying a digital signature using `cryptography`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — RSA-PSS signing/verification.
- `sample2.py` — ECDSA signing/verification (secp256r1).
- `sample3.py` — Ed25519 signing/verification.

Run any of them with:

```bash
python python-1000-snippets/0235-Digital-Signature/SAMPLES/sample1.py
```

## Output
Each script prints whether signature verification succeeded.

## Explanation
- **Digital Signature**: Signs a message with a private key and verifies with a public key.
- **Logic**: Sign data with a private key and verify using the corresponding public key.
- **Complexity**: Varies by algorithm; RSA is heavier (O(k^3)), while ECDSA/Ed25519 is faster.
- **Use Case**: Ensure data integrity and authenticity in secure communications.
- **Best Practice**: Protect private keys, validate signatures, and use algorithm-appropriate padding (e.g., PSS for RSA).