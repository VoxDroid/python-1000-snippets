# sample1.py
# Send a basic email using a local SMTP server (aiosmtpd) for testing.

import asyncio
from email.message import EmailMessage
import smtplib

from aiosmtpd.controller import Controller


class CollectingHandler:
    """Simple handler that collects received messages in memory."""

    def __init__(self):
        self.messages = []

    async def handle_DATA(self, server, session, envelope):
        self.messages.append(envelope)
        return "250 Message accepted for delivery"


def run_smtp_server(host='127.0.0.1', port=1025):
    handler = CollectingHandler()
    controller = Controller(handler, hostname=host, port=port)
    controller.start()
    return controller, handler


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 1025

    controller, handler = run_smtp_server(host, port)
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Hello from SMTP sample'
        msg['From'] = 'sender@example.com'
        msg['To'] = 'receiver@example.com'
        msg.set_content('This is a test email sent via a local SMTP server.')

        with smtplib.SMTP(host, port) as smtp:
            smtp.send_message(msg)

        print('Sent email; server received', len(handler.messages), 'message(s).')
        if handler.messages:
            env = handler.messages[0]
            print('First message subject:', env.mail_from, '->', env.rcpt_tos)
            print('Raw payload length:', len(env.content))
    finally:
        controller.stop()
