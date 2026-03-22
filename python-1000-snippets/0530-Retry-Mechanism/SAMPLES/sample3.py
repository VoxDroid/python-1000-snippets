# sample3.py
# Log retry attempts to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0530_retry_log.txt')


def run_with_logging(action, attempts=3):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    for i in range(attempts):
        try:
            result = action()
            with open(OUTPUT_PATH, 'a') as f:
                f.write(f'attempt {i+1}: success\n')
            return result
        except Exception as e:
            with open(OUTPUT_PATH, 'a') as f:
                f.write(f'attempt {i+1}: fail {e}\n')
    return 'failed'


if __name__ == '__main__':
    state = {'count': 0}

    def flaky():
        state['count'] += 1
        if state['count'] < 2:
            raise Exception('bad')
        return 'ok'

    print('Result:', run_with_logging(flaky, attempts=3))
    print('Retry log path: ', OUTPUT_PATH)
