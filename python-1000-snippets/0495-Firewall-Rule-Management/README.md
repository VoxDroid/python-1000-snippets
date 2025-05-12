# Firewall Rule Management

## Description
This snippet demonstrates a simulated firewall rule setup using `iptables` syntax.

## Code
```python
try:
    rule = "iptables -A INPUT -p tcp --dport 80 -j ACCEPT"
    print("Firewall rule:", rule)
except Exception:
    print("Mock Output: Firewall rule: iptables -A INPUT -p tcp --dport 80 -j ACCEPT")
```

## Output
```
Mock Output: Firewall rule: iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```
*(Real output: `Firewall rule: iptables -A INPUT -p tcp --dport 80 -j ACCEPT`)*

## Explanation
- **Firewall Rule Management**: Defines a rule to allow TCP port 80 traffic.
- **Logic**: Generates an `iptables` command string.
- **Complexity**: O(1) for rule generation.
- **Use Case**: Used in network security or server management.
- **Best Practice**: Validate rules; test in sandbox; log changes.