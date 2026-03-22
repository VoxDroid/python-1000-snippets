# sample3.py
# ETL step counts/logging in temp stats.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0519_etl_stats.txt')


def etl_stats():
    raw = [1, None, 3]
    transformed = [(x if x is not None else 0) * 2 for x in raw]
    return {'raw_count': len(raw), 'output_count': len(transformed), 'total': sum(transformed)}


if __name__ == '__main__':
    stats = etl_stats()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for k, v in stats.items():
            f.write(f'{k}: {v}\n')
    print('Wrote ETL stats to', OUTPUT_PATH)
