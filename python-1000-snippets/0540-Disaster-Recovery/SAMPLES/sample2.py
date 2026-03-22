# sample2.py
# Compare primary and backup data to validate consistency.


def validate_restore(primary, backup):
    return primary == backup


if __name__ == '__main__':
    print('Valid restore:', validate_restore([1,2,3], [1,2,3]))
