# sample2.py
# Simulate dynamic DAG execution with dependencies.


def task_a():
    return 1


def task_b():
    return 2


def task_c(a, b):
    return a + b


if __name__ == '__main__':
    a = task_a()
    b = task_b()
    c = task_c(a, b)
    print('Computed task graph:', {'a': a, 'b': b, 'c': c})
