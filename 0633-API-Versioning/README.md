# API Versioning

## Description
This snippet demonstrates API versioning for an e-commerce order endpoint using `fastapi`, supporting multiple API versions.

## Code
```python
# API versioning for an e-commerce order endpoint
# Note: Requires `fastapi`. Install with `pip install fastapi`
try:
    from fastapi import FastAPI
    from fastapi.routing import APIRouter

    # Initialize FastAPI app
    app = FastAPI()

    # Version 1 router
    v1_router = APIRouter(prefix="/v1")

    @v1_router.get("/order/{order_id}")
    async def get_order_v1(order_id: str):
        # Return order details for v1
        return {"order_id": order_id, "amount": 99.99}

    # Version 2 router with status
    v2_router = APIRouter(prefix="/v2")

    @v2_router.get("/order/{order_id}")
    async def get_order_v2(order_id: str):
        # Return order details with status for v2
        return {"order_id": order_id, "amount": 99.99, "status": "pending"}

    # Include routers
    app.include_router(v1_router)
    app.include_router(v2_router)

    # Simulate API setup
    print("API versioning enabled: /v1/order and /v2/order")
except ImportError:
    print("Mock Output: API versioning enabled: /v1/order and /v2/order")
```

## Output
```
Mock Output: API versioning enabled: /v1/order and /v2/order
```
*(Real output with `fastapi`: `API versioning enabled: /v1/order and /v2/order`)*

## Explanation
- **Purpose**: API versioning allows multiple versions of an API to coexist, supporting new features while maintaining compatibility.
- **Real-World Use Case**: In an e-commerce system, versioning the order API (e.g., adding `status` in v2) ensures existing clients continue using v1 without disruption.
- **Code Breakdown**:
  - A `FastAPI` app defines two routers: `v1` and `v2`.
  - The `v1` endpoint returns basic order details.
  - The `v2` endpoint adds a `status` field.
  - Routers are included with versioned prefixes.
- **Challenges**: Managing version sprawl, documenting changes, and migrating clients to newer versions.
- **Integration**: Works with Backward Compatibility (Snippet 634) and API Documentation (Snippet 620) for clear versioning.
- **Complexity**: O(1) for endpoint setup.
- **Best Practices**: Use clear version prefixes, document changes, automate version testing, and plan deprecation.