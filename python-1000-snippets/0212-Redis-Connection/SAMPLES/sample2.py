# sample2.py
# Demonstrate Redis list operations and pipeline for batching.
import redis

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    r.delete('mylist')
    r.lpush('mylist', 'one', 'two', 'three')
    print('List length:', r.llen('mylist'))
    print('List items:', r.lrange('mylist', 0, -1))

    pipe = r.pipeline()
    pipe.set('a', '1')
    pipe.set('b', '2')
    pipe.get('a')
    pipe.get('b')
    print('Pipeline results:', pipe.execute())

