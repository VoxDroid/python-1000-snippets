# sample1.py
# Start a local TLS server and connect to it as a client.

import datetime
import os
import socket
import threading

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import ssl


def create_self_signed_cert(cert_path: str, key_path: str):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Local Test"),
            x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
        ]
    )
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
        .not_valid_after(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1))
        .add_extension(x509.SubjectAlternativeName([x509.DNSName("localhost")]), critical=False)
        .sign(key, hashes.SHA256())
    )

    with open(key_path, "wb") as f:
        f.write(
            key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    with open(cert_path, "wb") as f:
        f.write(cert.public_bytes(serialization.Encoding.PEM))


def run_tls_server(cert_path: str, key_path: str, port: int, ready_event: threading.Event):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind(("127.0.0.1", port))
        sock.listen(1)
        ready_event.set()
        conn, addr = sock.accept()
        with context.wrap_socket(conn, server_side=True) as ssock:
            data = ssock.recv(4096)
            # Simple HTTP response
            ssock.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello world")


def run_client(cert_path: str, port: int):
    context = ssl.create_default_context(cafile=cert_path)
    with socket.create_connection(("127.0.0.1", port)) as sock:
        with context.wrap_socket(sock, server_hostname="localhost") as ssock:
            ssock.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
            data = ssock.recv(1024)
            print('Client received:', data.decode().split('\r\n')[0])


def main():
    temp_dir = os.path.join(os.getcwd(), "temp", "ssl_tls_client")
    os.makedirs(temp_dir, exist_ok=True)

    cert_path = os.path.join(temp_dir, "server.crt")
    key_path = os.path.join(temp_dir, "server.key")

    create_self_signed_cert(cert_path, key_path)

    # Use port 0 to auto-allocate a free port
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(("127.0.0.1", 0))
    port = listener.getsockname()[1]
    listener.close()

    ready_event = threading.Event()
    server_thread = threading.Thread(target=run_tls_server, args=(cert_path, key_path, port, ready_event))
    server_thread.daemon = True
    server_thread.start()

    # Wait until server is listening
    ready_event.wait(timeout=2)

    run_client(cert_path, port)
    server_thread.join(timeout=1)


if __name__ == '__main__':
    main()
