# sample3.py
# Compare lengths of two dictionaries

if __name__ == '__main__':
    a = {'x':1, 'y':2}
    b = {'a':1}
    if len(a) > len(b):
        print('first is larger')
    elif len(a) < len(b):
        print('second is larger')
    else:
        print('equal size')
