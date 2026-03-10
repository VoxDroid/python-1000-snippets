# sample1.py
# simple program with programmatic coverage measurement

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def test_add():
    # only testing one function on purpose
    assert add(2, 3) == 5


if __name__ == '__main__':
    # run the test under coverage and print a report
    import coverage

    cov = coverage.Coverage()
    cov.start()

    test_add()

    cov.stop()
    cov.save()
    cov.report()  # prints coverage to stdout

