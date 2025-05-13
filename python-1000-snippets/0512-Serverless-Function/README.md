# Serverless Function

## Description
This snippet demonstrates a simulated AWS Lambda function.

## Code
```python
try:
    def lambda_handler(event, context):
        return {"statusCode": 200, "body": "Hello from Lambda!"}
    result = lambda_handler({}, {})
    print("Response:", result["body"])
except ImportError:
    print("Mock Output: Response: Hello from Lambda!")
```

## Output
```
Mock Output: Response: Hello from Lambda!
```
*(Real output: `Response: Hello from Lambda!`)*

## Explanation
- **Serverless Function**: Simulates an AWS Lambda handler.
- **Logic**: Returns a simple HTTP response.
- **Complexity**: O(1) per invocation.
- **Use Case**: Used for event-driven serverless applications.
- **Best Practice**: Handle events; log errors; optimize cold starts.