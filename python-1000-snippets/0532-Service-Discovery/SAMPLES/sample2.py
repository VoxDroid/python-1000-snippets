# sample2.py
# Service discovery with dynamic registration and de-registration.

registry = {}


def register(name, address):
    registry[name] = address


def deregister(name):
    registry.pop(name, None)


if __name__ == '__main__':
    register('cache', 'localhost:6379')
    print('Discover cache:', registry.get('cache'))
    deregister('cache')
    print('Discover cache after deregister:', registry.get('cache', 'not found'))
