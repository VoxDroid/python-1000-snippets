# sample3.py
# Demonstrates SOAP fault handling when calling a service operation incorrectly.

import threading

from spyne import Application, Integer, rpc, ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


def _create_soap_app() -> WsgiApplication:
    class CalculatorService(ServiceBase):
        @rpc(Integer, Integer, _returns=Integer)
        def subtract(ctx, a: int, b: int) -> int:
            return a - b

    application = Application(
        [CalculatorService],
        tns="http://example.com/soap",
        in_protocol=Soap11(validator="lxml"),
        out_protocol=Soap11(),
    )

    return WsgiApplication(application)


def main() -> None:
    app = _create_soap_app()
    server = make_server("127.0.0.1", 0, app)
    port = server.server_port

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        from zeep import Client
        from zeep.exceptions import Fault

        wsdl = f"http://127.0.0.1:{port}/?wsdl"
        client = Client(wsdl=wsdl)

        # Calling with missing parameters triggers a SOAP fault.
        try:
            client.service.subtract(10)
        except Fault as exc:
            print("SOAP Fault received:", exc)
    finally:
        server.shutdown()
        thread.join(timeout=5)


if __name__ == "__main__":
    main()
