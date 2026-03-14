# SNMP Query

## Description
This snippet demonstrates querying an SNMP agent using `pysnmp`.

## Setup
A local SNMP agent (`snmpd`) is typically available on `localhost:161` on many systems.
This example uses the default community string `public` and queries standard MIB values like `sysDescr`.

## Code
```python
# Run the sample scripts in python-1000-snippets/0227-SNMP-Query/SAMPLES/
```

## Output
Samples print values retrieved from the SNMP agent (system description, uptime, etc.).

## Explanation
- **SNMP Query**: Uses `pysnmp` to send SNMP GET or WALK requests.
- **Logic**: Sends a request to the local SNMP agent and displays the returned OID values.
- **Complexity**: O(1) for GET; O(n) for walking a subtree.
- **Use Case**: Network monitoring, device discovery, or inventory collection.
- **Best Practice**: Use SNMPv3 with authentication and privacy for production systems.
