# sample1.py
# Simulated disaster recovery restore operation.


def restore_from_backup(backup):
    return backup.get('data', [])


if __name__ == '__main__':
    backup_data = {'data': [1, 2, 3]}
    print('Restored:', restore_from_backup(backup_data))
