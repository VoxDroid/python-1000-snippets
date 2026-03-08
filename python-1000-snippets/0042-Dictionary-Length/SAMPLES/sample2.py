# sample2.py
# Build a dictionary from user input and show its length

if __name__ == '__main__':
    data = {}
    for i in range(3):
        key = input('Enter key: ')
        val = input('Enter value: ')
        data[key] = val
    print('resulting dict:', data)
    print('length =', len(data))
