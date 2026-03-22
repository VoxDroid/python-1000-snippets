# sample2.py
# Simulate primary health probe with failover.


def failover_strategy(primary_health, backup_health):
    if primary_health:
        return 'primary'
    if backup_health:
        return 'backup'
    return 'unavailable'


if __name__ == '__main__':
    print('Chosen:', failover_strategy(False, True))
