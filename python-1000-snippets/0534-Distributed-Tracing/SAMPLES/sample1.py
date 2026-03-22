# sample1.py
# Simulated trace spans written to in-memory scenario.

trace_log = []

def start_span(name):
    trace_log.append(f'span_start:{name}')

def end_span(name):
    trace_log.append(f'span_end:{name}')


def do_work():
    start_span('example')
    # some work
    end_span('example')
    return trace_log


if __name__ == '__main__':
    logs = do_work()
    print('Trace entries:', logs)
