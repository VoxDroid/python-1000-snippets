# sample2.py
# Load a self-signed certificate and print its subject/issuer details.

import os
from cryptography import x509


def main() -> None:
    cert_path = os.path.join("temp", "selfsigned_cert.pem")
    if not os.path.exists(cert_path):
        print("Certificate not found; run sample1.py to generate it.")
        return

    with open(cert_path, "rb") as f:
        cert = x509.load_pem_x509_certificate(f.read())

    print("Subject:", cert.subject.rfc4514_string())
    print("Issuer:", cert.issuer.rfc4514_string())
    print("Not valid before:", cert.not_valid_before)
    print("Not valid after:", cert.not_valid_after)


if __name__ == "__main__":
    main()
