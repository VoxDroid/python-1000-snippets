# Kubernetes Deployment

## Description
This snippet demonstrates creating a Kubernetes deployment using `kubernetes`.

## Code
```python
# Note: Requires `kubernetes`. Install with `pip install kubernetes`
try:
    from kubernetes import client, config
    config.load_kube_config()
    v1 = client.AppsV1Api()
    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"name": "nginx-deployment"},
        "spec": {
            "replicas": 1,
            "selector": {"matchLabels": {"app": "nginx"}},
            "template": {
                "metadata": {"labels": {"app": "nginx"}},
                "spec": {"containers": [{"name": "nginx", "image": "nginx:latest"}]}
            }
        }
    }
    print("Deployment defined")
except ImportError:
    print("Mock Output: Deployment defined")
```

## Output
```
Mock Output: Deployment defined
```
*(Real output with `kubernetes`: `Deployment defined`)*

## Explanation
- **Kubernetes Deployment**: Defines a deployment for an NGINX container.
- **Logic**: Creates a deployment spec with one replica.
- **Complexity**: O(1) for definition.
- **Use Case**: Used for managing containerized applications in Kubernetes.
- **Best Practice**: Validate YAML; use namespaces; test with `kubectl apply`.