# sample3.py
# Demonstrate mutual TLS (mTLS) where both client and server present certificates.

import datetime
import os
import socket
import threading

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import ssl


def create_ca(cert_path: str, key_path: str):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Example CA"),
        x509.NameAttribute(NameOID.COMMON_NAME, "Example Root CA"),
    ])

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
        .not_valid_after(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=365))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
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

    return key, cert


def create_signed_cert(subject_cn: str, ca_key, ca_cert, cert_path: str, key_path: str):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Example"),
        x509.NameAttribute(NameOID.COMMON_NAME, subject_cn),
    ])

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(ca_cert.subject)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
        .not_valid_after(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=90))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .sign(ca_key, hashes.SHA256())
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


def run_mtls_server(ca_cert: str, server_cert: str, server_key: str, port: int, ready_event: threading.Event):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=server_cert, keyfile=server_key)
    context.load_verify_locations(cafile=ca_cert)
    context.verify_mode = ssl.CERT_REQUIRED

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind(("127.0.0.1", port))
        sock.listen(1)
        ready_event.set()
        conn, addr = sock.accept()
        with context.wrap_socket(conn, server_side=True) as ssock:
            data = ssock.recv(4096)
            ssock.sendall(b"HTTP/1.1 200 OK\r\nContent-Length: 4\r\n\r\nOK\n")


def run_mtls_client(ca_cert: str, client_cert: str, client_key: str, port: int):
    context = ssl.create_default_context(cafile=ca_cert)
    context.load_cert_chain(certfile=client_cert, keyfile=client_key)

    with socket.create_connection(("127.0.0.1", port)) as sock:
        with context.wrap_socket(sock, server_hostname="localhost") as ssock:
            ssock.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
            data = ssock.recv(1024)
            print('Client received:', data.decode().split('\r\n')[0])


def main():
    temp_dir = os.path.join(os.getcwd(), "temp", "ssl_tls_client")
    os.makedirs(temp_dir, exist_ok=True)

    ca_cert_path = os.path.join(temp_dir, "ca.crt")
    ca_key_path = os.path.join(temp_dir, "ca.key")
    server_cert_path = os.path.join(temp_dir, "server.crt")
    server_key_path = os.path.join(temp_dir, "server.key")
    client_cert_path = os.path.join(temp_dir, "client.crt")
    client_key_path = os.path.join(temp_dir, "client.key")

    ca_key, ca_cert = create_ca(ca_cert_path, ca_key_path)
    create_signed_cert("localhost", ca_key, ca_cert, server_cert_path, server_key_path)
    create_signed_cert("client", ca_key, ca_cert, client_cert_path, client_key_path)

    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(("127.0.0.1", 0))
    port = listener.getsockname()[1]
    listener.close()

    ready_event = threading.Event()
    server_thread = threading.Thread(
        target=run_mtls_server,
        args=(ca_cert_path, server_cert_path, server_key_path, port, ready_event),
    )
    server_thread.daemon = True
    server_thread.start()

    ready_event.wait(timeout=2)

    run_mtls_client(ca_cert_path, client_cert_path, client_key_path, port)

    server_thread.join(timeout=1)


if __name__ == '__main__':
    main()
