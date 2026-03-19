# sample1.py
# Demonstrates querying sysDescr from a local SNMP agent using pysnmp.

import socket
import threading
import time

from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity import config, engine
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.smi import builder
from pysnmp.proto.rfc1902 import OctetString
from pysnmp.hlapi.asyncio import get_cmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity


def start_snmp_agent(port: int) -> engine.SnmpEngine:
    snmp_engine = engine.SnmpEngine()

    # Community string setup
    config.add_v1_system(snmp_engine, 'my-area', 'public')

    # Allow read-only access for the community.
    config.add_vacm_user(snmp_engine, 2, 'my-area', 'noAuthNoPriv', readSubTree=(1, 3, 6))

    # Bind to a UDP socket.
    config.addSocketTransport(
        snmp_engine,
        udp.DOMAIN_NAME,
        udp.UdpTransport().open_server_mode(('127.0.0.1', port)),
    )

    # Add a sysDescr value under SNMPv2-MIB.
    mib_builder = snmp_engine.get_mib_builder()
    mib_builder.load_modules('SNMPv2-MIB')
    SysDescr, = mib_builder.import_symbols('SNMPv2-MIB', 'sysDescr')
    MibScalarInstance, = mib_builder.import_symbols('SNMPv2-SMI', 'MibScalarInstance')

    sys_descr_instance = MibScalarInstance(
        SysDescr.name,
        (0,),
        OctetString('Local SNMP agent running in python-1000-snippets'),
    )
    mib_builder.export_symbols('PYTHON-1000-SNIPPETS', sysDescrInstance=sys_descr_instance)

    snmp_ctx = context.SnmpContext(snmp_engine)
    cmdrsp.GetCommandResponder(snmp_engine, snmp_ctx)

    # Start dispatcher in a background thread.
    def serve():
        snmp_engine.transport_dispatcher.job_started(1)
        try:
            snmp_engine.transport_dispatcher.run_dispatcher()
        except Exception:
            snmp_engine.transport_dispatcher.close_dispatcher()

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()
    time.sleep(0.1)

    return snmp_engine


async def query_sysdescr(port: int) -> str:
    target = await UdpTransportTarget.create(('127.0.0.1', port))
    errorIndication, errorStatus, errorIndex, varBinds = await get_cmd(
        SnmpEngine(),
        CommunityData('public', mpModel=1),
        target,
        ContextData(),
        ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
    )

    if errorIndication:
        raise RuntimeError(errorIndication)
    if errorStatus:
        raise RuntimeError(f"{errorStatus.prettyPrint()} at {errorIndex}")

    return str(varBinds[0][1])


async def main() -> None:
    # Find an available UDP port.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('127.0.0.1', 0))
        port = sock.getsockname()[1]

    snmp_engine = start_snmp_agent(port)
    try:
        sys_descr = await query_sysdescr(port)
        print('sysDescr:', sys_descr)
    finally:
        snmp_engine.transport_dispatcher.close_dispatcher()


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
