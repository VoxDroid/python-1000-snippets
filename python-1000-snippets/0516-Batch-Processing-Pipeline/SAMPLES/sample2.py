# sample2.py
# Process data in batches and apply a transformation per batch.


def process_batch(values, batch_size):
    batches = []
    for i in range(0, len(values), batch_size):
        batch = values[i:i+batch_size]
        batches.append([x*2 for x in batch])
    return batches


if __name__ == '__main__':
    print('Batches:', process_batch(list(range(10)), 3))
