# sample2.py
# Use majority health checking for high availability.


def quorum(nodes, check):
    healthy = sum(1 for n in nodes if check(n))
    return healthy >= (len(nodes) // 2 + 1)


if __name__ == '__main__':
    print('Quorum reached:', quorum(['n1', 'n2', 'n3'], lambda n: n != 'n2'))
