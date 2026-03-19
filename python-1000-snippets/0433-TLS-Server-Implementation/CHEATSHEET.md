# 0433-TLS-Server-Implementation Cheatsheet

- Use `ssl.SSLContext` to wrap sockets for TLS.
- For servers, use `ssl.Purpose.CLIENT_AUTH`; for clients, use `ssl.Purpose.SERVER_AUTH`.
- Load certificates with `SSLContext.load_cert_chain(certfile, keyfile)`.
- Verify peers with `SSLContext.load_verify_locations(cafile=...)` and `verify_mode=ssl.CERT_REQUIRED`.

## Creating an SSL context for a server
```py
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.pem", keyfile="key.pem")
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(cafile="ca.pem")
```

## Creating an SSL context for a client
```py
context = ssl.create_default_context(cafile="ca.pem")
context.check_hostname = False
```

## Notes
- TLS requires proper certificate management for production.
- Self-signed certs are acceptable for local testing but not for public services.
