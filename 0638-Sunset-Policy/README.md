# Sunset Policy

## Description
This snippet demonstrates a sunset policy for an e-commerce API, enforcing the retirement of a legacy endpoint after its EOL date.

## Code
```python
# Sunset policy for a legacy API endpoint
try:
    from datetime import datetime
    from fastapi import FastAPI, HTTPException

    # Initialize FastAPI app
    app = FastAPI()

    # Define sunset date
    SUNSET_DATE = datetime(2025, 12, 31)

    @app.get("/legacy/order/{order_id}")
    async def get_legacy_order(order_id: str):
        # Enforce sunset policy
        if datetime.now() > SUNSET_DATE:
            raise HTTPException(status_code=410, detail="Endpoint has been retired")
        return {"order_id": order_id, "amount": 99.99}

    # Simulate API setup
    print("Sunset policy enabled: /legacy/order retires after 2025-12-31")
except ImportError:
    print("Mock Output: Sunset policy enabled: /legacy/order retires after 2025-12-31")
```

## Output
```
Mock Output: Sunset policy enabled: /legacy/order retires after 2025-12-31
```
*(Real output with `fastapi`: `Sunset policy enabled: /legacy/order retires after 2025-12-31`)*

## Explanation
- **Purpose**: A sunset policy enforces the retirement of features by disabling them after a set date, ensuring clean system evolution.
- **Real-World Use Case**: In an e-commerce system, sunsetting a legacy order endpoint prevents its use post-EOL, forcing clients to adopt the new API.
- **Code Breakdown**:
  - A `FastAPI` endpoint checks the current date against the sunset date.
  - If past the sunset date, a 410 Gone error is raised.
  - The setup confirms the policy.
- **Challenges**: Ensuring users are migrated, handling unexpected dependencies, and logging sunset usage.
- **Integration**: Complements End-of-Life Planning (Snippet 637) and Deprecation Strategy (Snippet 635) for phased retirement.
- **Complexity**: O(1) for date checks.
- **Best Practices**: Set clear sunset dates, return appropriate errors, log access attempts, and provide migration support.