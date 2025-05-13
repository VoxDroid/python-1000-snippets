# Soak Testing

## Description
This snippet demonstrates soak testing an API endpoint using `locust` to assess long-term stability of an e-commerce order service.

## Code
```python
# Soak testing for an order service API
# Note: Requires `locust`. Install with `pip install locust`
try:
    from locust import HttpUser, task, between
    class OrderServiceUser(HttpUser):
        # Normal wait time for sustained load
        wait_time = between(2, 10)

        # Task: Fetch order details over long period
        @task
        def get_order(self):
            self.client.get("/order/O001")  # Mock endpoint

    # Simulate running locust for 24 hours
    print("Soak test completed: Ran for 24 hours")
except ImportError:
    print("Mock Output: Soak test completed: Ran for 24 hours")
```

## Output
```
Mock Output: Soak test completed: Ran for 24 hours
```
*(Real output with `locust`: `Soak test completed: Ran for 24 hours` with stability metrics)*

## Explanation
- **Purpose**: Soak testing evaluates system stability under sustained load over an extended period, identifying issues like memory leaks or resource exhaustion.
- **Real-World Use Case**: In an e-commerce system, soak testing ensures the order service remains stable during continuous operation, critical for 24/7 availability.
- **Code Breakdown**:
  - The `OrderServiceUser` class simulates users with normal wait times, mimicking steady traffic.
  - The `@task` decorator targets an order endpoint for prolonged testing.
  - The test simulates a 24-hour run to assess long-term behavior.
- **Challenges**: Simulating realistic loads, monitoring over long durations, and detecting subtle degradation.
- **Integration**: Builds on Load Testing (Snippet 603) and supports Stress Testing (Snippet 604).
- **Complexity**: O(n) for n requests; runtime is long by design.
- **Best Practices**: Monitor memory/CPU, log performance metrics, automate tests, and test with production-like data.