# sample3.py
# Demonstrate increment/decrement and delete
import pylibmc

if __name__ == '__main__':
    client = pylibmc.Client(['127.0.0.1:11211'])
    client.set('counter', 0)
    client.incr('counter', 5)
    client.decr('counter', 2)
    print('Counter value:', client.get('counter'))
    client.delete('counter')
    print('After delete:', client.get('counter'))

