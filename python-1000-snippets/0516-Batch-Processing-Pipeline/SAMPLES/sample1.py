# sample1.py
# Group values in batches and sum each batch.


def batch_sum(values, batch_size=2):
    return [sum(values[i:i+batch_size]) for i in range(0, len(values), batch_size)]


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    result = batch_sum(data, 2)
    print('Batch sum:', result)
