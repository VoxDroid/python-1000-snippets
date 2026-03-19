# sample3.py
# Demonstrates sending an HTML email with multiple attachments using a local SMTP server.

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

    out_path = os.path.join(temp_dir, "smtp_html.eml")

    # Create local files to attach.
    attach1 = os.path.join(temp_dir, "notes.txt")
    attach2 = os.path.join(temp_dir, "data.csv")
    with open(attach1, "w", encoding="utf-8") as f:
        f.write("Quick notes attached.\n")
    with open(attach2, "w", encoding="utf-8") as f:
        f.write("id,value\n1,42\n")

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
        msg["Subject"] = "HTML email with attachments"
        msg.set_content("This is a fallback plain-text body.")
        msg.add_alternative(
            "<html><body><h1>Hello</h1><p>This email has attachments.</p></body></html>",
            subtype="html",
        )

        for path in (attach1, attach2):
            with open(path, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="octet-stream",
                    filename=os.path.basename(path),
                )

        import smtplib

        with smtplib.SMTP("127.0.0.1", port) as smtp:
            smtp.send_message(msg)

        print("HTML email sent; stored at:", out_path)

        with open(out_path, "r", encoding="utf-8") as f:
            data = f.read()
        print("Has HTML part:", "Content-Type: text/html" in data)
        print("Has attachments:", "Content-Disposition: attachment" in data)
    finally:
        controller.stop()


if __name__ == "__main__":
    asyncio.run(main())
