# sample3.py
# Use argparse to parse an optional --count parameter

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Demo argparse')
    parser.add_argument('--count', type=int, default=1,
                        help='number of times to print hello')
    args = parser.parse_args()
    for i in range(args.count):
        print('Hello', i+1)
