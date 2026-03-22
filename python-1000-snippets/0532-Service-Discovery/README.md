# Service Discovery

## Description
This snippet demonstrates basic service discovery and registry operations.

## Code
- `SAMPLES/sample1.py`: lookup service via a static registry.
- `SAMPLES/sample2.py`: dynamic register/deregister operations.
- `SAMPLES/sample3.py`: writes discovery report to `temp/0532_service_discovery.txt`.

## Output
- sample1: resolves service endpoints for known/unknown services.
- sample2: registry operations output.
- sample3: writes lookup report.

## Explanation
- **Service Discovery**: locate service endpoints via registry.
- **Logic**: dictionary lookup for service names.
- **Complexity**: O(1) per lookup.
- **Use Case**: microservices endpoint discovery.
- **Best Practice**: use dedicated service registry, handle stale endpoints, caching.
