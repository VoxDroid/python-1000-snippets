# Container Orchestration

## Description
This snippet demonstrates container orchestration artifacts and checks with builtin Python.

## Code
- `SAMPLES/sample1.py`: generates and prints a Kubernetes pod definition JSON.
- `SAMPLES/sample2.py`: writes a pod manifest to `temp/0509_pod_manifest.yaml`.
- `SAMPLES/sample3.py`: runs `docker ps` if Docker CLI is installed.

## Output
- sample1: JSON pod manifest on stdout.
- sample2: file path and manifest validation.
- sample3: Docker container names or CLI missing message.

## Explanation
- **Container Orchestration**: Compose container deployment specs.
- **Logic**: build functions for pod definitions; file persistence; runtime check.
- **Complexity**: O(1) plus small I/O.
- **Use Case**: edge-of-stack orchestration script helper.
- **Best Practice**: Use `kubectl apply` for management; keep definitions in git.
