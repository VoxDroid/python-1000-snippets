# sample2.py
# Demonstrates hashing and verifying passwords using Argon2 (argon2-cffi).

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def hash_password(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    ph = PasswordHasher()
    try:
        return ph.verify(hashed, password)
    except VerifyMismatchError:
        return False


def main() -> None:
    password = "S3cureP@ssw0rd"
    hashed = hash_password(password)

    print("Password:", password)
    print("Hashed:", hashed)
    print("Password matches:", verify_password(password, hashed))
    print("Wrong password matches:", verify_password("wrong", hashed))


if __name__ == "__main__":
    main()
