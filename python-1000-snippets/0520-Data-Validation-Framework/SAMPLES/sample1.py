# sample1.py
# Validate data values are in expected range.

def validate(values, min_v=0, max_v=10):
    return all(min_v <= v <= max_v for v in values)


if __name__ == '__main__':
    data = [1, 2, 3]
    is_valid = validate(data)
    print('Validation completed:' , is_valid)
