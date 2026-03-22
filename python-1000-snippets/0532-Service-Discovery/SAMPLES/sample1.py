# sample1.py
# Lookup service addresses in a service registry.

services = {'api': 'localhost:8080', 'db': 'localhost:5432'}


def discover(service_name):
    return services.get(service_name, 'Service not found')


if __name__ == '__main__':
    print('API address:', discover('api'))
    print('Cache service address:', discover('cache'))
