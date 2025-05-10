# API Call

## Description
This snippet makes a REST API call to a mock endpoint to retrieve JSON data.

## Code
```python
# Note: Requires `requests`. Install with `pip install requests`
try:
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    print("User:", response.json())
except ImportError:
    print("Mock User: {'id': 1, 'name': 'Leanne Graham', 'email': 'Sincere@april.biz'}")
```

## Output
```
Mock User: {'id': 1, 'name': 'Leanne Graham', 'email': 'Sincere@april.biz'}
```
*(Real output with requests: `User: {'id': 1, 'name': 'Leanne Graham', ...}`)*

## Explanation
- **API Call**: Fetches user data from a mock REST API using `requests.get`.
- **Mock**: Returns a static response if `requests` is unavailable.
- **Complexity**: O(1) for the request (network latency varies).
- **Use Case**: Used in applications integrating with external services.
- **Best Practice**: Handle API rate limits; validate JSON schema; use authentication if required.