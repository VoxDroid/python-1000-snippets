# sample1.py
# Basic Memcached set/get using pylibmc
import pylibmc

if __name__ == '__main__':
    client = pylibmc.Client(['127.0.0.1:11211'])
    client.set('python-key', 'memcached')
    print('Value:', client.get('python-key'))

