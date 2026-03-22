# sample2.py
# Replicate an array to multiple nodes.


def distribute(data, nodes):
    return {node: list(data) for node in nodes}


if __name__ == '__main__':
    print(distribute([1, 2, 3], ['nodeA', 'nodeB']))
