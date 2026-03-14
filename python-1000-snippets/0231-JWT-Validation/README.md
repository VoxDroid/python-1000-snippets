# JWT Validation

## Description
This snippet demonstrates validating a JSON Web Token (JWT) using `pyjwt`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — decode a valid HS256 token and print claims.
- `sample2.py` — attempt decoding with an incorrect key (invalid signature).
- `sample3.py` — decode a token with an expired `exp` claim.

Run any script with:

```bash
python python-1000-snippets/0231-JWT-Validation/SAMPLES/sample1.py
```

## Output
Each script prints the decoded claims or a validation error.

## Explanation
- **JWT Validation**: Uses `jwt.decode` to verify signature and claims.
- **Logic**: Decode with the expected key and algorithms, and handle errors for invalid or expired tokens.
- **Complexity**: O(1) for decoding.
- **Use Case**: Used for secure authentication in APIs or microservices.
- **Best Practice**: Validate `algorithms`, check `exp`, and enforce `iss`/`aud` when applicable.