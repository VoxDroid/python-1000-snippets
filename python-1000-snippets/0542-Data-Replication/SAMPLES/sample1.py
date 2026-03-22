# sample1.py
# Simple data replication from primary to replica object.


def replicate(primary):
    return primary.copy()


if __name__ == '__main__':
    prim = {'key': 'value'}
    print('Replica:', replicate(prim))
