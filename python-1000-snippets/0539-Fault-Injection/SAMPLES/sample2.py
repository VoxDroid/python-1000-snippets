# sample2.py
# Toggle fault injection at runtime.


def process_request():
    return 'OK'


def call_request(should_fault=False):
    if should_fault:
        raise RuntimeError('Injected runtime fault')
    return process_request()


if __name__ == '__main__':
    try:
        print(call_request(should_fault=True))
    except RuntimeError as e:
        print('Caught:', e)
