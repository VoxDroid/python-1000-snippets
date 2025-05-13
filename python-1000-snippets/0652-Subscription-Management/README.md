# Subscription Management

## Description
This snippet demonstrates managing recurring subscriptions for an e-commerce platform using Stripe, handling subscription creation and status checks.

## Code
```python
# Subscription management with Stripe
# Note: Requires `stripe`. Install with `pip install stripe`
try:
    import stripe

    # Configure Stripe API key
    stripe.api_key = "sk_test_123"

    # Create and manage a subscription
    def create_subscription(customer_id: str, price_id: str) -> dict:
        # Create a subscription for a customer
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[{"price": price_id}],
            payment_behavior="default_incomplete"
        )
        return {
            "subscription_id": subscription["id"],
            "status": subscription["status"],
            "current_period_end": subscription["current_period_end"]
        }

    # Example usage
    result = create_subscription("cus_123", "price_456")
    print("Subscription created:", result)
except ImportError:
    print("Mock Output: Subscription created: {'subscription_id': 'sub_123', 'status': 'incomplete', 'current_period_end': 1746729600}")
```

## Output
```
Mock Output: Subscription created: {'subscription_id': 'sub_123', 'status': 'incomplete', 'current_period_end': 1746729600}
```
*(Real output with `stripe`: `Subscription created: {'subscription_id': '<sub_id>', 'status': '<status>', 'current_period_end': <timestamp>}`)*

## Explanation
- **Purpose**: Subscription management automates recurring billing, ensuring consistent revenue streams.
- **Real-World Use Case**: In an e-commerce platform, managing subscriptions for premium services (e.g., free shipping) ensures automatic renewals and status tracking.
- **Code Breakdown**:
  - The `stripe` library is configured with an API key.
  - The `create_subscription` function creates a subscription linked to a customer and price plan.
  - The output includes the subscription ID, status, and renewal date.
- **Challenges**: Handling failed payments, managing cancellations, and syncing subscription states across systems.
- **Integration**: Works with Payment Gateway Integration (Snippet 651) and Revenue Recognition (Snippet 653) for financial tracking.
- **Complexity**: O(1) for subscription creation.
- **Best Practices**: Use webhooks for status updates, automate retries, offer flexible plans, and ensure clear cancellation policies.