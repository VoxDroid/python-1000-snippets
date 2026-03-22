# sample2.py
# Simulate incremental backup by appending changed entries.


def incremental_backup(base_data, new_data):
    return base_data + [item for item in new_data if item not in base_data]


if __name__ == '__main__':
    print('Incremental result:', incremental_backup([1,2,3], [3,4,5]))
