# sample1.py
# Generate an RSA key pair and serialize to PEM files.

import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_rsa_keypair(key_size: int = 2048):
    return rsa.generate_private_key(public_exponent=65537, key_size=key_size)


def main() -> None:
    key = generate_rsa_keypair()
    private_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_pem = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    os.makedirs("temp", exist_ok=True)
    priv_path = os.path.join("temp", "rsa_private.pem")
    pub_path = os.path.join("temp", "rsa_public.pem")

    with open(priv_path, "wb") as f:
        f.write(private_pem)
    with open(pub_path, "wb") as f:
        f.write(public_pem)

    print("Generated RSA key pair:")
    print("- Private key:", priv_path)
    print("- Public key:", pub_path)


if __name__ == "__main__":
    main()
