# sample3.py
# Demonstrates handling expired JWTs and refreshing tokens in a simple flow.

import datetime

import jwt


SECRET = "supersecret"


def create_token(user_id: str, roles: list[str], expires_in: int) -> str:
    payload = {
        "sub": user_id,
        "roles": roles,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in),
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")


def verify_token(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=["HS256"])


def main() -> None:
    # Create a token that expires immediately.
    expired = create_token("user123", ["user"], expires_in=-1)
    print("Expired token created")

    try:
        verify_token(expired)
        print("Expired token unexpectedly verified")
    except jwt.ExpiredSignatureError:
        print("Expired token correctly rejected")

    # Create a valid token and verify it.
    valid = create_token("user123", ["user", "admin"], expires_in=60)
    decoded = verify_token(valid)
    print("Valid token decoded roles:", decoded.get("roles"))

    # Simulate an endpoint that requires admin role.
    if "admin" in decoded.get("roles", []):
        print("Admin access granted")
    else:
        print("Admin access denied")


if __name__ == "__main__":
    main()
