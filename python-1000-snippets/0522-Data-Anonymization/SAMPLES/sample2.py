# sample2.py
# Anonymize email and phone fields in records.


def anonymize_record(rec):
    return {
        'email': 'anon@example.com',
        'phone': '000-000-0000',
        'id': rec.get('id')
    }


if __name__ == '__main__':
    records = [{'id': 1, 'email': 'a@example.com', 'phone': '1234'}, {'id': 2, 'email': 'b@example.com', 'phone': '5678'}]
    anon = [anonymize_record(r) for r in records]
    print('Anonymized records:', anon)
