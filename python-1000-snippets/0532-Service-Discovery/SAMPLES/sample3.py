# sample3.py
# Write discovered services to temp file for debugging/auditing.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0532_service_discovery.txt')


def discover(service_name, registry):
    return registry.get(service_name, 'Service not found')


if __name__ == '__main__':
    services = {'api': 'localhost:8080', 'db': 'localhost:5432'}
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for name in ['api', 'db', 'cache']:
            address = discover(name, services)
            f.write(f'{name} -> {address}\n')
    print('Wrote service discovery report to', OUTPUT_PATH)
