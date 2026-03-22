# Attribute-Based Access Control

## Description
This snippet demonstrates ABAC with attribute policy evaluation and logging to temp.

## Code
- `SAMPLES/sample1.py`: evaluate user access based on department/clearance attributes.
- `SAMPLES/sample2.py`: evaluate multiple subjects against resource constraints.
- `SAMPLES/sample3.py`: write ABAC decision to `temp/0526_abac_log.txt`.

## Output
- sample1: `Access True/False`.
- sample2: policy result dictionary for subjects.
- sample3: temp log entry with decision.

## Explanation
- **Attribute-Based Access Control**: fine-grained access control by attributes.
- **Logic**: match user attributes against resource requirements.
- **Complexity**: O(n) for multiple subjects.
- **Use Case**: cloud services and dynamic permission checks.
- **Best Practice**: central policy engine and decision logging.
