# Kubernetes Deployment

## Description
This snippet demonstrates generating Kubernetes deployment manifests and checking kubectl availability.

## Code
- `SAMPLES/sample1.py`: creates a Kubernetes deployment object and prints JSON representation.
- `SAMPLES/sample2.py`: writes a deployment YAML manifest to `temp/0511_deployment.yaml`.
- `SAMPLES/sample3.py`: checks `kubectl version` if installed.

## Output
- sample1: printed JSON manifest.
- sample2: manifest file created in `temp`.
- sample3: `kubectl` version or missing message.

## Explanation
- **Kubernetes Deployment**: simulates deployment manifest generation by code.
- **Logic**: no external Kubernetes client required; safe local generation.
- **Complexity**: O(1).
- **Use Case**: preparing YAML for `kubectl apply` or CI templates.
- **Best Practice**: validate with `kubectl apply --dry-run=client`, keep manifests in version control.
