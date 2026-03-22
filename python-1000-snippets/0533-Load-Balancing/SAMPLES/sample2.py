# sample2.py
# Weighted round-robin selection.

weights = {'server1:8080': 3, 'server2:8080': 1}
servers = list(weights.keys())
current = 0


def get_weighted_server():
    global current
    total = sum(weights.values())
    r = current % total
    acc = 0
    for server, w in weights.items():
        acc += w
        if r < acc:
            current += 1
            return server


if __name__ == '__main__':
    print('Weighted selection:')
    for i in range(8):
        print(get_weighted_server())
