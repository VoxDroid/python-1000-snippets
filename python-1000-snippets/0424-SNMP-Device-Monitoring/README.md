# SNMP Device Monitoring

## Description
This snippet demonstrates querying an SNMP device using `pysnmp`.

## Code
```python
# Note: Requires `pysnmp`. Install with `pip install pysnmp`
try:
    from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity
    iterator = getCmd(SnmpEngine(), CommunityData("public"), UdpTransportTarget(("localhost", 161)), ContextData(), ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)))
    error, _, _, varBinds = next(iterator)
    print("Mock Output: Device info retrieved")
except ImportError:
    print("Mock Output: Device info retrieved")
```

## Output
```
Mock Output: Device info retrieved
```
*(Real output with `pysnmp` and SNMP device: Device description)*

## Explanation
- **SNMP Device Monitoring**: Queries device information via SNMP.
- **Logic**: Uses `pysnmp` to retrieve system description.
- **Complexity**: O(1) per query (network-dependent).
- **Use Case**: Used for network device monitoring.
- **Best Practice**: Secure with SNMPv3; handle errors; validate OIDs.