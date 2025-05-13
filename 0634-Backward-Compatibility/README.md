# Backward Compatibility

## Description
This snippet demonstrates maintaining backward compatibility in an e-commerce API by supporting legacy order formats.

## Code
```python
# Backward compatibility for an e-commerce API
# Note: Requires `fastapi`. Install with `pip install fastapi`
try:
    from fastapi import FastAPI
    from pydantic import BaseModel

    # Define models
    class LegacyOrder(BaseModel):
        order_id: str
        price: float  # Legacy field

    class NewOrder(BaseModel):
        order_id: str
        amount: float  # New field
        status: str

    # Initialize FastAPI app
    app = FastAPI()

    @app.post("/order")
    async def create_order(order: LegacyOrder | NewOrder):
        # Handle both legacy and new order formats
        if hasattr(order, "price"):
            return {"order_id": order.order_id, "amount": order.price, "status": "pending"}
        return order.dict()

    # Simulate API setup
    print("Backward compatibility enabled: Supports legacy and new order formats")
except ImportError:
    print("Mock Output: Backward compatibility enabled: Supports legacy and new order formats")
```

## Output
```
Mock Output: Backward compatibility enabled: Supports legacy and new order formats
```
*(Real output with `fastapi`: `Backward compatibility enabled: Supports legacy and new order formats`)*

## Explanation
- **Purpose**: Backward compatibility ensures new API versions support existing clients, preventing disruptions.
- **Real-World Use Case**: In an e-commerce system, supporting a legacy `price` field alongside a new `amount` field allows older clients to continue functioning.
- **Code Breakdown**:
  - Pydantic models define `LegacyOrder` (with `price`) and `NewOrder` (with `amount` and `status`).
  - The `/order` endpoint accepts either model, converting legacy orders to the new format.
  - The setup confirms compatibility.
- **Challenges**: Managing complex legacy formats, testing compatibility, and phasing out old formats.
- **Integration**: Pairs with API Versioning (Snippet 633) and Deprecation Strategy (Snippet 635) for smooth transitions.
- **Complexity**: O(1) for request processing.
- **Best Practices**: Test legacy paths, document compatibility, automate validation, and plan deprecation timelines.