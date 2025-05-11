# REST API Client

## Description
This snippet demonstrates a REST API client using `requests` to fetch data.

## Code
```python
# Note: Requires `requests`. Install with `pip install requests`
try:
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    print("User:", response.json()["name"])
except ImportError:
    print("Mock Output: User: Leanne Graham")
```

## Output
```
Mock Output: User: Leanne Graham
```
*(Real output with `requests`: `User: Leanne Graham`)*

## Explanation
- **REST API Client**: Fetches user data from a public API using `requests.get`.
- **Logic**: Sends a GET request and extracts the user’s name from JSON.
- **Complexity**: O(1) for the request (network latency varies).
- **Use Case**: Used for integrating with web APIs.
- **Best Practice**: Handle HTTP errors; use timeouts; validate JSON responses.