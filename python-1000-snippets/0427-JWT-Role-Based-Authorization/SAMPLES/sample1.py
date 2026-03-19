# sample1.py
# Demonstrates creating and verifying a JWT that includes role claims.

import datetime

import jwt


SECRET = "supersecret"


def create_token(user_id: str, roles: list[str]) -> str:
    payload = {
        "sub": user_id,
        "roles": roles,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")


def verify_token(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=["HS256"])


def main() -> None:
    token = create_token("user123", ["user", "admin"])
    print("JWT:", token)

    decoded = verify_token(token)
    print("Decoded payload:", decoded)

    # Role-based authorization check
    if "admin" in decoded.get("roles", []):
        print("User has admin role")
    else:
        print("User is not an admin")


if __name__ == "__main__":
    main()
