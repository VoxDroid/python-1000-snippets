# sample1.py
# Simple failover logic choosing backup if primary fails.


def choose_server(primary_up):
    return 'primary' if primary_up else 'backup'


if __name__ == '__main__':
    print('Active server:', choose_server(False))
