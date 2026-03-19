# sample2.py
# Demonstrates a simple interactive Telnet session with a minimal command shell.

import asyncio
import datetime
import socket

import telnetlib3


async def shell(reader, writer):
    writer.write("Welcome to the mini telnet shell.\n")
    writer.write("Commands: time, echo <text>, quit\n")

    while True:
        writer.write("> ")
        await writer.drain()

        line = await reader.readline()
        if not line:
            break

        command = line.strip()
        if not command:
            continue

        if command.lower() == "quit":
            writer.write("Goodbye!\n")
            break

        if command.lower() == "time":
            writer.write(f"Current time: {datetime.datetime.now()}\n")
            continue

        if command.lower().startswith("echo "):
            writer.write(command[5:] + "\n")
            continue

        writer.write(f"Unknown command: {command}\n")


async def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]

    server = await telnetlib3.create_server(
        host="127.0.0.1", port=port, shell=shell, encoding="utf8"
    )

    try:
        print("Telnet shell server listening on port", port)

        reader, writer = await telnetlib3.open_connection("127.0.0.1", port)

        # Consume the welcome messages.
        await reader.read(4096)

        # Send a few commands.
        writer.write("time\n")
        await writer.drain()
        out = await reader.read(4096)
        print("Time response:", out.strip())

        writer.write("echo hello world\n")
        await writer.drain()
        out = await reader.read(4096)
        print("Echo response:", out.strip())

        writer.write("quit\n")
        await writer.drain()
        out = await reader.read(4096)
        print("Final response:", out.strip())

        writer.close()
        await writer.wait_closed()

    finally:
        server.close()
        await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
