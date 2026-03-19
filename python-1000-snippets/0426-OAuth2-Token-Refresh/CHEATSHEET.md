# 0426 - OAuth2 Token Refresh Cheatsheet

## Quick Facts
- Demonstrates the OAuth2 refresh token flow with a minimal local token endpoint.
- Uses `requests` to call the token endpoint and refresh an access token.

## Run Samples
```bash
python python-1000-snippets/0426-OAuth2-Token-Refresh/SAMPLES/sample1.py
python python-1000-snippets/0426-OAuth2-Token-Refresh/SAMPLES/sample2.py
python python-1000-snippets/0426-OAuth2-Token-Refresh/SAMPLES/sample3.py
```

## Key Concepts
- `grant_type=refresh_token` is used to exchange a refresh token for a new access token.
- The refresh response typically includes `access_token`, `expires_in`, and optionally a new `refresh_token`.
- Protected resources are accessed with the `Authorization: Bearer <access_token>` header.

## Tip
In production, always use HTTPS for token endpoints and never expose refresh tokens in URLs.
