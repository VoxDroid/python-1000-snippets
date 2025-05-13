# Stakeholder Notification

## Description
This snippet demonstrates notifying stakeholders about a critical incident in an e-commerce platform, such as a service outage.

## Code
```python
# Stakeholder notification for incidents
try:
    from datetime import datetime

    # Simulated incident
    incident = {
        "id": "I002",
        "type": "service_outage",
        "details": "Order processing down"
    }

    # Notify stakeholders
    def notify_stakeholders(incident: dict, stakeholders: list) -> dict:
        # Generate notification
        notification = {
            "incident_id": incident["id"],
            "message": f"Critical incident: {incident['details']}",
            "recipients": stakeholders,
            "timestamp": datetime.now().isoformat()
        }
        return notification

    # Run notification
    result = notify_stakeholders(incident, ["ops@ecommerce.com", "ceo@ecommerce.com"])
    print("Stakeholder notification:", result)
except ImportError:
    print("Mock Output: Stakeholder notification: {'incident_id': 'I002', 'message': 'Critical incident: Order processing down', 'recipients': ['ops@ecommerce.com', 'ceo@ecommerce.com'], 'timestamp': '2025-05-13T21:48:00'}")
```

## Output
```
Mock Output: Stakeholder notification: {'incident_id': 'I002', 'message': 'Critical incident: Order processing down', 'recipients': ['ops@ecommerce.com', 'ceo@ecommerce.com'], 'timestamp': '2025-05-13T21:48:00'}
```
*(Real output: `Stakeholder notification: {'incident_id': 'I002', 'message': 'Critical incident: Order processing down', 'recipients': ['ops@ecommerce.com', 'ceo@ecommerce.com'], 'timestamp': '<current_time>'}`)*

## Explanation
- **Purpose**: Stakeholder notification informs key personnel about incidents, ensuring timely action.
- **Real-World Use Case**: In an e-commerce platform, notifying ops and executives about an outage ensures rapid response to restore order processing.
- **Code Breakdown**:
  - A simulated incident describes a service outage.
  - The `notify_stakeholders` function generates a notification with details and recipients.
  - The output shows the notification details.
- **Challenges**: Ensuring timely delivery, avoiding spam, and tailoring messages to audiences.
- **Integration**: Works with Crisis Management (Snippet 663) and Escalation Protocol (Snippet 665) for communication.
- **Complexity**: O(1) for notification generation.
- **Best Practices**: Use reliable channels (e.g., email, SMS), automate notifications, maintain contact lists, and log deliveries.