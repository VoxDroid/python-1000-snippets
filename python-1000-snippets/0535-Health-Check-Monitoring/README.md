# Health Check Monitoring

## Description
This snippet demonstrates a simple health check endpoint using `flask`.

## Code
```python
# Note: Requires `flask`. Install with `pip install flask`
try:
    from flask import Flask
    app = Flask(__name__)
    @app.route("/health")
    def health():
        return {"status": "healthy"}
    print("Health check endpoint configured")
except ImportError:
    print("Mock Output: Health check endpoint configured")
```

## Output
```
Mock Output: Health check endpoint configured
```
*(Real output with `flask`: `Health check endpoint configured`)*

## Explanation
- **Health Check Monitoring**: Provides a health status endpoint.
- **Logic**: Returns a JSON status response.
- **Complexity**: O(1) per request.
- **Use Case**: Used in microservices for monitoring.
- **Best Practice**: Include metrics; secure endpoints; automate checks.