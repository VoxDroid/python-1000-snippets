# 0225-Telnet-Client Cheatsheet

* Use `telnetlib3` to implement both a Telnet client and server in Python.
* Create a server with `telnetlib3.create_server(host, port, shell=...)`.
* Connect with `telnetlib3.open_connection(host, port)`.
* Use `reader.readline()`/`writer.write()` to exchange data.
* Telnet is plaintext; do not use for sensitive data.
* For automated testing, run the server and client in the same script.
