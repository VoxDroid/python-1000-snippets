# sample2.py
# Demonstrate fetching and parsing an email message via IMAP.

import asyncio
import email
from email.message import EmailMessage

IMAP_PORT = 1143

TEST_EMAIL = EmailMessage()
TEST_EMAIL['From'] = 'alice@example.com'
TEST_EMAIL['To'] = 'bob@example.com'
TEST_EMAIL['Subject'] = 'IMAP Fetch Test'
TEST_EMAIL.set_content('This is a test email for IMAP fetch example.')


class MiniIMAPServer:
    def __init__(self, host='127.0.0.1', port=IMAP_PORT):
        self.host = host
        self.port = port
        self._server = None
        self._messages = [TEST_EMAIL]

    async def handle_client(self, reader, writer):
        writer.write(b'* OK Mini IMAP Service Ready\r\n')
        await writer.drain()
        logged_in = False
        selected = False

        while not reader.at_eof():
            line = await reader.readline()
            if not line:
                break
            line = line.decode('utf-8', errors='ignore').rstrip('\r\n')
            if not line:
                continue
            parts = line.split(' ', 2)
            tag = parts[0]
            cmd = parts[1].upper() if len(parts) > 1 else ''
            args = parts[2] if len(parts) > 2 else ''

            if cmd == 'LOGIN':
                logged_in = True
                writer.write(f"{tag} OK LOGIN completed\r\n".encode())
            elif cmd == 'CAPABILITY':
                writer.write(b'* CAPABILITY IMAP4rev1 LITERAL+ SASL-IR\r\n')
                writer.write(f"{tag} OK CAPABILITY completed\r\n".encode())
            elif cmd == 'LIST':
                writer.write(b'* LIST (\\HasNoChildren) "/" "INBOX"\r\n')
                writer.write(f"{tag} OK LIST completed\r\n".encode())
            elif cmd == 'SELECT':
                selected = True
                writer.write(f"* {len(self._messages)} EXISTS\r\n".encode())
                writer.write(f"{tag} OK [READ-WRITE] SELECT completed\r\n".encode())
            elif cmd == 'SEARCH':
                writer.write(b'* SEARCH 1\r\n')
                writer.write(f"{tag} OK SEARCH completed\r\n".encode())
            elif cmd == 'FETCH':
                if not selected:
                    writer.write(f"{tag} NO SELECT a mailbox first\r\n".encode())
                    continue
                msg = self._messages[0]
                raw = msg.as_bytes()
                writer.write(f"* 1 FETCH (BODY[] {{{len(raw)}}}\r\n".encode())
                writer.write(raw)
                writer.write(b")\r\n")
                writer.write(f"{tag} OK FETCH completed\r\n".encode())
            elif cmd == 'LOGOUT':
                writer.write(b'* BYE Logging out\r\n')
                writer.write(f"{tag} OK LOGOUT completed\r\n".encode())
                await writer.drain()
                break
            else:
                writer.write(f"{tag} BAD Unknown command\r\n".encode())
            await writer.drain()

        writer.close()
        await writer.wait_closed()

    async def start(self):
        self._server = await asyncio.start_server(self.handle_client, self.host, self.port)
        return self._server

    async def stop(self):
        if self._server:
            self._server.close()
            await self._server.wait_closed()


def run_client():
    import imaplib

    imap = imaplib.IMAP4('127.0.0.1', IMAP_PORT)
    imap.login('user', 'password')
    imap.select('INBOX')
    _, data = imap.search(None, 'ALL')
    num = len(data[0].split()) if data[0] else 0
    print('Emails found:', num)
    if num:
        _, msg_data = imap.fetch(data[0].split()[0], '(BODY[])')
        raw = msg_data[0][1]
        msg = email.message_from_bytes(raw)
        print('Message subject:', msg['Subject'])
        print('From:', msg['From'])
        print('Body:', msg.get_payload())
    imap.logout()


async def main():
    server = MiniIMAPServer()
    srv = await server.start()
    async with srv:
        await asyncio.to_thread(run_client)


if __name__ == '__main__':
    asyncio.run(main())
