# sample2.py
# Simulates each bulkhead reporting status and pool size limit.


def bulkhead_status(name, max_workers):
    return {'name': name, 'max_workers': max_workers, 'available': max_workers}


if __name__ == '__main__':
    statuses = [bulkhead_status('api', 2), bulkhead_status('database', 1)]
    print('Bulkhead statuses:', statuses)
