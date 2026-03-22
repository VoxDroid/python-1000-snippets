# sample1.py
# Execute basic ETL in-memory from raw data to transformed output.


def extract():
    return [1, None, 3]


def transform(records):
    return [(x if x is not None else 0) * 2 for x in records]


def load(output):
    return output


if __name__ == '__main__':
    raw_data = extract()
    transformed = transform(raw_data)
    result = load(transformed)
    print('ETL result:', result)
