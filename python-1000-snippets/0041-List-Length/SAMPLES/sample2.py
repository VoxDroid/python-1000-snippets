# sample2.py
# Read items until blank line, then print count

if __name__ == '__main__':
    items = []
    while True:
        line = input('Enter item (blank to finish): ')
        if not line:
            break
        items.append(line)
    print('You entered', len(items), 'items')
