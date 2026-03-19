# sample2.py
# Demonstrates sending an email with a file attachment via a local SMTP server.

import asyncio
import os
import tempfile
from email.message import EmailMessage

from aiosmtpd.controller import Controller


class CaptureHandler:
    def __init__(self, out_path: str):
        self.out_path = out_path

    async def handle_DATA(self, server, session, envelope):
        with open(self.out_path, "wb") as f:
            f.write(envelope.original_content)
        return "250 Message accepted for delivery"


async def main() -> None:
    temp_dir = os.path.join(os.getcwd(), "temp")
    os.makedirs(temp_dir, exist_ok=True)

    out_path = os.path.join(temp_dir, "smtp_attachment.eml")

    # Create a local file to attach.
    attach_path = os.path.join(temp_dir, "attachment.txt")
    with open(attach_path, "w", encoding="utf-8") as f:
        f.write("This is the attachment content.\n")

    # Find a free port for the SMTP server.
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
        msg["Subject"] = "Attachment example"
        msg.set_content("Please see the attached file.")

        with open(attach_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="text",
                subtype="plain",
                filename=os.path.basename(attach_path),
            )

        import smtplib

        with smtplib.SMTP("127.0.0.1", port) as smtp:
            smtp.send_message(msg)

        print("Email with attachment sent; stored at:", out_path)

        # Verify the captured message contains the attachment header.
        with open(out_path, "r", encoding="utf-8") as f:
            content = f.read()
        print("Attachment header present:", "Content-Disposition: attachment" in content)
    finally:
        controller.stop()


if __name__ == "__main__":
    asyncio.run(main())
