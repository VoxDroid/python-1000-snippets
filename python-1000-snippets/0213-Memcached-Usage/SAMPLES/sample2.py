# sample2.py
# Demonstrate multi-get and expiration
import time
import pylibmc

if __name__ == '__main__':
    client = pylibmc.Client(['127.0.0.1:11211'])
    client.set('k1', 'v1')
    client.set('k2', 'v2', time=1)
    print('Multi-get:', client.get_multi(['k1', 'k2']))
    time.sleep(1.1)
    print('After expiry:', client.get_multi(['k1', 'k2']))

