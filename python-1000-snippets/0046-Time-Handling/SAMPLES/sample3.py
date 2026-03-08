# sample3.py
# Countdown timer for a number of seconds

import time

if __name__ == '__main__':
    n = int(input('Count down seconds: '))
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print('Time up!')
