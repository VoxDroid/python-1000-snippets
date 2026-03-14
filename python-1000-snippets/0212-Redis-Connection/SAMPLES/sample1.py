# sample1.py
# Basic Redis set/get using redis-py
import redis

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    r.set('python-1000', 'redis')
    print('Value:', r.get('python-1000'))

