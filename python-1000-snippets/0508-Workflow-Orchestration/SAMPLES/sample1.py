# sample1.py
# Execute a three-step workflow in order.


def step1():
    return 'step1 output'


def step2(input_data):
    return f'{input_data} -> step2 output'


def step3(input_data):
    return f'{input_data} -> step3 output'


if __name__ == '__main__':
    out1 = step1()
    out2 = step2(out1)
    out3 = step3(out2)
    print('Workflow result:', out3)
