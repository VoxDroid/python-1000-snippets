# 0227-SNMP-Query Cheatsheet

* Use `pysnmp.hlapi` to construct SNMP GET and WALK requests.
* `getCmd()` performs a single GET request.
* `nextCmd()` performs an SNMP WALK over a subtree.
* Use `CommunityData('public')` for SNMP v2c with the default community.
* Target the agent with `UdpTransportTarget(('localhost', 161))`.
* For production, use SNMPv3 and secure community strings.
