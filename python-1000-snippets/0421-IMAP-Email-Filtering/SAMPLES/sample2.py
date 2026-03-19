# sample2.py
# Demonstrates filtering emails by subject and marking a message as read using a minimal IMAP server.

import asyncio
import email
import socket
from email.message import EmailMessage

import imaplib


class SimpleIMAPServer:
    def __init__(self, messages):
        self.messages = messages
        self.logged_in = False
        self.selected = False
        self.flags = {i + 1: set() for i in range(len(messages))}

    async def start(self, host="127.0.0.1", port=0):
        self.server = await asyncio.start_server(self._handle, host, port)
        sock = self.server.sockets[0]
        self.host, self.port = sock.getsockname()[:2]
        return self

    async def stop(self):
        self.server.close()
        await self.server.wait_closed()

    async def _handle(self, reader, writer):
        writer.write(b"* OK IMAP4rev1 Service Ready\r\n")
        await writer.drain()

        while not reader.at_eof():
            line = (await reader.readline()).decode("utf-8", errors="ignore").rstrip("\r\n")
            if not line:
                break

            parts = line.split(" ", 2)
            if len(parts) < 2:
                continue
            tag, cmd = parts[0], parts[1].upper()
            args = parts[2] if len(parts) > 2 else ""

            if cmd == "CAPABILITY":
                writer.write(f"* CAPABILITY IMAP4rev1\r\n{tag} OK CAPABILITY completed\r\n".encode())

            elif cmd == "LOGIN":
                self.logged_in = True
                writer.write(f"{tag} OK LOGIN completed\r\n".encode())

            elif cmd == "SELECT":
                self.selected = True
                writer.write(f"* {len(self.messages)} EXISTS\r\n".encode())
                writer.write(f"{tag} OK [READ-WRITE] SELECT completed\r\n".encode())

            elif cmd == "SEARCH":
                criteria = args.strip()
                if criteria.upper().startswith("SUBJECT"):
                    term = criteria.split(" ", 1)[1].strip().strip('"')
                    ids = [str(i + 1) for i, m in enumerate(self.messages) if term in (m.get("Subject") or "")]
                else:
                    ids = [str(i + 1) for i in range(len(self.messages))]
                writer.write(f"* SEARCH {' '.join(ids)}\r\n".encode())
                writer.write(f"{tag} OK SEARCH completed\r\n".encode())

            elif cmd == "FETCH":
                parts = args.split(" ", 1)
                msgnum = int(parts[0]) if parts else 1
                msg = self.messages[msgnum - 1]
                headers = []
                for h in ("Subject", "From"):
                    if h in msg:
                        headers.append(f"{h}: {msg[h]}")
                raw = "\r\n".join(headers) + "\r\n\r\n"
                writer.write(f"* {msgnum} FETCH (BODY[HEADER.FIELDS (Subject From)] {{{len(raw)}}}\r\n".encode())
                writer.write(raw.encode())
                writer.write(b")\r\n")
                writer.write(f"{tag} OK FETCH completed\r\n".encode())

            elif cmd == "STORE":
                # Very basic: handle STORE <msg> +FLAGS (\Seen)
                parts = args.split(" ", 2)
                msgnum = int(parts[0]) if parts else 1
                if "+FLAGS" in args.upper():
                    self.flags[msgnum].add(r"\Seen")
                writer.write(f"{tag} OK STORE completed\r\n".encode())

            elif cmd == "LOGOUT":
                writer.write(b"* BYE IMAP4rev1 Server logging out\r\n")
                writer.write(f"{tag} OK LOGOUT completed\r\n".encode())
                break

            else:
                writer.write(f"{tag} BAD Unknown command\r\n".encode())

            await writer.drain()

        writer.close()
        await writer.wait_closed()


def build_sample_messages():
    msg1 = EmailMessage()
    msg1["From"] = "alice@example.com"
    msg1["To"] = "bob@example.com"
    msg1["Subject"] = "Project update"
    msg1.set_content("Project is on track.")

    msg2 = EmailMessage()
    msg2["From"] = "carol@example.com"
    msg2["To"] = "bob@example.com"
    msg2["Subject"] = "Budget review"
    msg2.set_content("Please review the budget.")

    return [msg1, msg2]


def _run_client(port: int) -> None:
    client = imaplib.IMAP4("127.0.0.1", port)
    client.login("user", "pass")
    client.select("INBOX")

    typ, data = client.search(None, 'SUBJECT', '"Project"')
    print("Search response type:", typ)
    print("Message IDs with 'Project' in subject:", data)

    if data and data[0]:
        msgid = data[0].split()[0]
        client.store(msgid, "+FLAGS", "(\\Seen)")
        print(f"Marked message {msgid.decode()} as seen")

    client.logout()


async def main() -> None:
    messages = build_sample_messages()
    server = await SimpleIMAPServer(messages).start()

    try:
        print("IMAP server listening on port", server.port)
        await asyncio.to_thread(_run_client, server.port)
    finally:
        await server.stop()


if __name__ == "__main__":
    asyncio.run(main())
