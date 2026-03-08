# sample2.py
# show manual iteration using iter() and next()

if __name__ == '__main__':
    letters = ['a', 'b', 'c']
    it = iter(letters)
    try:
        while True:
            print(next(it))
    except StopIteration:
        print('done')
