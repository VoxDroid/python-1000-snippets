# Role-Based Access Control

## Description
This snippet demonstrates RBAC with role permissions and denial logging.

## Code
- `SAMPLES/sample1.py`: check role permissions for actions.
- `SAMPLES/sample2.py`: authorization logic for user roles.
- `SAMPLES/sample3.py`: log denied access attempts to `temp/0525_rbac_denies.log`.

## Output
- sample1: prints access decisions.
- sample2: prints authorization checks.
- sample3: logs denial events.

## Explanation
- **Role-Based Access Control**: assign abilities based on role.
- **Logic**: allow/deny decisions in small policy function.
- **Complexity**: O(1) checks.
- **Use Case**: protect resources in applications.
- **Best Practice**: centralize policies, audit denials, enforce least privilege.
