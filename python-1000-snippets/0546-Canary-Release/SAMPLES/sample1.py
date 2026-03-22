# sample1.py
# Canary release routing logic.

import random


def route_request(canary_rate=0.1):
    return 'canary' if random.random() < canary_rate else 'stable'


if __name__ == '__main__':
    print('Route:', route_request())
