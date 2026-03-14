# sample2.py
# Generate a certificate signing request (CSR) using cryptography.

from cryptography import x509
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID


def main():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    csr = (
        x509.CertificateSigningRequestBuilder()
        .subject_name(
            x509.Name(
                [
                    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
                    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
                    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
                    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Example Co"),
                    x509.NameAttribute(NameOID.COMMON_NAME, "example.com"),
                ]
            )
        )
        .sign(private_key, hashes.SHA256())
    )

    key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    csr_pem = csr.public_bytes(serialization.Encoding.PEM)

    print('Private key (PEM):')
    print(key_pem.decode())
    print('CSR (PEM):')
    print(csr_pem.decode())


if __name__ == '__main__':
    main()
