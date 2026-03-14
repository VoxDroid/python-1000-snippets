# sample3.py
# Generate a CA certificate and sign a CSR to issue a leaf certificate.

import datetime

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def main():
    # CA key and self-signed cert
    ca_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    ca_subject = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Example CA"),
            x509.NameAttribute(NameOID.COMMON_NAME, "Example Root CA"),
        ]
    )

    ca_cert = (
        x509.CertificateBuilder()
        .subject_name(ca_subject)
        .issuer_name(ca_subject)
        .public_key(ca_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=365))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .sign(ca_key, hashes.SHA256())
    )

    # Leaf key and CSR
    leaf_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    csr = (
        x509.CertificateSigningRequestBuilder()
        .subject_name(
            x509.Name(
                [
                    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
                    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Example Org"),
                    x509.NameAttribute(NameOID.COMMON_NAME, "www.example.com"),
                ]
            )
        )
        .sign(leaf_key, hashes.SHA256())
    )

    # Issue leaf certificate signed by CA
    leaf_cert = (
        x509.CertificateBuilder()
        .subject_name(csr.subject)
        .issuer_name(ca_cert.subject)
        .public_key(csr.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=90))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .sign(ca_key, hashes.SHA256())
    )

    print('CA Certificate (PEM):')
    print(ca_cert.public_bytes(serialization.Encoding.PEM).decode())
    print('Leaf Certificate (PEM):')
    print(leaf_cert.public_bytes(serialization.Encoding.PEM).decode())


if __name__ == '__main__':
    main()
