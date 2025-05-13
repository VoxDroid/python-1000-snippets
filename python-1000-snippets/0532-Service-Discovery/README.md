# Service Discovery

## Description
This snippet demonstrates a simulated service discovery using a dictionary.

## Code
```python
try:
    services = {"api": "localhost:8080", "db": "localhost:5432"}
    def discover(service_name):
        return services.get(service_name, "Service not found")
    print("Service address:", discover("api"))
except ImportError:
    print("Mock Output: Service address: localhost:8080")
```

## Output
```
Mock Output: Service address: localhost:8080
```
*(Real output: `Service address: localhost:8080`)*

## Explanation
- **Service Discovery**: Retrieves service endpoints dynamically.
- **Logic**: Looks up a service address in a dictionary.
- **Complexity**: O(1) per lookup.
- **Use Case**: Used in microservices to locate services.
- **Best Practice**: Use a registry like Consul; handle missing services; cache results.