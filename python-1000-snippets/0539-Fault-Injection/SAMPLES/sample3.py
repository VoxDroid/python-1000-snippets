# sample3.py
# Write fault test results to file.

import os

OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'temp', '0539_fault.txt'))


def test_fault():
    results = {'success': 0, 'fail': 0}
    for i in range(3):
        try:
            if i == 1:
                raise Exception('injected')
            results['success'] += 1
        except Exception:
            results['fail'] += 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(str(results) + '\n')
    return results


if __name__ == '__main__':
    print('Results:', test_fault())
    print('Written to', OUTPUT_PATH)
