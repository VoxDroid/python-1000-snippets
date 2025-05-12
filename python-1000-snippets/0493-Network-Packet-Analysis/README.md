# Network Packet Analysis

## Description
This snippet demonstrates packet sniffing using `scapy`.

## Code
```python
# Note: Requires `scapy`. Install with `pip install scapy`
try:
    from scapy.all import sniff
    packets = sniff(count=1, filter="tcp")
    print("Packet captured:", len(packets))
except ImportError:
    print("Mock Output: Packet captured: 1")
```

## Output
```
Mock Output: Packet captured: 1
```
*(Real output with `scapy`: `Packet captured: <number of packets>`)*

## Explanation
- **Network Packet Analysis**: Captures TCP packets.
- **Logic**: Uses `scapy` to sniff one packet.
- **Complexity**: O(n) for n packets (network-dependent).
- **Use Case**: Used for network diagnostics or security analysis.
- **Best Practice**: Filter packets; handle permissions; log results.