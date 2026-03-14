# sample1.py
# Query the local SNMP agent for sysDescr using pysnmp.

import asyncio

from pysnmp.hlapi.v1arch.asyncio import (
    SnmpDispatcher,
    CommunityData,
    UdpTransportTarget,
    ObjectType,
    ObjectIdentity,
    get_cmd,
)


async def main():
    error, _, _, varBinds = await get_cmd(
        SnmpDispatcher(),
        CommunityData('public'),
        await UdpTransportTarget.create(('localhost', 161)),
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
    )

    if error:
        print('SNMP error:', error)
        return

    for varBind in varBinds:
        print('System description:', varBind[1])


if __name__ == '__main__':
    asyncio.run(main())
