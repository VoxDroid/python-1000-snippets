# sample1.py
# Start a local Telnet server and connect to it using telnetlib3.

import asyncio
import telnetlib3

HOST = '127.0.0.1'
PORT = 8023


async def shell(reader, writer):
    # Simple echo shell
    writer.write('Welcome to the test Telnet server!\n')
    while True:
        line = await reader.readline()
        if line is None:
            break
        if line.strip().lower() in ('quit', 'exit'):
            writer.write('Bye!\n')
            break
        writer.write(f'Echo: {line}')

    writer.close()


async def run():
    server = await telnetlib3.create_server(host=HOST, port=PORT, shell=shell)

    try:
        reader, writer = await telnetlib3.open_connection(HOST, PORT)
        welcome = await reader.read(1024)
        print('Server says:', welcome.strip())

        writer.write('hello\n')
        response = await reader.read(1024)
        print('Server echoed:', response.strip())

        writer.write('exit\n')
        goodbye = await reader.read(1024)
        print('Server says:', goodbye.strip())

        writer.close()
        await writer.wait_closed()
    finally:
        server.close()
        await server.wait_closed()


if __name__ == '__main__':
    asyncio.run(run())
