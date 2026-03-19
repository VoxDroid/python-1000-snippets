# 0424 - SNMP Device Monitoring Cheatsheet

## Quick Facts
- Uses `pysnmp` to run a local SNMPv2c agent and query it.
- Demonstrates `GET`, `GETNEXT`, and SNMP walk operations.

## Run Samples
```bash
python python-1000-snippets/0424-SNMP-Device-Monitoring/SAMPLES/sample1.py
python python-1000-snippets/0424-SNMP-Device-Monitoring/SAMPLES/sample2.py
python python-1000-snippets/0424-SNMP-Device-Monitoring/SAMPLES/sample3.py
```

## Key pysnmp APIs
- `getCmd(...)` - fetch a specific OID value.
- `nextCmd(...)` - fetch the next OID (used for walks).
- `SnmpEngine`, `CommunityData`, `UdpTransportTarget` - configure the SNMP client.

## Notes
- The agent listens on a dynamic local UDP port; the client queries the same port.
- The community string is `public` for read-only access.
