# sample3.py
# context manager that suppresses exceptions

import contextlib

@contextlib.contextmanager
def suppress_errors():
    try:
        yield
    except Exception as e:
        print('suppressed', e)

if __name__ == '__main__':
    with suppress_errors():
        print('inside')
        raise ValueError('oops')
    print('continuing after suppressed error')
