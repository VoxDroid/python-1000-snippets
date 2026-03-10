# sample3.py
# manual iteration with next() and try/except

items = ['a', 'b', 'c']
iterator = iter(items)

if __name__ == '__main__':
    while True:
        try:
            item = next(iterator)
            print('got', item)
        except StopIteration:
            print('finished')
            break
