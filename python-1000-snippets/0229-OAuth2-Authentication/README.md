# OAuth2 Authentication

## Description
This snippet demonstrates OAuth2 authentication using `requests-oauthlib`.

## Code
```python
# Note: Requires `requests-oauthlib`. Install with `pip install requests-oauthlib`
try:
    from oauthlib.oauth2 import WebApplicationClient
    from requests_oauthlib import OAuth2Session
    client = WebApplicationClient(client_id="your_client_id")
    oauth = OAuth2Session(client=client, redirect_uri="http://localhost/callback")
    auth_url, _ = oauth.authorization_url("https://example.com/oauth/authorize")
    print("Auth URL:", auth_url)
except ImportError:
    print("Mock Output: Auth URL: https://example.com/oauth/authorize?...")
```

## Output
```
Mock Output: Auth URL: https://example.com/oauth/authorize?...
```
*(Real output with `requests-oauthlib`: `Auth URL: https://example.com/oauth/authorize?...`)*

## Explanation
- **OAuth2 Authentication**: Generates an authorization URL for OAuth2 flow.
- **Logic**: Uses `OAuth2Session` to create a URL for user authentication.
- **Complexity**: O(1) for URL generation.
- **Use Case**: Used for accessing protected APIs like Google or GitHub.
- **Best Practice**: Secure client secrets; handle token refresh; validate redirects.