# 0431-Digital-Signature-Verification Cheatsheet

- Use public-key cryptography to sign and verify data.
- Signing uses a private key; verification uses the corresponding public key.
- Common algorithms: RSA-PSS, ECDSA.

## RSA signing (PSS + SHA256)
```py
signature = private_key.sign(
    data,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)
```

## Verification
```py
public_key.verify(signature, data, padding.PSS(...), hashes.SHA256())
```

## Notes
- Do not use deterministic padding (e.g., PKCS1v15) for signatures if you can avoid it.
- Protect the private key; it should never leave the server.
