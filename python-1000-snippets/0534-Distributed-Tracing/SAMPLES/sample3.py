# sample3.py
# Save distributed trace events to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0534_trace_output.txt')


def trace_sequence():
    return ['span_start:root', 'span_end:root']


if __name__ == '__main__':
    events = trace_sequence()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for e in events:
            f.write(e + '\n')
    print('Wrote trace output to', OUTPUT_PATH)
