# sample3.py
# generate an HTML coverage report via coverage API

def divide(a, b):
    return a / b if b != 0 else None


def test_divide():
    assert divide(4, 2) == 2
    assert divide(1, 0) is None


if __name__ == '__main__':
    import coverage

    cov = coverage.Coverage()
    cov.start()

    test_divide()

    cov.stop()
    cov.save()
    cov.html_report(directory='htmlcov')
    print('HTML report generated in ./htmlcov')

