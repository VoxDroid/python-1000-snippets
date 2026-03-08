# sample2.py
# context manager for opening a file (mocked headless)

import contextlib

@contextlib.contextmanager
def open_file(name):
    print(f'opening {name}')
    yield f'file({name})'
    print(f'closing {name}')

if __name__ == '__main__':
    with open_file('test.txt') as f:
        print('got', f)
