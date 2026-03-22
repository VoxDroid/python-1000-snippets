# sample2.py
# Stream filtering and transformation pipeline.


def stream_generator(n):
    for i in range(n):
        yield i


def pipeline(stream):
    return [x * 2 for x in stream if x % 2 == 0]


if __name__ == '__main__':
    data = stream_generator(10)
    transformed = pipeline(data)
    print('Transformed stream:', transformed)
