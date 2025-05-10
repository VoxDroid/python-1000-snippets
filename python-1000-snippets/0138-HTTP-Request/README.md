# HTTP Request

## Description
This snippet makes a simple HTTP GET request using the `requests` library to fetch a mock API response.

## Code
```python
# Note: Requires `requests`. Install with `pip install requests`
try:
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    print("Response:", response.json())
except ImportError:
    print("Mock Response: {'userId': 1, 'id': 1, 'title': 'Test Post', 'body': 'This is a test'}")
```

## Output
```
Mock Response: {'userId': 1, 'id': 1, 'title': 'Test Post', 'body': 'This is a test'}
```
*(Real output with requests: `Response: {'userId': 1, 'id': 1, 'title': '...', 'body': '...'}`)*

## Explanation
- **HTTP Request**: Uses `requests.get` to fetch JSON data from a mock API endpoint.
- **Mock**: Falls back to a static response if `requests` is unavailable.
- **Complexity**: O(1) for the request (network latency varies).
- **Use Case**: Used in web applications or data fetching.
- **Best Practice**: Handle HTTP errors; use timeouts; validate responses.