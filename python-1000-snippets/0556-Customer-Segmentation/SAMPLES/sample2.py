# sample2.py
# Segment customers by purchase frequency and average value.


def segment_customers(records):
    segments = {'high_value': [], 'low_value': []}
    for r in records:
        if r['purchases'] > 5 and r['avg_value'] > 50:
            segments['high_value'].append(r['id'])
        else:
            segments['low_value'].append(r['id'])
    return segments


if __name__ == '__main__':
    data = [
        {'id': 1, 'purchases': 7, 'avg_value': 80},
        {'id': 2, 'purchases': 2, 'avg_value': 20},
        {'id': 3, 'purchases': 10, 'avg_value': 100},
    ]
    print('Segments:', segment_customers(data))
