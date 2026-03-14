# Password Hashing

## Description
This snippet demonstrates hashing and verifying passwords using `bcrypt`.

## Code
In the `SAMPLES/` folder you will find three examples:

- `sample1.py` — hash and verify a password with `bcrypt`.
- `sample2.py` — hash and verify using PBKDF2-HMAC (standard library).
- `sample3.py` — hash and verify using `scrypt` (standard library).

Run any of them with:

```bash
python python-1000-snippets/0232-Password-Hashing/SAMPLES/sample1.py
```

## Output
Each script prints a password hash and whether verification succeeded.

## Explanation
- **Password Hashing**: Uses slow hashing functions (bcrypt/pbkdf2/scrypt) to store passwords securely.
- **Logic**: Hash a password with a salt and compare hashes for verification.
- **Complexity**: Intentionally slow to defend against brute-force attacks; tune work factors.
- **Use Case**: Securely store passwords in authentication systems.
- **Best Practice**: Use a unique salt per password; use a strong work factor; never store plaintext passwords.