# 0428-Secure-Password-Storage Cheatsheet

- Use a strong hashing function (bcrypt, Argon2) for password storage.
- Never store plaintext passwords.
- Store the full hash string (it usually includes salt/work factor metadata).

## Bcrypt example
```py
import bcrypt
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
bcrypt.checkpw(password.encode(), hashed)
```

## Argon2 example
```py
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash(password)
ph.verify(hash, password)
```

## scrypt (KDF) example
```py
import hashlib, os
salt = os.urandom(16)
key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1)
```

## Notes
- Bcrypt and Argon2 are purpose-built for password hashing.
- Use a unique salt per password.
- Adjust work factors (cost) based on your hardware and desired latency.
