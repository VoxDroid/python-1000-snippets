# Serverless Function

## Description
This snippet demonstrates a simulated AWS Lambda function invocation in pure Python.

## Code
- `SAMPLES/sample1.py`: main Lambda handler invoked with an event.
- `SAMPLES/sample2.py`: batch event processing for lambda-like behavior.
- `SAMPLES/sample3.py`: logs outputs to `temp/0512_lambda_results.txt`.

## Output
- `sample1.py`: `Response: Hello developer!`
- `sample2.py`: `Batch results: [0, 2, 4, 6, 8]`
- `sample3.py`: writes results file and prints file path.

## Explanation
- **Serverless Function**: event-driven function pattern.
- **Logic**: request event -> handler -> response payload.
- **Complexity**: O(n) for batch invocation, O(1) per event.
- **Use Case**: prototyping Lambda handler behavior and test harnesses.
- **Best Practice**: add input validation, error handlers, and monitor execution times.
