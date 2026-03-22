# GDPR Compliance

## Description
This snippet demonstrates a GDPR data deletion flow with audit logs.

## Code
- `SAMPLES/sample1.py`: deletes user records from a list.
- `SAMPLES/sample2.py`: logs deletions to `temp/0523_gdpr_deletions.log`.
- `SAMPLES/sample3.py`: reads log and outputs deletion count.

## Output
- sample1: remaining user records printed.
- sample2: deletion event file path.
- sample3: count of deletions from log.

## Explanation
- **GDPR Compliance**: handle user erasure requests.
- **Logic**: filter records for deletion, append audit entries, verify log.
- **Complexity**: O(n).
- **Use Case**: data systems requiring right to erasure.
- **Best Practice**: secure audit trail, remove backups, confirm deletion.
