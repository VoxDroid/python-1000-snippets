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
`sample1.py` prints detected SSH attempts from event text.
`sample2.py` prints detected suspicious payload signatures.
`sample3.py` prints brute-force alerts after threshold failed logins.

## Explanation
- **Intrusion Detection**: Detects patterns in network event logs.
- **Logic**: Text inspection / signature checks / stateful counting.
- **Complexity**: O(n) for n events.
- **Use Case**: Useful for security monitoring rules and alert generation.
- **Best Practice**: Tune thresholds; reduce false positives; log incidents.
