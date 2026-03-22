# sample1.py
# Round-robin server selection.

servers = ['server1:8080', 'server2:8080', 'server3:8080']
index = 0


def get_server():
    global index
    server = servers[index]
    index = (index + 1) % len(servers)
    return server


if __name__ == '__main__':
    print('Selected servers:')
    for i in range(5):
        print(get_server())
