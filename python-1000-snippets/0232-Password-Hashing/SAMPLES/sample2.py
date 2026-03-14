# sample2.py
# Hash and verify a password using PBKDF2-HMAC (standard library).

import hashlib
import os


def hash_password(password: bytes, salt: bytes, iterations: int = 100_000) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password, salt, iterations)


def main():
    password = b'super-secure-password'
    salt = os.urandom(16)

    hashed = hash_password(password, salt)
    print('Salt:', salt.hex())
    print('Hash:', hashed.hex())

    # Verification: compute hash again with the same salt
    verified = hashed == hash_password(password, salt)
    print('Verified:', verified)

    # Wrong password fails
    wrong = hashed == hash_password(b'wrong-password', salt)
    print('Wrong password verified:', wrong)


if __name__ == '__main__':
    main()
