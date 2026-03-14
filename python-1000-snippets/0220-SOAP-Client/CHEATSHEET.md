# 0220-SOAP-Client Cheatsheet

* Install `zeep` with `pip install zeep`.
* Create client via WSDL URL: `Client('http://example.com/service?wsdl')`.
* Call SOAP methods via `client.service.MethodName(arg1, arg2)`.
* Use `client.settings(strict=False)` to tolerate schema mismatches.
* For auth, provide `Transport(session=...)` configured with HTTP auth or headers.
* Enable logging: `logging.basicConfig(level=logging.INFO)` to see SOAP requests/responses.
* Be careful with large responses; you can stream/walk the returned structure.
* Handle network errors via `requests.exceptions.RequestException`.
* If WSDL is unreachable, ensure network access and correct endpoint.

