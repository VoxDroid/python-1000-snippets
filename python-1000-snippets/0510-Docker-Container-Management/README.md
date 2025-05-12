# Docker Container Management

## Description
This snippet demonstrates starting a Docker container using `docker`.

## Code
```python
# Note: Requires `docker`. Install with `pip install docker`
try:
    import docker
    client = docker.from_env()
    container = client.containers.run("alpine", "echo hello", detach=True)
    print("Container started")
    container.stop()
except ImportError:
    print("Mock Output: Container started")
```

## Output
```
Mock Output: Container started
```
*(Real output with `docker`: `Container started`)*

## Explanation
- **Docker Container Management**: Runs a simple Alpine container.
- **Logic**: Starts a container to echo "hello" and stops it.
- **Complexity**: O(1) per container operation.
- **Use Case**: Used for development or CI/CD pipelines.
- **Best Practice**: Clean up containers; secure images; log outputs.