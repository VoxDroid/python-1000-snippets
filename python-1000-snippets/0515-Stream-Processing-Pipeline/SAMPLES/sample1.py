# sample1.py
# Rolling window mean over a stream of values.

from collections import deque


def rolling_mean(stream, window_size=2):
    window = deque()
    total = 0
    for value in stream:
        window.append(value)
        total += value
        if len(window) > window_size:
            total -= window.popleft()
        if len(window) == window_size:
            yield total / window_size
        else:
            yield None


if __name__ == '__main__':
    data_stream = [1, 2, 3, 4, 5]
    result = list(rolling_mean(data_stream, window_size=2))
    print('Rolling mean:', result)
