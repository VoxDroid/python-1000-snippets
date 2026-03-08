# sample1.py
# Show several time formats based on current time

from datetime import datetime

if __name__ == '__main__':
    now = datetime.now()
    print('raw datetime:', now)
    print('24h format:', now.strftime('%H:%M:%S'))
    print('12h format:', now.strftime('%I:%M:%S %p'))
    print('hour only:', now.strftime('%H'))
