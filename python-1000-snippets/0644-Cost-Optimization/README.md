# Cost Optimization

## Description
This snippet demonstrates cost optimization for an e-commerce system by identifying unused AWS EC2 instances.

## Code
```python
# Cost optimization for AWS EC2 instances
# Note: Requires `boto3`. Install with `pip install boto3`
try:
    import boto3

    # Simulate EC2 client
    ec2_client = boto3.client("ec2", region_name="us-east-1")

    # Check for unused instances
    def optimize_costs():
        # Simulated response with instance data
        response = {
            "Reservations": [
                {"Instances": [{"InstanceId": "i-123", "State": {"Name": "stopped"}}]},
                {"Instances": [{"InstanceId": "i-456", "State": {"Name": "running"}}]}
            ]
        }
        unused = [i["InstanceId"] for r in response["Reservations"] for i in r["Instances"] if i["State"]["Name"] == "stopped"]
        return unused

    # Run optimization
    unused_instances = optimize_costs()
    print("Cost optimization:", f"Unused instances: {unused_instances}")
except ImportError:
    print("Mock Output: Cost optimization: Unused instances: ['i-123']")
```

## Output
```
Mock Output: Cost optimization: Unused instances: ['i-123']
```
*(Real output with `boto3`: `Cost optimization: Unused instances: [<instance IDs>]`)*

## Explanation
- **Purpose**: Cost optimization identifies and eliminates unused cloud resources to reduce expenses.
- **Real-World Use Case**: In an e-commerce system, terminating stopped EC2 instances saves costs during low-traffic periods.
- **Code Breakdown**:
  - A simulated `boto3` client checks EC2 instance states.
  - The `optimize_costs` function identifies stopped instances.
  - The output lists unused instances.
- **Challenges**: Avoiding disruption, automating checks, and balancing performance with cost.
- **Integration**: Works with Resource Tagging (Snippet 645) and Budget Monitoring (Snippet 646) for cost management.
- **Complexity**: O(n) for checking n instances.
- **Best Practices**: Automate checks, use cost explorer tools, set alerts, and review regularly.