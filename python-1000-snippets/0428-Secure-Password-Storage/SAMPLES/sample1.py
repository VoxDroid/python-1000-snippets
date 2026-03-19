# sample1.py
# Demonstrates hashing and verifying passwords using bcrypt.

import bcrypt


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed)


def main() -> None:
    password = "S3cureP@ssw0rd"
    hashed = hash_password(password)

    print("Password:", password)
    print("Hashed (bytes):", hashed[:20], "...")
    print("Password matches:", verify_password(password, hashed))
    print("Wrong password matches:", verify_password("wrong", hashed))


if __name__ == "__main__":
    main()
