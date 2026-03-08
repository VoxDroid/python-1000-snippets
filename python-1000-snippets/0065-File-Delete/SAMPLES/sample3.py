# sample3.py
# Ask for filename and delete with confirmation

import os

if __name__ == '__main__':
    fname = input('Filename to delete: ')
    confirm = input(f'Delete {fname}? (y/n) ')
    if confirm.lower() == 'y':
        try:
            os.remove(fname)
            print('deleted', fname)
        except FileNotFoundError:
            print('file not found')
        except Exception as e:
            print('error', e)
    else:
        print('aborted')
