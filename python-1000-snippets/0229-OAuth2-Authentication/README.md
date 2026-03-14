# OAuth2 Authentication

## Description
This snippet demonstrates an OAuth2 client credentials flow against a local OAuth2 token endpoint.

## Setup
The sample script starts a minimal Flask-based OAuth2 token endpoint at `http://localhost:5001/token` and a protected resource at `/resource`.
It uses a fixed client ID/secret and returns a static access token.

## Code
Run any of the sample scripts:

```bash
python python-1000-snippets/0229-OAuth2-Authentication/SAMPLES/sample1.py
python python-1000-snippets/0229-OAuth2-Authentication/SAMPLES/sample2.py
python python-1000-snippets/0229-OAuth2-Authentication/SAMPLES/sample3.py
```

### What each sample demonstrates
- `sample1.py`: client credentials flow using `requests`
- `sample2.py`: client credentials flow using `requests-oauthlib`
- `sample3.py`: token refresh exercise (short-lived token + refresh token)

## Output
The sample prints the token response and the protected resource response.

## Explanation
- **OAuth2**: Demonstrates the client credentials grant where the client exchanges its credentials for an access token.
- **Logic**: Request a token from `/token`, then use it to access a protected endpoint.
- **Use Case**: Service-to-service authentication where user interaction is not required.
- **Best Practice**: Use secure storage for client secrets and use HTTPS for token endpoints.
