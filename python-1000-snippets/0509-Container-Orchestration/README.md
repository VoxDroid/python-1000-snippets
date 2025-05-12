# Container Orchestration

## Description
This snippet demonstrates a simulated Kubernetes pod definition.

## Code
```python
try:
    pod = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {"name": "example-pod"},
        "spec": {"containers": [{"name": "example", "image": "nginx"}]}
    }
    print("Pod definition:", pod["metadata"]["name"])
except ImportError:
    print("Mock Output: Pod definition: example-pod")
```

## Output
```
Mock Output: Pod definition: example-pod
```
*(Real output: `Pod definition: example-pod`)*

## Explanation
- **Container Orchestration**: Defines a Kubernetes pod spec.
- **Logic**: Creates a dictionary for an NGINX pod.
- **Complexity**: O(1) for definition.
- **Use Case**: Used in Kubernetes for container management.
- **Best Practice**: Validate YAML; use kubectl; test deployments.