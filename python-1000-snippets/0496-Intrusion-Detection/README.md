# Intrusion Detection

## Description
This snippet demonstrates a simple intrusion detection rule using `scapy`.

## Code
```python
# Note: Requires `scapy`. Install with `pip install scapy`
try:
    from scapy.all import sniff

    detection_results = []

    def detect(packet):
        if packet.haslayer("TCP") and packet["TCP"].dport == 22:
            result = "SSH attempt detected"
            detection_results.append(result)
            return result
        return None

    sniff(count=1, prn=detect)
    print("Detection result:", detection_results[0] if detection_results else "None")

except ImportError:
    print("Mock Output: Detection result: None")
```

## Output
```
Mock Output: Detection result: None
```
*(Real output with `scapy`: `Detection result: <SSH attempt or None>`)*

## Explanation
- **Intrusion Detection**: Monitors for SSH connection attempts.
- **Logic**: Sniffs packets and checks for TCP port 22.
- **Complexity**: O(n) for n packets.
- **Use Case**: Used in network security monitoring.
- **Best Practice**: Define robust rules; log alerts; minimize false positives.