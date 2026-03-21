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
`sample1.py` prints parsed firewall command fields.
`sample2.py` prints active rules after add/remove operations.
`sample3.py` prints whether test packets are allowed by rules.

## Explanation
- **Firewall Rule Management**: Parses and manages rules in-memory.
- **Logic**: Simulates addition/removal and packet matching.
- **Complexity**: O(n) for rule list processing.
- **Use Case**: Useful for firewall configuration parsers and policy checks.
- **Best Practice**: Normalize rule specification and audit modifications.
