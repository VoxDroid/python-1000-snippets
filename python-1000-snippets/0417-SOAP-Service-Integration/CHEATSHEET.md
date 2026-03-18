# 0417-SOAP-Service-Integration Cheatsheet

## Quick start
1. Install dependencies:
   ```bash
   pip install spyne zeep
   ```
2. Run a sample:
   ```bash
   python SAMPLES/sample1.py
   ```

## Key concepts
- **SOAP service**: A structured XML/RPC protocol with WSDL metadata.
- **Spyne**: Creates a local SOAP server and auto-generates a WSDL.
- **Zeep**: Consumes WSDL and exposes service operations as Python methods.

## Notes
- The sample scripts start a local HTTP server and shut it down after the call.
- SOAP faults (errors) are raised as `zeep.exceptions.Fault`.
