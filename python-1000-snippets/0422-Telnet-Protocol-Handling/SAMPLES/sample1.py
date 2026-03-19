# sample1.py
# Demonstrates a basic Telnet server and client using telnetlib3.

import asyncio
import socket
import telnetlib3


async def shell(reader, writer):
    writer.write("Welcome to the telnet sample. Type something and press enter.\n")
    writer.write("> ")
    await writer.drain()

    line = await reader.readline()
    if line is None:
        return

    writer.write(f"You typed: {line.strip()}\n")
    writer.write("Goodbye!\n")


async def main() -> None:
    # Find a free TCP port to run the Telnet server on.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]

    server = await telnetlib3.create_server(
        host="127.0.0.1", port=port, shell=shell, encoding="utf8"
    )

    try:
        print("Telnet server listening on port", port)

        reader, writer = await telnetlib3.open_connection("127.0.0.1", port)

        # Read the welcome text from the server.
        welcome = await reader.read(1024)
        print("Server sent:", welcome.strip())

        # Send a line to the server and read the response.
        writer.write("Hello telnet\n")
        await writer.drain()

        response = await reader.read(1024)
        print("Server response:", response.strip())

        writer.close()
        await writer.wait_closed()

    finally:
        server.close()
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
