# JWT Role-Based Authorization

## Description
This snippet demonstrates creating and verifying JWTs that include role claims using `pyjwt`.

## Requirements
- Python 3.8+
- `pyjwt` (`pip install pyjwt`)

## Samples
- `SAMPLES/sample1.py`: Create a JWT with roles, decode it, and check for required roles.
- `SAMPLES/sample2.py`: Enforce a role requirement and deny access if the role is missing.
- `SAMPLES/sample3.py`: Show handling of expired tokens and role-based access.

## Running
```bash
python python-1000-snippets/0427-JWT-Role-Based-Authorization/SAMPLES/sample1.py
python python-1000-snippets/0427-JWT-Role-Based-Authorization/SAMPLES/sample2.py
python python-1000-snippets/0427-JWT-Role-Based-Authorization/SAMPLES/sample3.py
```

## Notes
- JWTs are signed using HMAC-SHA256 (HS256) with a shared secret.
- Always validate `exp` and other claims in production.
