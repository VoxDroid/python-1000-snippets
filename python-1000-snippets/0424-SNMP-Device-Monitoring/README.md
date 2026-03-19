# SNMP Device Monitoring

## Description
This snippet demonstrates querying an SNMP agent using `pysnmp`.

The examples run a local SNMP agent in-process and then query it using SNMPv2c GET and GETNEXT operations.

## Requirements
- Python 3.8+
- `pysnmp` (`pip install pysnmp`)

## Samples
- `SAMPLES/sample1.py`: Query the `sysDescr` scalar via SNMP GET.
- `SAMPLES/sample2.py`: Perform an SNMP GETNEXT (next OID) operation.
- `SAMPLES/sample3.py`: Walk a MIB subtree using SNMP GETNEXT.

## Running
```bash
python python-1000-snippets/0424-SNMP-Device-Monitoring/SAMPLES/sample1.py
python python-1000-snippets/0424-SNMP-Device-Monitoring/SAMPLES/sample2.py
python python-1000-snippets/0424-SNMP-Device-Monitoring/SAMPLES/sample3.py
```

## Notes
- The local agent uses community string `public` and listens on a dynamically selected UDP port.
- The examples do not require any external SNMP device.
