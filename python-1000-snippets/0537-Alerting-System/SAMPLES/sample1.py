# sample1.py
# Simple alert trigger based on condition.


def alert(condition, message):
    if condition:
        return f'Alert: {message}'
    return 'OK'


if __name__ == '__main__':
    print(alert(True, 'CPU usage high'))
