# sample3.py
# Countdown timer that sleeps between ticks

import time

if __name__ == '__main__':
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print('Done!')
