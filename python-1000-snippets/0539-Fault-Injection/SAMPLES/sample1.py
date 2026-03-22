# sample1.py
# Fault injection wrapper for service calls.


def inject_fault(func, enabled=True):
    def wrapper(*args, **kwargs):
        if enabled:
            raise ValueError('Injected fault')
        return func(*args, **kwargs)
    return wrapper


@inject_fault
def process_request():
    return 'OK'


if __name__ == '__main__':
    try:
        print(process_request())
    except ValueError as e:
        print('Caught:', e)
