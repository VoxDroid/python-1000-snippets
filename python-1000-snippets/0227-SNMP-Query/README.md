# SNMP Query

## Description
This snippet demonstrates querying an SNMP device using `pysnmp`.

## Code
```python
# Note: Requires `pysnmp`. Install with `pip install pysnmp`
try:
    from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity
    iterator = getCmd(
        SnmpEngine(),
        CommunityData("public"),
        UdpTransportTarget(("localhost", 161)),
        ContextData(),
        ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0))
    )
    error, _, _, varBinds = next(iterator)
    print("System Description:", str(varBinds[0]))
except ImportError:
    print("Mock Output: System Description: Hardware: x86")
```

## Output
```
Mock Output: System Description: Hardware: x86
```
*(Real output with SNMP: `System Description: <device description>`)*

## Explanation
- **SNMP Query**: Queries a device’s system description using `pysnmp`.
- **Logic**: Sends a GET request for the `sysDescr` OID.
- **Complexity**: O(1) for query (network latency varies).
- **Use Case**: Used for network monitoring or device management.
- **Best Practice**: Secure SNMP with v3; handle errors; ensure device is SNMP-enabled.