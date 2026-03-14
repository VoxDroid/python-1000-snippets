# sample3.py
# Demonstrate basic IMAP commands (NOOP/LOGOUT) with a minimal IMAP server.

import asyncio
from email.message import EmailMessage

IMAP_PORT = 1143

TEST_EMAIL = EmailMessage()
TEST_EMAIL['From'] = 'sender@example.com'
TEST_EMAIL['To'] = 'receiver@example.com'
TEST_EMAIL['Subject'] = 'IMAP Noop Test'
TEST_EMAIL.set_content('This message is used to demonstrate NOOP.')


class MiniIMAPServer:
    """Minimal IMAP server implementation for testing purposes."""

    def __init__(self, host='127.0.0.1', port=IMAP_PORT):
        self.host = host
        self.port = port
        self._server = None
        self._messages = [TEST_EMAIL]

    async def handle_client(self, reader, writer):
        writer.write(b'* OK Mini IMAP Service Ready\r\n')
        await writer.drain()

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

            if cmd == 'LOGIN':
                writer.write(f"{tag} OK LOGIN completed\r\n".encode())
            elif cmd == 'CAPABILITY':
                writer.write(b'* CAPABILITY IMAP4rev1 LITERAL+ SASL-IR\r\n')
                writer.write(f"{tag} OK CAPABILITY completed\r\n".encode())
            elif cmd == 'NOOP':
                writer.write(f"{tag} OK NOOP completed\r\n".encode())
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
    typ, data = imap.noop()
    print('NOOP response:', typ, data)
    imap.logout()


async def main():
    server = MiniIMAPServer()
    srv = await server.start()
    async with srv:
        await asyncio.to_thread(run_client)


if __name__ == '__main__':
    asyncio.run(main())
