# sample3.py
# Demonstrates mutual TLS (mTLS) where the server requires a client certificate.

import os
import ssl
import threading
import ipaddress

import datetime

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID

import requests


def _make_cert(subject_name, issuer_name, issuer_key, public_key, is_ca=False, san_names=None):
    builder = (
        x509.CertificateBuilder()
        .subject_name(subject_name)
        .issuer_name(issuer_name)
        .public_key(public_key)
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
    )

    if is_ca:
        builder = builder.add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
    else:
        builder = builder.add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)

    if san_names:
        builder = builder.add_extension(x509.SubjectAlternativeName(san_names), critical=False)

    return builder.sign(issuer_key, hashes.SHA256())


def generate_certificates(temp_dir: str):
    os.makedirs(temp_dir, exist_ok=True)

    # Generate CA
    ca_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    ca_name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "Test CA")])
    ca_cert = _make_cert(ca_name, ca_name, ca_key, ca_key.public_key(), is_ca=True)

    ca_key_path = os.path.join(temp_dir, "ca_key.pem")
    ca_cert_path = os.path.join(temp_dir, "ca_cert.pem")
    with open(ca_key_path, "wb") as f:
        f.write(
            ca_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )
    with open(ca_cert_path, "wb") as f:
        f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

    # Server key/cert signed by CA
    server_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    server_name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "localhost")])
    server_cert = _make_cert(
        server_name,
        ca_name,
        ca_key,
        server_key.public_key(),
        is_ca=False,
        san_names=[
            x509.DNSName("localhost"),
            x509.IPAddress(ipaddress.IPv4Address("127.0.0.1")),
        ],
    )

    server_key_path = os.path.join(temp_dir, "server_key.pem")
    server_cert_path = os.path.join(temp_dir, "server_cert.pem")
    with open(server_key_path, "wb") as f:
        f.write(
            server_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )
    with open(server_cert_path, "wb") as f:
        f.write(server_cert.public_bytes(serialization.Encoding.PEM))

    # Client key/cert signed by CA
    client_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    client_name = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "client")])
    client_cert = _make_cert(client_name, ca_name, ca_key, client_key.public_key(), is_ca=False)

    client_key_path = os.path.join(temp_dir, "client_key.pem")
    client_cert_path = os.path.join(temp_dir, "client_cert.pem")
    with open(client_key_path, "wb") as f:
        f.write(
            client_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )
    with open(client_cert_path, "wb") as f:
        f.write(client_cert.public_bytes(serialization.Encoding.PEM))

    return {
        "ca_cert": ca_cert_path,
        "server_cert": server_cert_path,
        "server_key": server_key_path,
        "client_cert": client_cert_path,
        "client_key": client_key_path,
    }


def run_server(cert_path: str, key_path: str, ca_path: str, port: int):
    import http.server

    server = http.server.HTTPServer(("127.0.0.1", port), http.server.SimpleHTTPRequestHandler)
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations(cafile=ca_path)
    server.socket = context.wrap_socket(server.socket, server_side=True)
    server.serve_forever()


def main() -> None:
    temp_dir = "temp"
    certs = generate_certificates(temp_dir)

    # Start server in background
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]

    server_thread = threading.Thread(
        target=run_server,
        args=(
            certs["server_cert"],
            certs["server_key"],
            certs["ca_cert"],
            port,
        ),
        daemon=True,
    )
    server_thread.start()

    # Wait until the server is accepting connections (avoid race on startup).
    def wait_for_port(host: str, port: int, timeout: float = 5.0) -> bool:
        import socket
        import time

        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                with socket.create_connection((host, port), timeout=0.5):
                    return True
            except OSError:
                time.sleep(0.05)
        return False

    host = "127.0.0.1"
    if not wait_for_port(host, port):
        raise RuntimeError(f"Server did not start on {host}:{port}")

    url = f"https://localhost:{port}/"
    print("Making mutual TLS request to", url)

    # Client will present its certificate and verify server cert via CA
    resp = requests.get(
        url,
        cert=(certs["client_cert"], certs["client_key"]),
        verify=certs["ca_cert"],
    )

    print("Response status:", resp.status_code)
    print("Response length:", len(resp.content))


if __name__ == "__main__":
    main()
