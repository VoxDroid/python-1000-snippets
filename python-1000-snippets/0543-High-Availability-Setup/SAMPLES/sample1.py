# sample1.py
# Determine available nodes assuming health checks.


def available_nodes(nodes, check):
    return [n for n in nodes if check(n)]


def always_up(n):
    return True


if __name__ == '__main__':
    print('Up nodes:', available_nodes(['node1', 'node2'], always_up))
