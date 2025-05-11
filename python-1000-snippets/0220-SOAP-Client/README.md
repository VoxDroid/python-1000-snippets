# SOAP Client

## Description
This snippet demonstrates a SOAP client using `zeep` to call a web service.

## Code
```python
# Note: Requires `zeep`. Install with `pip install zeep`
try:
    from zeep import Client
    client = Client("http://www.dneonline.com/calculator.asmx?WSDL")
    result = client.service.Add(5, 3)
    print("Result:", result)
except ImportError:
    print("Mock Output: Result: 8")
```

## Output
```
Mock Output: Result: 8
```
*(Real output with `zeep`: `Result: 8`)*

## Explanation
- **SOAP Client**: Calls a SOAP web service’s `Add` method using `zeep`.
- **Logic**: Connects to a WSDL-defined service and invokes the method.
- **Complexity**: O(1) for the call (network latency varies).
- **Use Case**: Used for legacy enterprise systems or specific APIs.
- **Best Practice**: Handle WSDL errors; cache client instances; secure credentials.