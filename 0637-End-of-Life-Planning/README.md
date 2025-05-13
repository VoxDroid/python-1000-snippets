# End-of-Life Planning

## Description
This snippet demonstrates end-of-life (EOL) planning for an e-commerce API, scheduling the shutdown of a legacy endpoint.

## Code
```python
# End-of-life planning for a legacy API endpoint
try:
    from datetime import datetime, timedelta

    # Define EOL plan
    class EOLEndpoint:
        def __init__(self, endpoint: str, eol_date: datetime):
            self.endpoint = endpoint
            self.eol_date = eol_date

        # Check if endpoint is still active
        def is_active(self, current_date: datetime) -> bool:
            return current_date < self.eol_date

        # Generate EOL notice
        def get_notice(self, current_date: datetime) -> str:
            if not self.is_active(current_date):
                return f"Endpoint {self.endpoint} is no longer active as of {self.eol_date.date()}"
            return f"Endpoint {self.endpoint} will be retired on {self.eol_date.date()}"

    # Example usage
    eol = EOLEndpoint("/legacy/order", datetime(2025, 12, 31))
    current_date = datetime(2025, 5, 13)
    print("EOL notice:", eol.get_notice(current_date))
except ImportError:
    print("Mock Output: EOL notice: Endpoint /legacy/order will be retired on 2025-12-31")
```

## Output
```
Mock Output: EOL notice: Endpoint /legacy/order will be retired on 2025-12-31
```
*(Real output: `EOL notice: Endpoint /legacy/order will be retired on 2025-12-31`)*

## Explanation
- **Purpose**: EOL planning schedules the retirement of features or services, ensuring users are informed and prepared.
- **Real-World Use Case**: In an e-commerce system, planning the EOL of a legacy order endpoint helps clients migrate to a new API before shutdown.
- **Code Breakdown**:
  - The `EOLEndpoint` class tracks an endpoint and its EOL date.
  - The `is_active` method checks if the endpoint is still available.
  - The `get_notice` method generates a user-facing notice.
- **Challenges**: Communicating timelines, supporting users during transition, and ensuring no critical dependencies remain.
- **Integration**: Works with Deprecation Strategy (Snippet 635) and Sunset Policy (Snippet 638) for coordinated shutdowns.
- **Complexity**: O(1) for notice generation.
- **Best Practices**: Announce EOL early, provide migration guides, automate notices, and monitor usage.