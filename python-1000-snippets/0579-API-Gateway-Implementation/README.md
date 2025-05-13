# API Gateway Implementation

## Description
This snippet demonstrates a simple API gateway using `fastapi`.

## Code
```python
# Note: Requires `fastapi`. Install with `pip install fastapi`
try:
    from fastapi import FastAPI
    app = FastAPI()
    @app.get("/proxy")
    def proxy():
        return {"service": "routed"}
    print("API gateway configured")
except ImportError:
    print("Mock Output: API gateway configured")
```

## Output
```
Mock Output: API gateway configured
```
*(Real output with `fastapi`: `API gateway configured`)*

## Explanation
- **API Gateway Implementation**: Routes requests to services.
- **Logic**: Sets up a FastAPI endpoint as a proxy.
- **Complexity**: O(1) per request.
- **Use Case**: Used in microservices for centralized routing.
- **Best Practice**: Add authentication; rate limit; log requests.