# sample3.py
# Demonstrates performing an SNMP walk (GETNEXT) over a subtree using a local SNMP agent.

import socket
import threading
import time

from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity import config, engine
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.smi import builder
from pysnmp.proto.rfc1902 import OctetString
from pysnmp.hlapi.asyncio import SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity, next_cmd


def start_snmp_agent(port: int) -> engine.SnmpEngine:
    snmp_engine = engine.SnmpEngine()
    config.add_v1_system(snmp_engine, 'my-area', 'public')
    config.add_vacm_user(snmp_engine, 2, 'my-area', 'noAuthNoPriv', readSubTree=(1, 3, 6))

    config.addSocketTransport(
        snmp_engine,
        udp.DOMAIN_NAME,
        udp.UdpTransport().open_server_mode(('127.0.0.1', port)),
    )

    mib_builder = snmp_engine.get_mib_builder()
    mib_builder.load_modules('SNMPv2-MIB')

    SysDescr, = mib_builder.import_symbols('SNMPv2-MIB', 'sysDescr')
    SysName, = mib_builder.import_symbols('SNMPv2-MIB', 'sysName')
    MibScalarInstance, = mib_builder.import_symbols('SNMPv2-SMI', 'MibScalarInstance')

    sys_descr_instance = MibScalarInstance(
        SysDescr.name,
        (0,),
        OctetString('Local SNMP agent for walk example'),
    )
    sys_name_instance = MibScalarInstance(
        SysName.name,
        (0,),
        OctetString('python-1000-snippets'),
    )
    mib_builder.export_symbols(
        'PYTHON-1000-SNIPPETS',
        sysDescrInstance=sys_descr_instance,
        sysNameInstance=sys_name_instance,
    )

    snmp_ctx = context.SnmpContext(snmp_engine)
    cmdrsp.GetCommandResponder(snmp_engine, snmp_ctx)
    cmdrsp.NextCommandResponder(snmp_engine, snmp_ctx)

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


async def snmp_walk(port: int, *oid):
    target = await UdpTransportTarget.create(('127.0.0.1', port))
    errorIndication, errorStatus, errorIndex, varBinds = await next_cmd(
        SnmpEngine(),
        CommunityData('public', mpModel=1),
        target,
        ContextData(),
        ObjectType(ObjectIdentity(*oid)),
        lexicographicMode=True,
    )

    if errorIndication:
        raise RuntimeError(errorIndication)
    if errorStatus:
        raise RuntimeError(f"{errorStatus.prettyPrint()} at {errorIndex}")

    return [(str(vb[0]), str(vb[1])) for vb in varBinds]


async def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind(('127.0.0.1', 0))
        port = sock.getsockname()[1]

    snmp_engine = start_snmp_agent(port)
    try:
        results = await snmp_walk(port, 'SNMPv2-MIB', 'sysDescr')
        for oid, val in results[:5]:
            print(oid, '=', val)
    finally:
        snmp_engine.transport_dispatcher.close_dispatcher()


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
