# Deprecation Strategy

## Description
This snippet demonstrates a deprecation strategy for an e-commerce API, issuing warnings for a legacy endpoint.

## Code
```python
# Deprecation strategy for an API endpoint
# Note: Requires `fastapi`. Install with `pip install fastapi`
try:
    from fastapi import FastAPI, HTTPException
    import warnings

    # Initialize FastAPI app
    app = FastAPI()

    @app.get("/legacy/order/{order_id}")
    async def get_legacy_order(order_id: str):
        # Issue deprecation warning
        warnings.warn("The /legacy/order endpoint is deprecated. Use /order instead.", DeprecationWarning)
        return {"order_id": order_id, "amount": 99.99}

    @app.get("/order/{order_id}")
    async def get_order(order_id: str):
        # Current endpoint
        return {"order_id": order_id, "amount": 99.99, "status": "pending"}

    # Simulate API setup
    print("Deprecation strategy enabled: /legacy/order warns users")
except ImportError:
    print("Mock Output: Deprecation strategy enabled: /legacy/order warns users")
```

## Output
```
Mock Output: Deprecation strategy enabled: /legacy/order warns users
```
*(Real output with `fastapi`: `Deprecation strategy enabled: /legacy/order warns users` with warning in logs)*

## Explanation
- **Purpose**: A deprecation strategy communicates that an API feature is outdated, guiding users to new endpoints while maintaining functionality.
- **Real-World Use Case**: In an e-commerce system, deprecating a legacy order endpoint ensures clients transition to a new version with additional features like status tracking.
- **Code Breakdown**:
  - A `/legacy/order` endpoint issues a `DeprecationWarning` but still functions.
  - The `/order` endpoint provides the current implementation.
  - The setup confirms the deprecation strategy.
- **Challenges**: Communicating deprecation effectively, tracking usage, and enforcing sunset dates.
- **Integration**: Works with Backward Compatibility (Snippet 634) and Feature Deprecation (Snippet 636) for phased transitions.
- **Complexity**: O(1) for endpoint processing.
- **Best Practices**: Issue clear warnings, document alternatives, monitor usage, and set clear sunset dates.