# sample1.py
# Demonstrates sending a plain-text email using a local SMTP server.

import asyncio
import os
import tempfile
from email.message import EmailMessage

from aiosmtpd.controller import Controller


class CaptureHandler:
    """SMTP handler that captures the last received message to a file."""

    def __init__(self, out_path: str):
        self.out_path = out_path

    async def handle_DATA(self, server, session, envelope):
        # Write raw email to disk for inspection.
        with open(self.out_path, "wb") as f:
            f.write(envelope.original_content)
        return "250 Message accepted for delivery"


async def main() -> None:
    temp_dir = os.path.join(os.getcwd(), "temp")
    os.makedirs(temp_dir, exist_ok=True)

    out_path = os.path.join(temp_dir, "smtp_received.eml")

    # Find a free port to bind the SMTP server.
    import socket

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]

    handler = CaptureHandler(out_path)
    controller = Controller(handler, hostname="127.0.0.1", port=port)

    controller.start()
    try:
        print("SMTP server listening on port", port)

        msg = EmailMessage()
        msg["From"] = "sender@example.com"
        msg["To"] = "recipient@example.com"
        msg["Subject"] = "Hello from SMTP sample"
        msg.set_content("This is a plain-text message sent to a local SMTP server.")

        import smtplib

        with smtplib.SMTP("127.0.0.1", port) as smtp:
            smtp.send_message(msg)

        print("Email sent; stored at:", out_path)

        # Print the captured email for verification.
        print("--- Captured email ---")
        with open(out_path, "r", encoding="utf-8") as f:
            print(f.read())
    finally:
        controller.stop()


if __name__ == "__main__":
    asyncio.run(main())
