# Docker Container Management

## Description
This snippet demonstrates container management using Docker CLI where available.

## Code
- `SAMPLES/sample1.py`: runs an Alpine container command via `docker run --rm`.
- `SAMPLES/sample2.py`: lists running containers with `docker ps`.
- `SAMPLES/sample3.py`: logs Docker version check to `temp/0510_docker_status.txt`.

## Output
- sample1: prints container output or errors based on Docker availability.
- sample2: prints running container list or availability message.
- sample3: writes status string to temp file.

## Explanation
- **Docker Container Management**: interacts with Docker runtime via subprocess calls.
- **Logic**: CLI command invocations with error handling.
- **Complexity**: O(1) per operation.
- **Use Case**: quick health checks and command-based container management scripts.
- **Best Practice**: use defensive checks for environment, cleanup resources, log outputs.
