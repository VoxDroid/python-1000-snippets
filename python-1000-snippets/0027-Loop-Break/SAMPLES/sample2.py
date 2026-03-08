# sample2.py
# Read lines until user types 'stop'.

if __name__ == '__main__':
    while True:
        s = input()
        if s.strip().lower() == 'stop':
            break
        print('You entered', s)

