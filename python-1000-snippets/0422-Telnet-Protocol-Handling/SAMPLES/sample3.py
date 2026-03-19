# sample3.py
# Demonstrates Telnet binary mode (no encoding) and raw byte exchanges.

import asyncio
import socket

import telnetlib3


async def shell(reader, writer):
    # In binary mode, reader/writer operate on bytes.
    await writer.drain()
    data = await reader.read(1024)
    if data:
        # Echo back the data in upper-case form.
        writer.write(data.upper())
        await writer.drain()


async def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]

    server = await telnetlib3.create_server(
        host="127.0.0.1", port=port, shell=shell, encoding=False
    )

    try:
        print("Telnet binary server listening on port", port)

        reader, writer = await telnetlib3.open_connection(
            "127.0.0.1", port, encoding=False
        )

        payload = b"hello\n"
        writer.write(payload)
        await writer.drain()

        response = await reader.read(1024)
        print("Received bytes:", response)

        writer.close()
        await writer.wait_closed()

    finally:
        server.close()
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
