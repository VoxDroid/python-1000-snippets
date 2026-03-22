# sample2.py
# Generate nested spans and output event counts.


def nested_trace():
    events = []
    events.append('span_start:outer')
    events.append('span_start:inner')
    events.append('span_end:inner')
    events.append('span_end:outer')
    return events


if __name__ == '__main__':
    events = nested_trace()
    print('Nested trace events:', events)
