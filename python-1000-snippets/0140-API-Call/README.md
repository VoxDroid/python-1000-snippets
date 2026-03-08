# API Call

## Description
This snippet makes a REST API call to a public endpoint to retrieve JSON data.

## Code
```python
# Note: Requires `requests`. Install with `pip install requests`
try:
    import requests
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
        response.raise_for_status()
        print("User:", response.json())
    except requests.RequestException as e:
        print("HTTP error or network issue:", e)
except ImportError:
    print("Mock User: {'id': 1, 'name': 'Leanne Graham', 'email': 'Sincere@april.biz'}")
```

## Output
```
Mock User: {'id': 1, 'name': 'Leanne Graham', 'email': 'Sincere@april.biz'}
```
*(Real output with requests: `User: {'id': 1, 'name': 'Leanne Graham', ...}`; network errors will be printed.)*

## Explanation
- **API Call**: Fetches user data from a mock REST API using `requests.get`.
- **Mock**: Returns a static response if `requests` is unavailable.
- **Complexity**: O(1) for the request (network latency varies).
- **Use Case**: Used in applications integrating with external services.
- **Best Practice**: Handle API rate limits; validate JSON schema; use authentication if required.