# API Documentation

## Description
This snippet demonstrates generating API documentation for an e-commerce order endpoint using `fastapi` and its built-in Swagger UI.

## Code
```python
# API documentation with fastapi
# Note: Requires `fastapi`. Install with `pip install fastapi`
try:
    from fastapi import FastAPI

    # Initialize FastAPI app
    app = FastAPI(title="E-commerce API")

    # Define order endpoint
    @app.get("/order/{order_id}", summary="Get order details")
    async def get_order(order_id: str):
        """Retrieve order details by ID.
        
        Args:
            order_id: Unique order identifier
        Returns:
            Order details
        """
        return {"order_id": order_id, "amount": 99.99}

    # Simulate generating Swagger docs
    print("API docs generated: Available at /docs")
except ImportError:
    print("Mock Output: API docs generated: Available at /docs")
```

## Output
```
Mock Output: API docs generated: Available at /docs
```
*(Real output with `fastapi`: `API docs generated: Available at /docs`)*

## Explanation
- **Purpose**: API documentation provides interactive, user-friendly documentation for API endpoints, aiding developers and consumers.
- **Real-World Use Case**: In an e-commerce system, documenting the order endpoint helps external services integrate with the platform.
- **Code Breakdown**:
  - A `FastAPI` app defines a `/order/{order_id}` endpoint.
  - The endpoint includes a docstring and metadata for Swagger UI.
  - The snippet simulates generating interactive docs at `/docs`.
- **Challenges**: Keeping docs in sync with code, documenting complex APIs, and ensuring clarity for external users.
- **Integration**: Works with Documentation Generation (Snippet 619) and CI/CD Pipeline (Snippet 624) for automated doc deployment.
- **Complexity**: O(1) for generating endpoint docs.
- **Best Practices**: Use clear descriptions, include examples, automate doc generation, and host docs publicly.