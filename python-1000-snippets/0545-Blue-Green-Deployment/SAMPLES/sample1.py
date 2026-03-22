# sample1.py
# Toggle blue-green deployment environment.


def switch_env(active):
    return 'green' if active == 'blue' else 'blue'


if __name__ == '__main__':
    print('New active:', switch_env('blue'))
