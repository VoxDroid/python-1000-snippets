# sample3.py
# Compare lengths of two strings entered by user

if __name__ == '__main__':
    a = input('first: ')
    b = input('second: ')
    if len(a) > len(b):
        print('first longer')
    elif len(a) < len(b):
        print('second longer')
    else:
        print('equal length')
