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
`sample1.py` prints TCP packet count from a text packet list.
`sample2.py` prints byte sizes and header preview from such packet hex strings.
`sample3.py` prints whether SYN flood behavior is suspected.

## Explanation
- **Network Packet Analysis**: Processes packet-like text data without live sniffing.
- **Logic**: Parses key fields, evaluates protocol counts, and inspects flags.
- **Complexity**: O(n) in number of packets.
- **Use Case**: Useful when `scapy` is unavailable or to test parsing logic.
- **Best Practice**: Validate packet parsing and handle malformed lines.
