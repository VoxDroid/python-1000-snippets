# Microservices Communication

## Description
This snippet demonstrates HTTP-based microservice communication.

## Code
```python
# Note: Requires `requests`. Install with `pip install requests`
try:
    import requests
    response = {"status": "mocked"}  # Simulate API call
    print("Service response:", response["status"])
except ImportError:
    print("Mock Output: Service response: mocked")
```

## Output
```
Mock Output: Service response: mocked
```
*(Real output with `requests`: `Service response: <API response>`)*

## Explanation
- **Microservices Communication**: Simulates calling a service via HTTP.
- **Logic**: Mocked response from a service API.
- **Complexity**: O(1) per request (network-dependent).
- **Use Case**: Used in distributed systems for service interaction.
- **Best Practice**: Use retries; secure APIs; monitor latency.