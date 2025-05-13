# Feature Deprecation

## Description
This snippet demonstrates deprecating a feature (discount calculation) in an e-commerce API, replacing it with a new implementation.

## Code
```python
# Feature deprecation for discount calculation
# Note: Requires `fastapi`. Install with `pip install fastapi`
try:
    from fastapi import FastAPI
    import warnings

    # Initialize FastAPI app
    app = FastAPI()

    @app.get("/discount/legacy")
    async def legacy_discount(price: float, rate: float):
        # Deprecated discount calculation
        warnings.warn("Legacy discount is deprecated. Use /discount instead.", DeprecationWarning)
        return {"discount": price * rate}

    @app.get("/discount")
    async def new_discount(price: float, rate: float):
        # New discount calculation with validation
        if rate > 1 or rate < 0:
            raise ValueError("Rate must be between 0 and 1")
        return {"discount": price * (1 - rate)}

    # Simulate API setup
    print("Feature deprecation enabled: Legacy discount warns users")
except ImportError:
    print("Mock Output: Feature deprecation enabled: Legacy discount warns users")
```

## Output
```
Mock Output: Feature deprecation enabled: Legacy discount warns users
```
*(Real output with `fastapi`: `Feature deprecation enabled: Legacy discount warns users` with warning in logs)*

## Explanation
- **Purpose**: Feature deprecation phases out outdated functionality, encouraging users to adopt improved versions.
- **Real-World Use Case**: In an e-commerce system, deprecating a flawed discount calculation ensures clients use a validated, correct implementation.
- **Code Breakdown**:
  - The `/discount/legacy` endpoint uses an old, incorrect discount formula and issues a warning.
  - The `/discount` endpoint implements a validated calculation.
  - The setup confirms the deprecation.
- **Challenges**: Ensuring users transition, maintaining compatibility, and testing new implementations.
- **Integration**: Pairs with Deprecation Strategy (Snippet 635) and API Versioning (Snippet 633) for smooth feature updates.
- **Complexity**: O(1) for discount calculations.
- **Best Practices**: Warn early, provide clear alternatives, test new features, and monitor deprecated usage.