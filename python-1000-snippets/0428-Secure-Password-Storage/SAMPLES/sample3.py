# sample3.py
# Demonstrates deriving a secure key from a password using scrypt (built-in hashlib).

import hashlib
import os
import base64


def derive_key(password: str, salt: bytes) -> bytes:
    # Using scrypt to derive a key from a password.
    return hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=2**14,
        r=8,
        p=1,
        dklen=32,
    )


def main() -> None:
    password = "S3cureP@ssw0rd"
    salt = os.urandom(16)

    key = derive_key(password, salt)
    print("Derived key (base64):", base64.b64encode(key).decode())

    # Verify by deriving again with the same salt.
    key2 = derive_key(password, salt)
    print("Keys match:", key == key2)

    # Simulate wrong password.
    wrong_key = derive_key("wrong", salt)
    print("Wrong password matches:", key == wrong_key)


if __name__ == "__main__":
    main()
