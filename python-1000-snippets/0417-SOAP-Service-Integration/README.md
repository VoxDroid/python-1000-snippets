# SOAP Service Integration

## Description
Demonstrates setting up a local SOAP service using `spyne` and calling it with the `zeep` SOAP client.

## Requirements
- Python 3.8+
- `spyne` (`pip install spyne`)
- `zeep` (`pip install zeep`)
- `lxml` (installed as a dependency of `spyne`)

## Code (excerpt)
```python
from spyne import Application, rpc, ServiceBase, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a: int, b: int) -> int:
        return a + b

app = WsgiApplication(
    Application([CalculatorService], tns="http://example.com/soap", in_protocol=Soap11(), out_protocol=Soap11())
)
```

## Output (sample)
```
7 + 5 = 12
```

## Notes
- The samples start a local HTTP server that exposes the WSDL at `/?wsdl`.
- `zeep` auto-generates a client from the WSDL and allows calling operations like normal methods.
