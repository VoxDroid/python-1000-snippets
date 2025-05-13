# Revenue Recognition

## Description
This snippet demonstrates recognizing revenue for an e-commerce subscription based on the subscription period, ensuring accurate financial reporting.

## Code
```python
# Revenue recognition for subscriptions
try:
    from datetime import datetime, timedelta
    import pandas as pd

    # Simulated subscription data
    subscriptions = [
        {"id": "sub_123", "amount": 1200, "start_date": "2025-01-01", "duration_months": 12}
    ]

    # Recognize revenue
    def recognize_revenue(subscriptions: list, current_date: str) -> dict:
        current = datetime.strptime(current_date, "%Y-%m-%d")
        revenue = {}
        for sub in subscriptions:
            start = datetime.strptime(sub["start_date"], "%Y-%m-%d")
            end = start + timedelta(days=30 * sub["duration_months"])
            if start <= current <= end:
                # Calculate monthly revenue
                monthly = sub["amount"] / sub["duration_months"]
                revenue[sub["id"]] = monthly
        return revenue

    # Example usage
    result = recognize_revenue(subscriptions, "2025-05-13")
    print("Revenue recognized:", result)
except ImportError:
    print("Mock Output: Revenue recognized: {'sub_123': 100.0}")
```

## Output
```
Mock Output: Revenue recognized: {'sub_123': 100.0}
```
*(Real output: `Revenue recognized: {'sub_123': 100.0}`)*

## Explanation
- **Purpose**: Revenue recognition allocates revenue over the service period, adhering to accounting standards like ASC 606.
- **Real-World Use Case**: In an e-commerce platform, recognizing subscription revenue monthly ensures accurate financial statements for premium services.
- **Code Breakdown**:
  - Simulated subscription data includes amount, start date, and duration.
  - The `recognize_revenue` function calculates monthly revenue if the current date falls within the subscription period.
  - The output shows recognized revenue per subscription.
- **Challenges**: Handling partial periods, ensuring compliance with GAAP/IFRS, and integrating with accounting systems.
- **Integration**: Complements Subscription Management (Snippet 652) and Financial Reporting (Snippet 654) for accurate bookkeeping.
- **Complexity**: O(n) for processing n subscriptions.
- **Best Practices**: Align with accounting standards, automate calculations, audit regularly, and integrate with ERP systems.