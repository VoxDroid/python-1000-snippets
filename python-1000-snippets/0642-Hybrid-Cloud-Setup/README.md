# Hybrid Cloud Setup

## Description
This snippet demonstrates a hybrid cloud setup for an e-commerce system, combining on-premises and AWS S3 storage.

## Code
```python
# Hybrid cloud setup with AWS S3
# Note: Requires `boto3`. Install with `pip install boto3`
try:
    import boto3
    import os

    # Simulate on-premises storage
    def save_on_prem(file_name: str, data: str):
        with open(f"/on-prem/{file_name}", "w") as f:
            f.write(data)
        return f"/on-prem/{file_name}"

    # Simulate S3 client
    s3_client = boto3.client("s3")

    # Save to S3
    def save_to_s3(bucket: str, file_name: str, data: str):
        s3_client.put_object(Bucket=bucket, Key=file_name, Body=data)
        return f"s3://{bucket}/{file_name}"

    # Hybrid storage function
    def hybrid_save(file_name: str, data: str, use_cloud: bool):
        if use_cloud:
            return save_to_s3("ecommerce-bucket", file_name, data)
        return save_on_prem(file_name, data)

    # Simulate hybrid setup
    print("Hybrid cloud setup:", hybrid_save("order.csv", "order_data", True))
except ImportError:
    print("Mock Output: Hybrid cloud setup: s3://ecommerce-bucket/order.csv")
```

## Output
```
Mock Output: Hybrid cloud setup: s3://ecommerce-bucket/order.csv
```
*(Real output with `boto3`: `Hybrid cloud setup: s3://ecommerce-bucket/order.csv`)*

## Explanation
- **Purpose**: A hybrid cloud setup combines on-premises and cloud resources, balancing control and scalability.
- **Real-World Use Case**: In an e-commerce system, storing sensitive order data on-premises and reports in S3 provides flexibility and compliance.
- **Code Breakdown**:
  - The `save_on_prem` function simulates local storage.
  - The `save_to_s3` function simulates S3 storage.
  - The `hybrid_save` function chooses storage based on a flag.
- **Challenges**: Ensuring data consistency, managing latency, and securing hybrid connections.
- **Integration**: Works with Cloud Migration (Snippet 641) and Multi-Cloud Strategy (Snippet 643) for flexible infrastructure.
- **Complexity**: O(1) for storage operations.
- **Best Practices**: Secure data transfers, monitor performance, automate deployments, and plan workload distribution.