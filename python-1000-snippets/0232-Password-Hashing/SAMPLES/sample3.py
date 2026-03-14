# sample3.py
# Hash and verify a password using scrypt (standard library).

import hashlib
import os


def hash_password(password: bytes, salt: bytes, n: int = 2**14, r: int = 8, p: int = 1) -> bytes:
    return hashlib.scrypt(password, salt=salt, n=n, r=r, p=p, dklen=64)


def main():
    password = b'super-secure-password'
    salt = os.urandom(16)

    hashed = hash_password(password, salt)
    print('Salt:', salt.hex())
    print('Hash:', hashed.hex())

    verified = hashed == hash_password(password, salt)
    print('Verified:', verified)

    wrong = hashed == hash_password(b'wrong-password', salt)
    print('Wrong password verified:', wrong)


if __name__ == '__main__':
    main()
