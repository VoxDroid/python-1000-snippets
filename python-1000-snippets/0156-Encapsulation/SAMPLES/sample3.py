# sample3.py
# demonstrate name mangling of private attributes

class Secret:
    def __init__(self, data):
        self.__data = data
    def reveal(self):
        return self.__data

if __name__ == '__main__':
    s = Secret('hidden')
    print('reveal:', s.reveal())
    # direct access fails
    try:
        print(s.__data)
    except AttributeError as e:
        print('attr error', e)
    # hack via mangled name
    print('mangled access', s._Secret__data)
