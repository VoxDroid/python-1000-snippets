# 0427-JWT-Role-Based-Authorization Cheatsheet

- Use `pyjwt` to **encode** and **decode** JWTs.
- Store role claims in a claim like `roles` (list of strings).
- Always verify tokens with the same `secret` and algorithm.
- Validate expiration (`exp`) and required roles before granting access.

## Quick patterns
```py
import jwt

SECRET = "secret"

payload = jwt.decode(token, SECRET, algorithms=["HS256"])
roles = payload.get("roles", [])
if "admin" in roles:
    # allow admin action
```

## Notes
- In production, use a strong secret and rotate keys.
- Do not trust unsigned tokens.
