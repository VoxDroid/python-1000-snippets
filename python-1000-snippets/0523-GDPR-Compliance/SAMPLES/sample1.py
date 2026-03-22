# sample1.py
# Delete user records to simulate GDPR right-to-be-forgotten.


def delete_user(records, user_id):
    return [r for r in records if r.get('user_id') != user_id]


if __name__ == '__main__':
    rows = [{'user_id': 1, 'data': 'info1'}, {'user_id': 2, 'data': 'info2'}]
    remaining = delete_user(rows, 1)
    print('Remaining records:', remaining)
