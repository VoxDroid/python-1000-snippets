# sample3.py
# Write batch processing metadata to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0516_batch_processing.txt')


def batch_stats(values, batch_size):
    batched = [values[i:i+batch_size] for i in range(0, len(values), batch_size)]
    return {'batches': len(batched), 'total': sum(values)}


if __name__ == '__main__':
    stats = batch_stats(list(range(20)), 5)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for k,v in stats.items():
            f.write(f'{k}: {v}\n')
    print('Written batch stats to', OUTPUT_PATH)
