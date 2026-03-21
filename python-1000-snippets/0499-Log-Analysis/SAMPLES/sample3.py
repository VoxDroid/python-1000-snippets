# sample3.py
# Writes filtered logs (login only) to temp/log_filter.txt.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/log_filter.txt')


def filter_log(lines, keyword='login'):
    return [line for line in lines if keyword in line]


def main() -> None:
    lines = [
        '[2026-03-20 08:00:00] login user=alice',
        '[2026-03-20 08:05:00] logout user=alice',
        '[2026-03-20 08:10:00] login user=bob',
    ]
    filtered = filter_log(lines)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write('\n'.join(filtered) + '\n')
    print('Wrote filtered log to', OUTPUT_PATH)


if __name__ == '__main__':
    main()