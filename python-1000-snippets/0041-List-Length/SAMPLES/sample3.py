# sample3.py
# Compare lengths of two lists

if __name__ == '__main__':
    a = [1,2,3]
    b = [4,5]
    if len(a) > len(b):
        print('First list is longer')
    elif len(a) < len(b):
        print('Second list is longer')
    else:
        print('Lists are same length')
