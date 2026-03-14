# sample2.py
# Walk a subtree of the SNMP agent (system group) using pysnmp.

import asyncio

from pysnmp.hlapi.v1arch.asyncio import (
    SnmpDispatcher,
    CommunityData,
    UdpTransportTarget,
    ObjectType,
    ObjectIdentity,
    next_cmd,
)


async def main():
    error, _, _, varBinds = await next_cmd(
        SnmpDispatcher(),
        CommunityData('public'),
        await UdpTransportTarget.create(('localhost', 161)),
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'system')),
    )

    if error:
        print('SNMP error:', error)
        return

    for varBind in varBinds:
        print(varBind)


if __name__ == '__main__':
    asyncio.run(main())
