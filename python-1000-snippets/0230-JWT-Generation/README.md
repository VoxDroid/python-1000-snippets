# JWT Generation

## Description
This snippet demonstrates generating a JSON Web Token (JWT) using `pyjwt`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — HS256 symmetric signing and verification.
- `sample2.py` — RS256 asymmetric signing (RSA key pair).
- `sample3.py` — ES256 asymmetric signing (ECDSA key pair) with custom headers.

Run any of them with:

```bash
python python-1000-snippets/0230-JWT-Generation/SAMPLES/sample1.py
```

## Output
Each script prints a generated JWT and the decoded claims.

## Explanation
- **JWT Generation**: Signs a JSON payload to create a compact token.
- **Logic**: Uses `pyjwt` to encode with a secret (HS256) or private key (RS256/ES256), then decodes/validates it.
- **Complexity**: O(1) for encoding and decoding.
- **Use Case**: Used for secure authentication or data exchange in APIs.
- **Best Practice**: Set `exp` (expiration) claims, validate algorithms, and protect signing keys.