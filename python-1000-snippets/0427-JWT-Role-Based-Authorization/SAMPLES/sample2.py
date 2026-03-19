# sample2.py
# Demonstrates verifying JWT role claims and enforcing role-based access.

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


def require_role(token: str, role: str) -> bool:
    decoded = verify_token(token)
    return role in decoded.get("roles", [])


def main() -> None:
    # Create a token for a user with only the "user" role.
    token = create_token("user123", ["user"])
    print("Token:", token)

    print("Has user role?", require_role(token, "user"))
    print("Has admin role?", require_role(token, "admin"))

    # Simulate an endpoint that requires admin privileges.
    if require_role(token, "admin"):
        print("Access granted to admin endpoint")
    else:
        print("Access denied: admin role required")


if __name__ == "__main__":
    main()
