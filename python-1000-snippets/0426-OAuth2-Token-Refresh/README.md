# OAuth2 Token Refresh

## Description
This snippet demonstrates using the OAuth2 refresh token flow to obtain a new access token.

The examples run a local HTTP server that implements a minimal OAuth2 token endpoint, so no external identity provider is required.

## Requirements
- Python 3.8+
- `flask` (`pip install flask`)
- `requests` (`pip install requests`)

## Samples
- `SAMPLES/sample1.py`: Refresh an access token using a valid refresh token.
- `SAMPLES/sample2.py`: Handle an invalid refresh token response.
- `SAMPLES/sample3.py`: Use the refreshed access token to call a protected endpoint.

## Running
```bash
python python-1000-snippets/0426-OAuth2-Token-Refresh/SAMPLES/sample1.py
python python-1000-snippets/0426-OAuth2-Token-Refresh/SAMPLES/sample2.py
python python-1000-snippets/0426-OAuth2-Token-Refresh/SAMPLES/sample3.py
```

## Notes
- These examples are for demonstration; a real OAuth2 implementation should include client authentication, secure storage of refresh tokens, and HTTPS.
