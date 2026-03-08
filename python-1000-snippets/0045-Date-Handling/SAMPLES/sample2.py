# sample2.py
# Parse a date string entered by the user and display weekday

from datetime import datetime

if __name__ == '__main__':
    s = input('Enter date (YYYY-MM-DD): ')
    try:
        dt = datetime.strptime(s, '%Y-%m-%d')
        print('Parsed date:', dt.date())
        print('Weekday:', dt.strftime('%A'))
    except ValueError:
        print('Invalid format')
