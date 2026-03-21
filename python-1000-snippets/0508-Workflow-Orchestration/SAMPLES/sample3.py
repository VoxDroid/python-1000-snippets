# sample3.py
# Save workflow step execution trace to temp file.

import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../../temp/0508_workflow_trace.txt')


def step(n):
    return f'step{n} done'


if __name__ == '__main__':
    events = []
    for i in range(1, 5):
        events.append(step(i))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        for e in events:
            f.write(e + '\n')

    print('Workflow trace written to', OUTPUT_PATH)
