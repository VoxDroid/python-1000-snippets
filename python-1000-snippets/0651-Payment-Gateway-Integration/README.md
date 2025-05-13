# Payment Gateway Integration

## Description
This snippet demonstrates integrating the Stripe payment gateway into an e-commerce platform to process order payments securely.

## Code
```python
# Payment gateway integration with Stripe
# Note: Requires `stripe`. Install with `pip install stripe`
try:
    import stripe

    # Configure Stripe API key (use environment variable in production)
    stripe.api_key = "sk_test_123"

    # Process payment for an order
    def process_payment(order_id: str, amount: float, currency: str = "usd") -> dict:
        # Create a payment intent
        payment_intent = stripe.PaymentIntent.create(
            amount=int(amount * 100),  # Convert to cents
            currency=currency,
            description=f"Order {order_id}",
            metadata={"order_id": order_id}
        )
        return {
            "payment_id": payment_intent["id"],
            "status": payment_intent["status"],
            "client_secret": payment_intent["client_secret"]
        }

    # Example usage
    result = process_payment("O001", 99.99)
    print("Payment processed:", result)
except ImportError:
    print("Mock Output: Payment processed: {'payment_id': 'pi_123', 'status': 'requires_confirmation', 'client_secret': 'secret_123'}")
```

## Output
```
Mock Output: Payment processed: {'payment_id': 'pi_123', 'status': 'requires_confirmation', 'client_secret': 'secret_123'}
```
*(Real output with `stripe`: `Payment processed: {'payment_id': '<payment_intent_id>', 'status': 'requires_confirmation', 'client_secret': '<client_secret>'}`)*

## Explanation
- **Purpose**: Payment gateway integration enables secure transaction processing, ensuring reliable payment collection.
- **Real-World Use Case**: In an e-commerce platform, integrating Stripe allows customers to pay for orders using credit cards, supporting seamless checkout.
- **Code Breakdown**:
  - The `stripe` library is configured with an API key.
  - The `process_payment` function creates a payment intent for a given order, converting the amount to cents and including metadata.
  - The output includes the payment ID, status, and client secret for frontend confirmation.
- **Challenges**: Handling payment failures, ensuring PCI compliance, and managing refunds or disputes.
- **Integration**: Complements Subscription Management (Snippet 652) and Tax Calculation (Snippet 655) for complete financial workflows.
- **Complexity**: O(1) for creating a payment intent.
- **Best Practices**: Use environment variables for API keys, implement webhooks for payment updates, log transactions, and test with Stripe’s sandbox.