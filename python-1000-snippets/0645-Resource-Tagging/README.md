# Resource Tagging

## Description
This snippet demonstrates tagging AWS EC2 instances for an e-commerce system to track ownership and purpose.

## Code
```python
# Resource tagging for AWS EC2 instances
# Note: Requires `boto3`. Install with `pip install boto3`
try:
    import boto3

    # Simulate EC2 client
    ec2_client = boto3.client("ec2", region_name="us-east-1")

    # Tag resources
    def tag_instance(instance_id: str, tags: dict):
        # Simulated tagging
        response = {
            "ResponseMetadata": {"HTTPStatusCode": 200},
            "Tags": [{"Key": k, "Value": v} for k, v in tags.items()]
        }
        return response

    # Example usage
    tags = {"Owner": "EcommerceTeam", "Purpose": "OrderProcessing"}
    result = tag_instance("i-123", tags)
    print("Resource tagging completed:", result["Tags"])
except ImportError:
    print("Mock Output: Resource tagging completed: [{'Key': 'Owner', 'Value': 'EcommerceTeam'}, {'Key': 'Purpose', 'Value': 'OrderProcessing'}]")
```

## Output
```
Mock Output: Resource tagging completed: [{'Key': 'Owner', 'Value': 'EcommerceTeam'}, {'Key': 'Purpose', 'Value': 'OrderProcessing'}]
```
*(Real output with `boto3`: `Resource tagging completed: [<tag list>]`)*

## Explanation
- **Purpose**: Resource tagging assigns metadata to cloud resources, improving tracking and cost allocation.
- **Real-World Use Case**: In an e-commerce system, tagging EC2 instances by team and purpose helps attribute costs and manage resources.
- **Code Breakdown**:
  - A simulated `boto3` client tags an EC2 instance.
  - The `tag_instance` function applies tags like `Owner` and `Purpose`.
  - The output confirms the tags applied.
- **Challenges**: Ensuring consistent tagging, enforcing policies, and updating legacy resources.
- **Integration**: Works with Cost Optimization (Snippet 644) and Cost Allocation (Snippet 648) for cost tracking.
- **Complexity**: O(1) for tagging operations.
- **Best Practices**: Define tagging policies, automate tagging, use standardized tags, and audit regularly.