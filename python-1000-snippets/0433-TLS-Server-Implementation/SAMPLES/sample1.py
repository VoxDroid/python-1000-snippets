# sample1.py
# Demonstrates a simple TLS server using Python's ssl module and a self-signed certificate.

import datetime
import http.server
import ipaddress
import os
import ssl
import threading

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def generate_self_signed_cert(cert_path: str, key_path: str):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    subject = issuer = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Example"),
            x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
        ]
    )

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .add_extension(
            x509.SubjectAlternativeName(
                [
                    x509.DNSName("localhost"),
                    x509.IPAddress(ipaddress.IPv4Address("127.0.0.1")),
                ]
            ),
            critical=False,
        )
        .sign(key, hashes.SHA256())
    )

    os.makedirs("temp", exist_ok=True)
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


def main() -> None:
    cert_path = os.path.join("temp", "tls_cert.pem")
    key_path = os.path.join("temp", "tls_key.pem")
    generate_self_signed_cert(cert_path, key_path)

    server = http.server.HTTPServer(("127.0.0.1", 0), http.server.SimpleHTTPRequestHandler)
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)
    server.socket = context.wrap_socket(server.socket, server_side=True)

    host, port = server.server_address
    print("TLS server listening on https://127.0.0.1:%d" % port)

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    # Make a connection to the server using a client SSL context that trusts our cert.
    client_context = ssl.create_default_context(cafile=cert_path)

    import urllib.request

    url = f"https://127.0.0.1:{port}/"
    with urllib.request.urlopen(url, context=client_context) as resp:
        print("Response status:", resp.status)
        print("Response length:", len(resp.read()))

    server.shutdown()
    thread.join()


if __name__ == "__main__":
    main()
