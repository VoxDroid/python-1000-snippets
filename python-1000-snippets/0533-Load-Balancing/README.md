# Load Balancing

## Description
This snippet demonstrates a simple round-robin load balancer.

## Code
```python
try:
    servers = ["server1:8080", "server2:8080"]
    current = 0
    def get_server():
        global current
        server = servers[current]
        current = (current + 1) % len(servers)
        return server
    print("Selected server:", get_server())
except ImportError:
    print("Mock Output: Selected server: server1:8080")
```

## Output
```
Mock Output: Selected server: server1:8080
```
*(Real output: `Selected server: server1:8080`)*

## Explanation
- **Load Balancing**: Distributes requests across servers.
- **Logic**: Selects servers in a round-robin fashion.
- **Complexity**: O(1) per selection.
- **Use Case**: Used to balance traffic in distributed systems.
- **Best Practice**: Add health checks; support weighted balancing; monitor performance.