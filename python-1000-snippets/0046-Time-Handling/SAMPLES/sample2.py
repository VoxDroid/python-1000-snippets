# sample2.py
# Parse time string and indicate AM/PM

from datetime import datetime

if __name__ == '__main__':
    s = input('Enter time (HH:MM:SS): ')
    try:
        t = datetime.strptime(s, '%H:%M:%S').time()
        print('Parsed time:', t)
        print('AM/PM:', 'AM' if t.hour < 12 else 'PM')
    except ValueError:
        print('Invalid time format')
