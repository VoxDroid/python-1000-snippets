# sample2.py
# Send an HTML email with an attachment using a local SMTP server.

import mimetypes
from email.message import EmailMessage
import smtplib

from aiosmtpd.controller import Controller


class CollectingHandler:
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
        msg['Subject'] = 'HTML + Attachment'
        msg['From'] = 'sender@example.com'
        msg['To'] = 'receiver@example.com'
        msg.set_content('This is a fallback plain text body.')
        msg.add_alternative('<html><body><h1>Hello</h1><p>This is <b>HTML</b>.</p></body></html>', subtype='html')

        # Add a small text attachment
        attachment_data = b'This is an attachment.'
        maintype, subtype = mimetypes.guess_type('attachment.txt')[0].split('/')
        msg.add_attachment(attachment_data, maintype=maintype, subtype=subtype, filename='attachment.txt')

        with smtplib.SMTP(host, port) as smtp:
            smtp.send_message(msg)

        print('Sent HTML email; server received', len(handler.messages), 'message(s).')
        if handler.messages:
            print('First message size (bytes):', len(handler.messages[0].content))
    finally:
        controller.stop()
