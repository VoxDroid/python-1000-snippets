# Audit Trail Logging

## Description
This snippet demonstrates audit logging and verification using python `logging` module.

## Code
- `SAMPLES/sample1.py`: writes events to `temp/audit_0524.log`.
- `SAMPLES/sample2.py`: reads and counts events.
- `SAMPLES/sample3.py`: appends an additional audit event.

## Output
- sample1: message with log file path.
- sample2: count of audit entries.
- sample3: append confirmation.

## Explanation
- **Audit Trail Logging**: collects operational events for traceability.
- **Logic**: use log file with timestamped entries.
- **Complexity**: O(1) per event.
- **Use Case**: security auditing and compliance.
- **Best Practice**: rotate logs, restrict access, preserve logs for retention.
